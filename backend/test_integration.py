import asyncio
import aiofiles
import requests
import time
import tempfile
import subprocess
from pathlib import Path
import json

BASE_URL = "http://localhost:8000"

def create_test_video():
    """Create a simple test video using ffmpeg"""
    temp_dir = Path(tempfile.mkdtemp())
    video_path = temp_dir / "test_video.mp4"
    
    cmd = [
        "ffmpeg", "-f", "lavfi", "-i", "testsrc=duration=5:size=320x240:rate=30",
        "-c:v", "libx264", "-t", "5", str(video_path)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Failed to create test video: {result.stderr}")
    
    return video_path

def test_health_endpoint():
    """Test the health endpoint"""
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/healthz")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    print("✓ Health endpoint working")

def test_video_encoding():
    """Test the complete video encoding workflow"""
    print("Testing video encoding workflow...")
    
    test_video_path = create_test_video()
    print(f"Created test video: {test_video_path}")
    
    try:
        with open(test_video_path, 'rb') as f:
            files = {'file': ('test_video.mp4', f, 'video/mp4')}
            response = requests.post(f"{BASE_URL}/encode", files=files)
        
        assert response.status_code == 200
        result = response.json()
        job_id = result["job_id"]
        assert result["status"] == "processing"
        print(f"✓ Video upload successful, job_id: {job_id}")
        
        max_wait_time = 60  # 60 seconds max wait
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            response = requests.get(f"{BASE_URL}/status/{job_id}")
            assert response.status_code == 200
            status = response.json()
            
            print(f"Job status: {status['status']}, progress: {status.get('progress', 0)}%")
            
            if status["status"] == "completed":
                break
            elif status["status"] == "error":
                raise Exception(f"Encoding failed: {status.get('error', 'Unknown error')}")
            
            time.sleep(2)
        else:
            raise Exception("Encoding timed out")
        
        print("✓ Video encoding completed")
        
        assert "outputs" in status
        outputs = status["outputs"]
        expected_qualities = ["low", "medium", "high"]
        
        for quality in expected_qualities:
            assert quality in outputs
            output_info = outputs[quality]
            assert "filename" in output_info
            assert "quality" in output_info
            assert "path" in output_info
            print(f"✓ {quality} quality ({output_info['quality']}) created: {output_info['filename']}")
        
        for quality in expected_qualities:
            response = requests.get(f"{BASE_URL}/download/{job_id}/{quality}")
            assert response.status_code == 200
            assert response.headers["content-type"] == "video/mp4"
            assert len(response.content) > 0
            print(f"✓ {quality} quality download working")
        
        print("✓ All quality levels successfully created and downloadable")
        
    finally:
        test_video_path.unlink()
        test_video_path.parent.rmdir()

def test_invalid_file_upload():
    """Test uploading non-video file"""
    print("Testing invalid file upload...")
    
    temp_dir = Path(tempfile.mkdtemp())
    text_file = temp_dir / "test.txt"
    text_file.write_text("This is not a video file")
    
    try:
        with open(text_file, 'rb') as f:
            files = {'file': ('test.txt', f, 'text/plain')}
            response = requests.post(f"{BASE_URL}/encode", files=files)
        
        assert response.status_code == 400
        assert "File must be a video" in response.json()["detail"]
        print("✓ Invalid file upload properly rejected")
        
    finally:
        text_file.unlink()
        temp_dir.rmdir()

def test_job_not_found():
    """Test accessing non-existent job"""
    print("Testing job not found...")
    
    fake_job_id = "non-existent-job-id"
    response = requests.get(f"{BASE_URL}/status/{fake_job_id}")
    assert response.status_code == 404
    assert "Job not found" in response.json()["detail"]
    print("✓ Non-existent job properly returns 404")

def run_all_tests():
    """Run all integration tests"""
    print("Starting integration tests...")
    print("=" * 50)
    
    try:
        test_health_endpoint()
        test_invalid_file_upload()
        test_job_not_found()
        test_video_encoding()
        
        print("=" * 50)
        print("✅ All integration tests passed!")
        return True
        
    except Exception as e:
        print("=" * 50)
        print(f"❌ Test failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
