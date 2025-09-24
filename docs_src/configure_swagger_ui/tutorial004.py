from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": 2})


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
