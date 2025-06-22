# 🗣️ Text-to-Speech Converter

A multilingual web application that converts text into spoken voice using various input formats like plain text, uploaded files, and images. The app also includes OCR (Optical Character Recognition) to extract text from images.

## 🔧 Features

- ✅ Convert plain text into speech
- ✅ Upload `.txt` or `.docx` files for voice conversion
- ✅ Upload images to extract and convert text using OCR
- ✅ Support for multiple languages (e.g., English, Hindi, Telugu)
- ✅ User-friendly interface for input and output

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django
- **Libraries Used:** 
  - `gTTS` or `pyttsx3` for Text-to-Speech
  - `pytesseract` for OCR
  - `Django` for the backend

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/ChilukuriSivaKarthikeya/Text-to-speech-convertor-project.git

# Navigate into the project directory
cd Text-to-speech-convertor-project

# Install dependencies (make sure virtualenv is activated)
pip install -r requirements.txt

# Start the server
python manage.py runserver
