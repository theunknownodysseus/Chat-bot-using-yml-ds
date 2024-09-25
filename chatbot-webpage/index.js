import React from 'react';
import Chatbot from './components/Chatbot';  // Correct path to Chatbot component
import './App.css';  // Import CSS file for styling

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Chatbot</h1>
            </header>
            <Chatbot />  {/* Render the Chatbot component */}
        </div>
    );
}

export default App;
