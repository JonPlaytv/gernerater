from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get JSON data from the request
        data = request.json
        user_text = data.get('prompt', '')  # Assuming 'prompt' is the key for user text
        width = int(data.get('width', 512))  # Assuming 'width' is the key for width, defaulting to 512
        height = int(data.get('height', 512))  # Assuming 'height' is the key for height, defaulting to 512

        # Make a request to your FastAPI endpoint with updated resolution
        response = requests.post('http://37.60.173.43:8080/sdapi/v1/txt2img', json={
            'prompt': user_text,
            'width': width,
            'height': height
            # Include other parameters as needed
        })

        # Print or log the received response for debugging
        print("FastAPI Response:", response.text)

        # Assume the API responds with an image encoded in base64
        base64_image = response.json().get('base64_image')

        # Print or log the base64 image for debugging
        print("Base64 Image:", base64_image)

        return jsonify({'base64_image': base64_image})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
