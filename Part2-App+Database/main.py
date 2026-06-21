# Created by Aswin KS
# Date: 20-06-2026
# About the Project: This is a simple Python Fast API to create passport size photos. Program accept an image file and creates the passport size image matching the resolution.
# Why this Project: Aim of this project is not to build the best app, but to learn system design. This app is required as a sample demo application to demonstrate different use cases when learning system design concepts.



from fastapi import FastAPI, UploadFile, File # Import fastAPI package.
from fastapi.responses import StreamingResponse  #StreamingResponse is used for images, videos etc

from image_processor import make_passport_size  # Our operational logic is in file "image_processor.py" . we are importing it to main.

app = FastAPI(title="Passport Photo API")  # Starts your web server
from database import SessionLocal
from models import PhotoJob



@app.post("/resize-passport") # This creates an HTTP endpoint:
async def resize_passport(file: UploadFile = File(...)):  # File operations can be slow. Using async allows FastAPI to handle other requests while waiting for file I/O.

    db = SessionLocal()
    try:
        # 1. Create DB job entry
        job = PhotoJob(
            filename=file.filename,
            status="PROCESSING"
        )

        db.add(job)
        db.commit()
        db.refresh(job)    


    # Read Image
        image_bytes = await file.read()    # File is temporarily stored in memory/disk .  .read() converts it into raw bytes

        # Process Image
        processed_image = make_passport_size(image_bytes)  # Calls the make_passport_size method in the image_processor.py file

        # Update job status in DB
        job.status = "COMPLETED"
        db.commit()


        # Return Processed Image
        return StreamingResponse(  #It tells FastAPI: Don’t convert this to JSON,  send raw bytes directly”
            processed_image,  # in-memory image file
            media_type="image/jpeg" # This tells browser: This response is an image
        )


    finally:
        db.close()