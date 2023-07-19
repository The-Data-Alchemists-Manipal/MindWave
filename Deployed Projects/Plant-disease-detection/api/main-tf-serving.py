from fastapi import FastAPI, File ,UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests

app = FastAPI()

endpoint = 'http://localhost:8501/v1/models/Disease_model:predict'
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
@app.get("/ping")
async def ping():
    return "Hello I'm alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image,0)
    json_data = {
        "instances":img_batch.tolist()
    }
    response = requests.post(endpoint,json=json_data)
    prediction = np.array(response.json()["predictions"][0])
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)

    return{
        "class" : predicted_class,
        "confidence" : float(confidence)
    }

    

if __name__ =="__main__":
    uvicorn.run(app,host='localhost',port=8000)