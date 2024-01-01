# app.py

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get user input from the request using request.form.get
    user_text = request.form.get('user_text', '')
    userwith = 2000
    try:
        # Make a request to your FastAPI endpoint
        response = requests.post(
            'http://37.60.173.43:8080/sdapi/v1/txt2img',
            json={'prompt': user_text, 'negative_prompt': 'nsfw', 'width': userwith}
        )
        response.raise_for_status()  # Raise an error for HTTP errors

        # Assume the API responds with an image encoded in base64 under "images" field
        base64_image = response.json().get('images', [])[0]  # Assuming it's a list

        # Print the base64 string
        print(f"Received Base64 Image: {base64_image}")

        return jsonify({'base64_image': base64_image})

    except Exception as e:
        # Log or print the error
        print(f"Error generating image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)