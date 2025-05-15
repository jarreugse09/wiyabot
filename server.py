from flask import Flask, request, jsonify, render_template
from main import chat_session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Get the chatbot's response
    response = chat_session.send_message(user_input)

    response_text = response.text

    return jsonify({"response": response_text})

# Run the Flask app
if __name__ == "__main__":
    app.run(host = "0.0.0.0")