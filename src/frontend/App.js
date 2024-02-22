import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [koreanPhrase, setKoreanPhrase] = useState('');
  const [base64Audio, setBase64Audio] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/translate', { query });
      setKoreanPhrase(response.data.koreanPhrase);
      setBase64Audio(response.data.base64Audio);
    } catch (error) {
      console.error('Error during translation:', error);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter text to translate"
        />
        <button type="submit">Translate</button>
      </form>
      {koreanPhrase && <p>Translation: {koreanPhrase}</p>}
      {base64Audio && (
        <audio
          controls
          src={`data:audio/mp3;base64,${base64Audio}`}>
          Your browser does not support the audio element.
        </audio>
      )}
    </div>
  );
}

export default App;
