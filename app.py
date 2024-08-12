from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'  # SQLite database file
db = SQLAlchemy(app)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voter_id = db.Column(db.String(50), nullable=False)
    candidate = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/get_candidates', methods=['GET'])
def get_candidates():
    candidates = ["Candidate A", "Candidate B", "Candidate C"]
    return jsonify({"candidates": candidates})

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    data = request.get_json()
    vote = Vote(voter_id=data['voter_id'], candidate=data['candidate'])
    db.session.add(vote)
    db.session.commit()
    return jsonify({"message": "Vote submitted successfully"})

@app.route('/get_chatbot_responses', methods=['GET'])
def get_chatbot_responses():
    chatbot_responses = {
        "guidelines": [
            "Welcome to the Blockchain Voting System!",
            "Follow these guidelines for a smooth voting experience:",
            "1. Enter your voter ID correctly.",
            "2. Select a candidate from the list.",
            "3. Click the 'Submit Vote' button to cast your vote.",
            "Thank you for participating in the voting process!"
        ],
        "another_chatbot": [
            "Hello! I am the second chatbot.",
            "How can I assist you today?",
            "Feel free to ask me anything!",
            "I'm here to help you with information and answers."
        ]
    }
    return jsonify({"chatbot_responses": chatbot_responses})

@app.route('/send_user_message', methods=['POST'])
def send_user_message():
    data = request.get_json()
    user_input = data.get('user_input', '')
    
    chatbot_response = generate_chatbot_response(user_input)
    
    return jsonify({"chatbot_response": chatbot_response})

def generate_chatbot_response(user_input):
    responses = [
        "I'm sorry, I didn't understand that.",
        "Could you please provide more details?",
        "That's interesting! Tell me more.",
        "I'm here to assist you. Ask me anything."
    ]
    return random.choice(responses)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
