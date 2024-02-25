from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
from io import BytesIO
import openai  # Corrected import
from gtts import gTTS

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})


# Set the OpenAI API key directly
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return 'Welcome to my Flask app!'

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    app.logger.info('Headers added by after_request')
    return response

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    query = data.get('query')

    try:
        # Corrected API call
        completion_korean = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Translate the following English text to Korean: {query}"},
            ],
            temperature=0.5,
        )
        # Accessing the last message for the translated text
        translated_text_korean = completion_korean.choices[0].message.content.strip()

        # Convert the Korean text to speech and encode it as Base64
        tts = gTTS(text=translated_text_korean, lang='ko')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        mp3_data = mp3_fp.read()
        base64_audio = base64.b64encode(mp3_data).decode('utf-8')

        # Assuming you're returning this in a Flask route
        return jsonify({
            'koreanPhrase': translated_text_korean,
            'base64Audio': base64_audio
        })
    except Exception as e:
        # Handle exception
        print(f"An error occurred: {e}")
        # Assuming this is part of a Flask route, you may want to return an error response
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
