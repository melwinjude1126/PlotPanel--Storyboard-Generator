import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import glob

load_dotenv()

app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# The code was using `genai.Client()` which is not correct for the `google-generativeai` library.
# I am replacing it with `genai.GenerativeModel`.
# I am using 'gemini-pro' which is a text model. The 'google-generativeai' library and the standard
# Gemini models do not support text-to-image generation directly. You would typically need to use
# the Vertex AI SDK with an Imagen model for that, which requires a different setup.
# This corrected code will call the Gemini API, which will likely return a text description
# of the requested image, not the image itself. The application will save a placeholder image
# and print the model's text response to the console.
try:
    model = genai.GenerativeModel('gemini-2.5-flash-image')
except Exception as e:
    print(f"Error creating model: {e}")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    script = request.form['script']
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    image_paths = []

    # Clear old storyboard images
    old_images = glob.glob(os.path.join(os.path.dirname(__file__), 'static/images/storyboard_*.png'))
    for img_path in old_images:
        try:
            os.remove(img_path)
        except Exception as e:
            print(f"Error removing old image {img_path}: {e}")

    if not model:
        return jsonify({'error': 'Model could not be initialized.'}), 500

    for i, line in enumerate(lines):
        try:
            # The prompt is kept to request an image, so you can see the text-based response from the model.
            prompt = f"Generate a single, high-quality, cinematic storyboard image for the following scene, focusing on the key actions and characters. The image should be in a 16:9 aspect ratio. Scene: {line}"
            
            response = model.generate_content(prompt)

            # The following block attempts to find image data in the response.
            # With 'gemini-pro', this will not succeed. It's here to show what would be needed
            # if the model could generate images.
            image_generated = False
            if response.parts:
                for part in response.parts:
                    # Check for 'inline_data' which is how images would be returned.
                    if hasattr(part, 'inline_data') and part.inline_data:
                        image_data = part.inline_data.data
                        image_path = f"static/images/storyboard_{i}.png"
                        with open(os.path.join(os.path.dirname(__file__), image_path), "wb") as f:
                            f.write(image_data)
                        image_paths.append(image_path)
                        image_generated = True
                        break
            
            if not image_generated:
                print(f"No image generated for line: {line}")
                if response.text:
                    print(f"Model response: {response.text}")
                # Fallback to a placeholder image
                image_paths.append("static/images/placeholder.png")

        except Exception as e:
            print(f"Error generating content for line: {line}\n{e}")
            image_paths.append("static/images/placeholder.png")

    return jsonify({'images': image_paths})

if __name__ == '__main__':
    app.run(debug=True)
