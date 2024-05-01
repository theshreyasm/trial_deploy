from flask import Flask, render_template, request, jsonify
from tut import generate  # Import your generate function
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

# Route for handling image upload and caption generation
@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file is uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    # Check if the file extension is allowed
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file extension'})

    # Save the uploaded image with the desired filename
    filename = 'captured_image.png'
    file.save(filename)

    # Process the uploaded image and generate the caption
    # You need to implement this part based on your generate() function
    # Assuming generate() function takes an image file as input
    caption = generate(filename)

    return caption

if __name__ == '__main__':
    app.run(debug=True)
