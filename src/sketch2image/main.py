from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

# Mount the 'frontend' directory to serve static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# Create a directory to store uploaded and generated images
os.makedirs("images", exist_ok=True)

@app.post("/generate-image/")
async def generate_image_endpoint(
    sketch: UploadFile = File(...),
    model: str = Form("nano-banana"),
):
    """
    Endpoint to receive a sketch and generate an image.
    """
    sketch_path = f"images/{sketch.filename}"
    with open(sketch_path, "wb") as buffer:
        buffer.write(await sketch.read())

    from .models import generate_image
    output_path = f"images/generated_{sketch.filename}"
    generate_image(sketch_path, output_path, model)

    return FileResponse(output_path)

@app.get("/")
async def read_root():
    return FileResponse('frontend/index.html')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
