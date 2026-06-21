
# PART 2: Integrating a Database with the Python API application 

Our goal in this part is to integrate postgres databse with the application.

Database will store the following details:

1. File name uploaded, 2. Status of Job (Processing/Completed), 3. Created time, 4. Completed time.




## Why we need a Database?

```
The API:

Accepts an image upload
Converts image to RGB format
Center-crops the image into a square
Resizes it to 600x600 pixels
Returns the processed image directly in the response
```

## Request Flow

Client → FastAPI → Image Processing (Pillow) → Response Image


## Technology Added

```
Python
FastAPI
Pillow (PIL)
Uvicorn
```



## What Part2 Teaches?

This Part is used to understand:
```
File upload handling in APIs
Binary data processing
Basic image processing (crop, resize)
Stateless API design
CPU-bound workloads inside APIs
```

## Limitations  (We will fix these limitations when we move forward)

This project is intentionally simple and has several limitations:

```

❗️ No Queue System

Image processing is synchronous

API waits until processing is complete

Not scalable for heavy load

❗️ No Cache Layer

Reprocesses the same image every time

No optimization for repeated requests

❗️ No Background Workers

CPU‑heavy tasks run inside the API process

Can block the server under load

❗️ No Scalability Design

Single‑process execution

No load balancing or distributed workers

❗️ Not Micro-service based

API is currenly standalone/monoloth.

Containerizing it would improve scaling.

```

## Learning Goal

Understand how to integrate a database with Python application for permanent data storage.



## Sample Screenshots





## Dependencies 



```
pip install fastapi uvicorn pillow python-multipart

```


## How to Run the API?

```
python -m uvicorn main:app
```




# Next Step:

Check part 3 to learn how to integrate a Caching Mechanism (Redis) with this App.