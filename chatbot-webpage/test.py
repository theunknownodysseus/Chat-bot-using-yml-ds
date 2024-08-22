import nltk
from nltk.chat.util import Chat, reflections
import yaml
import os

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
            print(f"Unexpected conversation format: {conversation}")
    return pairs

# Load patterns from the chloned Chatterbot Corpus files
directory_path = r"C:\Users\SUBHA SHREE SV\OneDrive\ドキュメント\All_Folder\Hackathon\SIH24\working chatbot\datasets"  # Update with your path
pairs = load_yaml_files(directory_path)

# Create a chatbot instance with the loaded patterns
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm your chatbot. Type 'quit' to exit.")
chatbot.converse()
