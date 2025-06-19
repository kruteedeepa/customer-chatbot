from flask import Flask, render_template, request, jsonify
import json
import pickle
import random

app = Flask(__name__)

# Load model and intents
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Map tags to responses
responses = {intent["tag"]: intent["responses"] for intent in data["intents"]}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"response": "Sorry, I didn’t get that."})

    # Predict intent tag
    tag = model.predict([user_input])[0]

    if tag in responses:
        bot_reply = random.choice(responses[tag])
    else:
        bot_reply = "Sorry, I’m not sure how to help with that."

    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
