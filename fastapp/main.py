import os
import shutil
from fastapi import FastAPI, File, HTTPException, UploadFile, status
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="FastAPI Image Upload")

# Setup upload directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve uploaded images statically so they can be viewed via URL
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

# Allowed MIME types for images
ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"]


@app.post("/upload-image/", status_code=status.HTTP_201_CREATED)
async def upload_image(file: UploadFile = File(...)):
    # 1. Validate file type
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format. Only JPEG, PNG, GIF, and WEBP are allowed.",
        )

    # 2. Define target file destination
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # 3. Save file asynchronously to avoid blocking the event loop
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "url": f"/static/{file.filename}",
    }