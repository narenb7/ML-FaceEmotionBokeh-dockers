from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()
face-bokeh = ec2-54-157-42-29.compute-1.amazonaws.com
face-emotion = ec2-54-157-42-29.compute-1.amazonaws.com
@app.get("/", tags=["Health Check"])
async def root():
#   return {"message": "Service is Online"}

     r1 = requests.get("http://ec2-54-157-42-29.compute-1.amazonaws.com:8001/")
     r2 = requests.get("http://ec2-54-157-42-29.compute-1.amazonaws.com:8002/")
     return r1.text, r2.text

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/


#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
