from fastapi import FastAPI, File, UploadFile
from app.api.routes.image_processing import image_processing_router

app = FastAPI()

@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)):
    # Placeholder for file saving and processing
    return {"filename": file.filename, "status": "uploaded"}

app.include_router(image_processing_router, prefix="/api")
