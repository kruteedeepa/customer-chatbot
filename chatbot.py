import json
import random
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import json
import random
import pickle

# Load JSON
with open("intents.json") as f:
    data = json.load(f)

# Data preparation
X = []
y = []
responses = {}

for intent in data["intents"]:
    tag = intent["tag"]
    responses[tag] = intent["responses"]
    for pattern in intent["patterns"]:
        X.append(pattern.lower())
        y.append(tag)

# Training the model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
# Chat loop
def chatbot():
    print("Chatbot: Hello! Ask me something. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        pred = model.predict([user_input])[0]
        print("Chatbot:", random.choice(responses[pred]))

if __name__ == "__main__":
    chatbot()
