import pytest
from app import app, db, QA
from openai_client import get_openai_answer

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_ask__endpoint(client, monkeypatch):

    response = client.post('/ask', json={'question': 'What is the airport code of Paris?'})
    
    assert response.status_code == 200
    data = response.get_json()
    assert 'answer' in data
    assert "CDG" in data['answer']

def test_openai_api():
    question = 'What is the airport code of Paris?'
    answer = get_openai_answer(question)
    
    assert "CDG" in answer