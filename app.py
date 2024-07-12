from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


app = Flask(__name__)
database_uri = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:Shb316381649@db:5432/mydatabase') ## changed from localhost to db
#pp.config['SQLALCHEMY_DATABASE_URI'] = database_uri ## for debbuging
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Shb316381649@db:5432/mydatabase' ## changed from localhost to db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class QA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Question is required'}), 400

    from openai_client import get_openai_answer
    answer = get_openai_answer(question)

    qa = QA(question=question, answer=answer)
    print(f"debugging: {qa}")
    print(f"Inserting QA: {qa.id}, {qa.question}, {qa.answer}")  # Log the inserted data
    db.session.add(qa)
    db.session.commit()

    print(f"Inserted QA: {qa.id}, {qa.question}, {qa.answer}")  # Log the inserted data

    return jsonify({ 'answer': answer})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
