from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import requests
app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) to allow requests from the frontend
origins = ["*"]  # Update this list with the appropriate origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(request: Request):
    try:
        # Extract data from the request body
        data = await request.json()
        user_text = data.get('prompt')
        width = data.get('width')
        height = data.get('height')
        negative_prompt = data.get('negative_prompt')  # Added line for negative prompt

        # Make a request to your external server for image generation
        # Replace the URL with the actual URL of your external server
        # Update the payload structure as needed
        response = requests.post('http://37.60.173.43:8080/sdapi/v1/txt2img', json={
            'text': user_text,
            'width': width,
            'height': height,
            'negative_prompt': negative_prompt  # Added line for negative prompt
        })

        # Assume the API responds with an image encoded in base64
        base64_image = response.json().get('images')

        return JSONResponse(content=jsonable_encoder({'images': base64_image}))
    except Exception as e:
        return JSONResponse(content=jsonable_encoder({'error': str(e)}), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

if __name__ == "__main__":
    import uvicorn

  
