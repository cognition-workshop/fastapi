from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import aiofiles
import asyncio
import subprocess
import os
import uuid
import shutil
from pathlib import Path
from typing import Dict, List

app = FastAPI()

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

jobs: Dict[str, Dict] = {}

QUALITY_PRESETS = {
    "low": {
        "resolution": "640x360",
        "bitrate": "500k",
        "name": "360p"
    },
    "medium": {
        "resolution": "1280x720", 
        "bitrate": "1500k",
        "name": "720p"
    },
    "high": {
        "resolution": "1920x1080",
        "bitrate": "3000k", 
        "name": "1080p"
    }
}

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.post("/encode")
async def encode_video(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith('video/'):
        raise HTTPException(status_code=400, detail="File must be a video")
    
    job_id = str(uuid.uuid4())
    
    file_extension = Path(file.filename).suffix
    input_path = UPLOAD_DIR / f"{job_id}{file_extension}"
    
    async with aiofiles.open(input_path, 'wb') as f:
        content = await file.read()
        await f.write(content)
    
    jobs[job_id] = {
        "status": "processing",
        "progress": 0,
        "outputs": {},
        "original_filename": file.filename
    }
    
    asyncio.create_task(process_video(job_id, input_path))
    
    return {"job_id": job_id, "status": "processing"}

async def process_video(job_id: str, input_path: Path):
    try:
        output_files = {}
        total_qualities = len(QUALITY_PRESETS)
        
        for i, (quality_key, preset) in enumerate(QUALITY_PRESETS.items()):
            output_filename = f"{job_id}_{preset['name']}.mp4"
            output_path = OUTPUT_DIR / output_filename
            
            cmd = [
                "ffmpeg", "-i", str(input_path),
                "-vf", f"scale={preset['resolution']}",
                "-b:v", preset['bitrate'],
                "-c:v", "libx264",
                "-preset", "fast",
                "-y",  # Overwrite output files
                str(output_path)
            ]
            
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode != 0:
                jobs[job_id]["status"] = "error"
                jobs[job_id]["error"] = f"FFmpeg error for {quality_key}: {stderr.decode()}"
                return
            
            output_files[quality_key] = {
                "filename": output_filename,
                "quality": preset['name'],
                "path": str(output_path)
            }
            
            progress = int(((i + 1) / total_qualities) * 100)
            jobs[job_id]["progress"] = progress
        
        jobs[job_id]["status"] = "completed"
        jobs[job_id]["outputs"] = output_files
        
        input_path.unlink()
        
    except Exception as e:
        jobs[job_id]["status"] = "error"
        jobs[job_id]["error"] = str(e)

@app.get("/status/{job_id}")
async def get_job_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return jobs[job_id]

@app.get("/download/{job_id}/{quality}")
async def download_video(job_id: str, quality: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = jobs[job_id]
    if job["status"] != "completed":
        raise HTTPException(status_code=400, detail="Job not completed")
    
    if quality not in job["outputs"]:
        raise HTTPException(status_code=404, detail="Quality not found")
    
    output_info = job["outputs"][quality]
    file_path = Path(output_info["path"])
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=file_path,
        filename=f"{Path(job['original_filename']).stem}_{output_info['quality']}.mp4",
        media_type="video/mp4"
    )

@app.get("/jobs")
async def list_jobs():
    return {"jobs": jobs}
