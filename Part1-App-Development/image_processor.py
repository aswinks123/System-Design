from PIL import Image  # It can opens and manipulates images
import io


def make_passport_size(image_bytes: bytes):
    image = Image.open(io.BytesIO(image_bytes))  # Load image from bytes

    # Convert to RGB 
    image = image.convert("RGB")  # RGB = standard color format

    width, height = image.size # Get image size

    # ---- center crop to square ----
    min_side = min(width, height)  # Pick smaller side so image becomes square-safe

    left = (width - min_side) // 2       #This ensures face stays centered. Assuming face is in the middle.
    top = (height - min_side) // 2
    right = left + min_side
    bottom = top + min_side

    image = image.crop((left, top, right, bottom))   # cuts image into square. removes extra edges

    # ---- resize to passport size ----
    image = image.resize((600, 600))   # passport-photo like output

    # save to bytes
    output = io.BytesIO()  # create empty in-memory file
    image.save(output, format="JPEG") # save processed image into memory
    output.seek(0)  # Moves pointer back to start: write > pointer at end  and read > pointer must go back to start

    return output  # This is what FastAPI sends to browser.