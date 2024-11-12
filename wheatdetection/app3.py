from flask import Flask, request, render_template
from roboflow import Roboflow
import cv2
import os

# Optionally load environment variables from a .env file
# from dotenv import load_dotenv
# load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("ROBOFLOW_API_KEY")
if not api_key:
    raise EnvironmentError("ROBOFLOW_API_KEY environment variable not set")

# Initialize Roboflow with your API key
rf = Roboflow(api_key=api_key)  # Use environment variable

# Load your project and model
project = rf.workspace().project("ragi-usesw")  # Replace with your project name
model = project.version(1).model  # Replace with your model version number

# Initialize Flask app
app = Flask(__name__)

# Ensure the 'static' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

# Function to draw bounding boxes on image
def draw_bounding_boxes(img_path, predictions):
    img = cv2.imread(img_path)
    for box in predictions:
        x0 = int(box['x'] - box['width'] / 2)
        y0 = int(box['y'] - box['height'] / 2)
        x1 = int(box['x'] + box['width'] / 2)
        y1 = int(box['y'] + box['height'] / 2)
        cv2.rectangle(img, (x0, y0), (x1, y1), (0, 255, 0), 2)
    return img

# Home route to render HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to upload image and predict
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # Save the uploaded image
    file_path = os.path.join('static', file.filename)
    file.save(file_path)

    # Check if file was saved correctly
    if not os.path.exists(file_path):
        return f"Error: The file {file.filename} was not saved correctly."

    # Run inference via Roboflow's API
    try:
        prediction = model.predict(file_path, confidence=40, overlap=30).json()
    except Exception as e:
        return f"Error during prediction: {str(e)}"

    # Count number of trees detected
    detected_trees = len(prediction['predictions'])

    # Draw bounding boxes on the image
    img_with_boxes = draw_bounding_boxes(file_path, prediction['predictions'])
    
    # Save the result image
    result_img_path = os.path.join('static', 'result_' + file.filename)
    cv2.imwrite(result_img_path, img_with_boxes)

    # Return the HTML page with the tree count and result image
    return render_template('result.html', num_trees=detected_trees, result_image=result_img_path)

# Start Flask app
if __name__ == '__main__':
    app.run(debug=True)
