import React, { useState } from 'react';
import './Chatbot.css';

function Chatbot() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (input.trim() === "") return;
    
        const newMessages = [...messages, { sender: 'user', text: input }];
        setMessages(newMessages);
    
        try {
            const response = await fetch('http://localhost:5000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: input })
            });
    
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            const data = await response.json();
            console.log('Bot response:', data.reply); // Log the bot's response
            setMessages([...newMessages, { sender: 'bot', text: data.reply }]);
        } catch (error) {
            console.error('Error fetching chatbot response:', error);
            setMessages([...newMessages, { sender: 'bot', text: 'Sorry, something went wrong.' }]);
        }
        setInput('');
    };
    

    return (
        <div className="chat-container">
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <form onSubmit={handleSubmit} className="input-container">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type a message..."
                />
                <button type="submit">Send</button>
            </form>
        </div>
    );
}

export default Chatbot;
