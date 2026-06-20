from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse  #StreamingResponse is used for images, videos etc

from image_processor import make_passport_size  # Our operational logic is in file "image_processor.py" . we are importing it to main.

app = FastAPI(title="Passport Photo API")  # Starts your web server


@app.post("/resize-passport") # This creates an HTTP endpoint:
async def resize_passport(file: UploadFile = File(...)):  # File operations can be slow. Using async allows FastAPI to handle other requests while waiting for file I/O.
    image_bytes = await file.read()    # File is temporarily stored in memory/disk .  .read() converts it into raw bytes

    processed_image = make_passport_size(image_bytes)  # Calls the make_passport_size method in the image_processor.py file

    return StreamingResponse(  #It tells FastAPI: Don’t convert this to JSON,  send raw bytes directly”
        processed_image,  # in-memory image file
        media_type="image/jpeg" # This tells browser: This response is an image
    )