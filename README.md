# Sidhufy

A vibe coded web application that converts your text into Navjot Singh Sidhu's unique style of speaking using Google's Gemini API.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://localhost:5000`

## Features

- Simple and aesthetic user interface
- Real-time text conversion to Sidhu's style
- Support for multiple input languages
- Responsive design

## Note

This application uses Google's Gemini API, which requires an API key. Make sure to keep your API key secure and never commit it to version control. 