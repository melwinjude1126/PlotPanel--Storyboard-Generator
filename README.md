# PlotPanel - AI Storyboard Generator

![Storyboard Generator Screenshot](static/images/storyboard_3.png)

PlotPanel is a web-based application that leverages the power of Google's Gemini AI to automatically generate storyboard images from a written script. This tool is perfect for filmmakers, content creators, and writers who want to quickly visualize their stories.

## Features

-   **AI-Powered Image Generation**: Utilizes Google's Gemini Pro model to interpret your script and generate corresponding images.
-   **Simple Web Interface**: An intuitive and easy-to-use interface for entering your script and viewing the generated storyboard.
-   **Dynamic Image Grid**: The generated storyboard images are displayed in a clean, responsive grid layout.
-   **Loading State**: Provides feedback to the user while the AI is generating the images.
-   **Placeholder Support**: If an image cannot be generated, a placeholder is shown, ensuring the storyboard flow is not interrupted.

## How to Use

1.  **Enter Your Script**: Open the PlotPanel web application and you will see a text area. Enter your script, with each line representing a different scene or shot.
2.  **Generate Storyboard**: Click the "Generate Storyboard" button.
3.  **View Your Storyboard**: The application will process your script and display the generated storyboard images.

## Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/plotpanel.git
    cd plotpanel
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file. See the "Technologies Used" section for the necessary packages.)*

3.  **Set up your environment variables:**
    -   Create a file named `.env` in the root of the project.
    -   Add your Google Gemini API key to the `.env` file:
        ```
        GEMINI_API_KEY=your_api_key_here
        ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  Open your web browser and go to `http://127.0.0.1:5000`.

## Technologies Used

-   **Backend**:
    -   [Flask](https://flask.palletsprojects.com/): A lightweight WSGI web application framework in Python.
    -   [google-generativeai](https://pypi.org/project/google-generativeai/): The Python library for the Google Gemini API.
    -   [python-dotenv](https://pypi.org/project/python-dotenv/): To manage environment variables.
    -   [Pillow](https://python-pillow.org/): For image manipulation (although the current Gemini model does not return images).

-   **Frontend**:
    -   HTML5
    -   CSS3
    -   JavaScript
    -   [Font Awesome](https://fontawesome.com/): for icons.

Here are the contents for a `requirements.txt` file:
```
Flask
google-generativeai
python-dotenv
Pillow
```

## Limitations

-   The current version of the `google-generativeai` library and the `gemini-2.5-flash-image` model do not support direct text-to-image generation. The model will return a *textual description* of the requested image, not the image itself. The application is set up to handle image data if the model supported it, but for now, it will display a placeholder image for each scene. The model's text response is printed to the console.
-   For actual text-to-image generation with Google's models, you would typically need to use the Vertex AI SDK with a model like Imagen.

## Future Improvements

-   Integrate with a text-to-image model like Imagen to generate actual images.
-   Allow users to customize the style of the generated images.
-   Add the ability to save and export the generated storyboard as a PDF or a set of image files.
-   Implement user accounts and project management.
