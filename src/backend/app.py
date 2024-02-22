from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
from io import BytesIO
from openai import OpenAI
from gtts import gTTS

app = Flask(__name__)
CORS(app, resources={r"/translate": {"origins": "http://localhost:3000"}})
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI

@app.route('/')
def home():
    return 'Welcome to my Flask app!'


@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    query = data.get('query')

    try:
        # First translation: English to Korean
        completion_korean = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Translate the following English text to Korean: '{query}'",
            max_tokens=100,
            temperature=0.5
        )
        translated_text_korean = completion_korean.choices[0].text.strip()

        # Convert the Korean text to speech and encode it as Base64
        tts = gTTS(text=translated_text_korean, lang='ko')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        mp3_data = mp3_fp.read()
        base64_audio = base64.b64encode(mp3_data).decode('utf-8')

        return jsonify({
            'koreanPhrase': translated_text_korean,
            'base64Audio': base64_audio
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
