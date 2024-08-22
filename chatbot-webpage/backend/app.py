from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.chat.util import Chat, reflections
import yaml
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allows requests from any origin

# Function to load and parse the YAML files from the Chatterbot Corpus
def load_yaml_files(directory):
    pairs = []
    for filename in os.listdir(directory):
        if filename.endswith(".yml"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                for conversation in data['conversations']:
                    if len(conversation) >= 2:
                        pattern = conversation[0]
                        response = conversation[1]
                        pairs.append([pattern.strip(), [response.strip()]])
        else:
            print(f"Unexpected conversation format: {filename}")
    return pairs

# Load patterns from the YAML files in the datasets directory
directory_path = 'datasets'  # Path to the datasets directory
pairs = load_yaml_files(directory_path)

# Create a chatbot instance with the loaded patterns
chatbot = Chat(pairs, reflections)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        print(f"Received message: {user_message}")  # Debugging line
        if not user_message:
            return jsonify({'reply': 'No message provided'}), 400
        # Generate response from the chatbot
        reply = chatbot.respond(user_message)
        print(f"Chatbot reply: {reply}")  # Debugging line
        return jsonify({'reply': reply})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'reply': 'Sorry, something went wrong.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
