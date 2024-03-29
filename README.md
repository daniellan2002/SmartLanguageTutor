# SmartLanguageTutor
This application is designed to provide a simple and interactive way for users to translate English phrases or queries into Korean, leveraging the capabilities of GPT-based models for accurate and context-aware translations. Here's a brief overview of its functionality:

## Frontend (React): 
Offers a user-friendly interface where users can input their English text or queries about how to say something in Korean. It includes a form for inputting the text and a button to submit the query. Once the translation is processed, it displays the translated Korean phrase and provides an audio playback feature for hearing the correct pronunciation.

## Backend (Flask): 
Acts as an intermediary between the frontend and the OpenAI API. It receives the user's query from the frontend, processes it through the OpenAI's GPT model to translate the text into Korean, and then uses Google's Text-to-Speech to convert the translated text into an audio file. The backend returns both the Korean text and a link to the audio file back to the frontend for display and playback.



The app aims to make it easy for users to not only get translations of English phrases into Korean but also to hear the pronunciation, enhancing learning and ensuring correct usage of phrases in real-life conversations. This combination of text and audio output provides a comprehensive tool for language learners, travelers, or anyone interested in Korean language and culture.



## Setup Instructions:

### Backend Setup:

####  Step 1: Navigate to the /backend directory.

#### Step 2: Install Python dependencies: 
- pip install -r requirements.txt

#### Step 3: Run the Flask app: 
- python app.py.


### Frontend Setup:

#### Step 1: Set Up Your Frontend with React

- npx create-react-app my-translation-app

- cd my-translation-app

- npm install

- npm start


#### Step 2: Install Axios for making HTTP requests:
- npm install axios


## Testing Backend

### Simple Curl Command:
-  curl -X POST http://127.0.0.1:5000/translate -H "Content-Type: application/json" -d '{"query":"Hello, how are you?"}'

