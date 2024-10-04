
# **PicturePerfect: AI-Driven Image Describer**

## **Overview**
**PicturePerfect** is an AI-powered application designed to generate comprehensive descriptions for uploaded images. By leveraging the **Gemini model**, users can simply upload an image, optionally provide a prompt, and receive a rich, text-based description of the image's contents. This tool is perfect for those looking to analyze and understand the key elements of visual content quickly and accurately.

## **Features**
- **Upload Image**: Accepts JPG, JPEG, and PNG image formats.
- **Custom Prompt**: Optionally input a text prompt to guide the AI’s description.
- **Detailed Descriptions**: Uses advanced AI to provide insightful details about the image.
- **Image Metadata**: Displays information such as image dimensions, file type, and format.
- **Custom Styling**: Clean, responsive UI with intuitive navigation and design.
- **Error Handling**: Provides meaningful feedback for missing inputs or issues during the description process.

## **Tech Stack**
- **Python**: Backend language for the application logic.
- **Streamlit**: Framework for building the interactive user interface.
- **Google Gemini API**: Powered by Google's Gemini model to analyze and generate descriptions.
- **Pillow (PIL)**: For image processing and manipulation.
- **dotenv**: To securely manage environment variables.

## **Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/atharv2001j/pictureperfect.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd pictureperfect
    ```

3. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Set up API key**:  
   Create a `.env` file in the root directory and add your Google API key:
    ```bash
    GOOGLE_API_KEY=your-google-api-key
    ```

## **Usage**

1. **Run the application**:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to the URL provided (usually `http://localhost:8501`).

3. **Upload an image**: Select an image file in JPG, JPEG, or PNG format.
   
4. **Optional prompt**: You can add a text prompt to guide the AI's description, or leave it blank for automatic analysis.

5. **Analyze Image**: Click the "Analyze Image" button to generate the image description.

## **Project Structure**

```
PicturePerfect
│
├── app.py                # Main application code
├── README.md             # Project documentation
├── requirements.txt      # Required Python packages
├── .env                  # Environment variables for API key (not included in repository)
├── assets/               # Static assets (e.g., logos, images)
└── ...
```

## **Example Output**

1. **Uploaded Image**
   
2. **Generated Description**:  

## **Future Improvements**
- Add support for multiple image formats.
- Enhance the UI with additional customization options.
- Implement a feature to export image descriptions as downloadable files.
- Expand AI model support for more precise image analysis.

## **Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests to enhance this project.

## **Contact**
For any inquiries or suggestions, please reach out to:
- **Email**: joshiatharv67@gmail.com
- **Demo**: https://www.loom.com/share/a15342ecaadc4a069a7fd06cde7115a4?sid=db9deba8-67e4-4132-a536-7cc4dd4542bb

