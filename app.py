from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')

def sanitize_input(text):
    # Remove any HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove any potential command injection attempts
    text = re.sub(r'[;&|`]', '', text)
    # Remove any newlines that could break the prompt
    text = text.replace('\n', ' ').replace('\r', '')
    # Limit to 280 characters
    return text[:280].strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sidhufy', methods=['POST'])
def sidhufy():
    try:
        text = request.json.get('text', '')
        
        # Sanitize the input
        sanitized_text = sanitize_input(text)
        
        if not sanitized_text:
            return jsonify({"error": "Please enter some text to convert"}), 400
        
        # Create the prompt for Gemini with proper escaping
        prompt = f"""You are a Chatbot that Sidhu-fy the sentences that people feed you. 
        Navjot Singh Sidhu is a former cricketer that is famous for his unique style of commentary. 
        He usually includes different Dohe in his commentary and has very unique bag of words. 
        Convert the following text into how Sidhu would say it in Hindi Language and not Hindi written in English. Sprinkle some Dohe in the text sometime and keep the response 2-3 sentences: {sanitized_text}"""
        
        response = model.generate_content(prompt)
        sidhufied_text = response.text
        
        return jsonify({"result": sidhufied_text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 