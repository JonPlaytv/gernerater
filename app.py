from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get user input from the request
    user_text = request.json.get('prompt')  # assuming your request structure has 'prompt'

    # Make a request to your FastAPI endpoint
    response = requests.post('http://37.60.173.43:8080/sdapi/v1/txt2img', json={'text': user_text})

    # Assume the API responds with an image encoded in base64
    base64_image = response.json().get('images')
    print(response.text)
    return jsonify({'images': base64_image})

@app.route('/queue/status')
def queue_status():
    # Make a request to the external server for queue status
    response = requests.get('http://37.60.173.43:8080/queue/status')

    # Return the response from the external server
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
