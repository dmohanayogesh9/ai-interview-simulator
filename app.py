from flask import Flask, request, jsonify
from flask_cors import CORS
from llamafactory.chat import ChatModel
from llamafactory.extras.misc import torch_gc

args = dict(
  model_name_or_path="meta-llama/Llama-3.2-1B-Instruct", # use bnb-4bit-quantized Llama-3-8B-Instruct model
  adapter_name_or_path="C:\\Users\\kkris\\Project Ai interviewer\\adapter\\content\\LLaMA-Factory\\llama3_lora",                        # load the saved LoRA adapters
  template="llama3",                                         # same to the one in training
  finetuning_type="lora",                                    # same to the one in training
)
chat_model = ChatModel(args)
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Endpoint to handle user messages
@app.route('/reply', methods=['POST'])
def reply():
    user_message = request.json.get('message')

    # Customize this logic to generate the reply
    reply = generate_reply(user_message)
    print(reply)
    # Send the reply back to the frontend
    return jsonify({'reply': reply})

# Function to generate a reply (you can modify this)
def generate_reply(user_message):
    # Ensure messages is always a list
    messages = [{"role": "user", "content": user_message}]

    response = ""
    for new_text in chat_model.stream_chat(messages):
        response += new_text

    return response


# Start the server
if __name__ == '__main__':
    app.run(debug=True)
