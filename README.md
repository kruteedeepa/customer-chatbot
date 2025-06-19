🤖 Customer Service Chatbot

A simple NLP-based chatbot designed to answer basic customer service queries like order tracking and general inquiries.

This chatbot is built using **Python**, **Flask**, and **scikit-learn**, and has a clean user interface with typing animation and professional chat layout. It's perfect for internship projects or beginner-level AI implementations.
🧠 Features

- ✅ Responds to common order tracking and service queries
- ✅ Trained using a Naive Bayes classifier and `scikit-learn`
- ✅ Real-time chat interface built with Flask backend
- ✅ Clean and modern UI (pastel green & white theme)
- ✅ Typing animation for bot responses
- ✅ Chat bubbles with profile icons (user and AI)
- ✅ Customer messages aligned to the right professionally
 📁 Folder Structure
customer-chatbot/
│
├── app.py # Flask server to run the bot
├── train.py # Trains the intent model
├── model.pkl # Trained machine learning model
├── intents.json # Predefined questions and responses
│
├── templates/
│ └── index.html # Frontend UI
│
├── static/
│ └── style.css # Styling for the chatbot interface


yaml
Copy
Edit
⚙️ How to Run the Chatbot Locally
 1️⃣ Clone the Repository

```bash
git clone https://github.com/kruteedeepa/customer-chatbot.git
cd customer-chatbot
2️⃣ Install Required Libraries
bash
Copy
Edit
pip install flask scikit-learn
3️⃣ Train the Chatbot Model
bash
Copy
Edit
python train.py
This generates the model.pkl file used by the chatbot.

4️⃣ Start the Flask Server
bash
Copy
Edit
python app.py
Then open your browser and go to:
📍 http://127.0.0.1:5000

🛠️ Tech Stack Used
Python
Flask
scikit-learn
HTML, CSS, JavaScript

📌 Use Case Example Queries
“Where is my order?”

“How long will it take to deliver?”

“What is the delivery location?”

“My order hasn’t arrived”

🙋‍♀️ Author
Kruteedeepa Sahoo
📧 kruteedeepasahoo@gmail.com
🌐 GitHub Profile: https://github.com/kruteedeepa

🚀 This project is built for internship learning purposes and can be extended with multilingual support or order management systems.

Copy
Edit
✅ What To Do Next:
1. Open your GitHub repo.
2. Click **“Add file” > “Create new file”**.
3. Name it `README.md`.
4. Paste the above content.
5. Click **“Commit new file”**.

That’s it! 🎉 It’ll now display beautifully on your GitHub home page.

Would you like me to convert this to a **PDF** for offline submission too?
