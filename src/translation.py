import os
from openai import OpenAI
from gtts import gTTS

# Initialize OpenAI client
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


def translate_text_and_provide_meaning(text, source_lang='en', target_lang='ko'):
    try:
        # First translation: English to Korean
        completion_korean = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Only reply the Korean result: '{text}'",
            max_tokens=100,
            temperature=0.5
        )
        translated_text_korean = completion_korean.choices[0].text.strip()
        print(f"Translated Text (Korean): {translated_text_korean}")

        completion_analysis = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Explain how to use this phrase and in what context: '{text}'",
            max_tokens=100,
            temperature=0.5
        )
        korean_analysis = completion_analysis.choices[0].text.strip()
        print(f"Usage Help: {korean_analysis}")

        # Use gTTS for converting the Korean text to speech
        tts = gTTS(text=translated_text_korean, lang='ko')
        tts.save("output.mp3")
        print("Audio file saved as 'output.mp3'")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        user_input = input("Enter English text to translate into Korean: ")
        translate_text_and_provide_meaning(user_input)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
