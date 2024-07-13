# Insait_Home_Project
check out a short video depicting the project's usage here:
```
https://youtu.be/jNTHBSBkL2k
```

This project is a backend application developed with Flask and PostgreSQL, Dockerized for ease of deployment. It includes functionality to ask questions and get answers using the OpenAI API.

# Features
1. Ask questions and get answers.
2. Persistent storage of questions and answers in a PostgreSQL database.
3. Dockerized application for easy deployment.

# Technologies Used
1. Backend: Flask
2. Database: PostgreSQL
3. Docker: For containerization
4. API: OpenAI API

# Installation
1. clone the repo:
```
git clone https://github.com/yourusername/insaithomeassignment.git
cd insaithomeassignment
```
2. Create a .env file in the root directory with the following content:
```
SQLALCHEMY_DATABASE_URI=postgresql://postgres:Shb316381649@db:5432/mydatabase
OPENAI_API_KEY=your_openai_api_key_here
```

# Usage
1. Build and start the containers using Docker Compose:
```
docker-compose up --build
```
2. Use the  provided Postman collection to use the API

# Project Structure
```
insaithomeassignment/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── instance/
│   └── qa.db
│
├── venv/
│
├── .env
├── .gitignore
├── alembic.ini
├── app.py
├── docker-compose.yml
├── dockerfile
├── init_db.py
├── openai_client.py
├── requirements.txt
├── test_app.py
├── Instait.postman_collection.json
└── README.md
```
# API Endpoints
1. 'POST /ask'
   
   1.1. Ask a question and get an answer.
   
   1.2. Request Body:
   ```
   {
    "question": "Your question here"
    }
   ```
# Commit History

```
* 9967bdf (HEAD -> master, origin/master) added postman collection
* 6fdf2af added docker
* 21ce9ed added alembic for db migration
* dd24a89 working Postgres
| * 90084d2 (postgress) working postgres
|/
* 472058e added pytest
* 0ca5331 basic first step - working Postman test
```

# Contributing

I welcome contributions to this project! Whether you want to add new features, improve existing functionality, or fix bugs, your help is appreciated. Please feel free to fork the repository and submit pull requests.

Thank you for checking out this project. If you have any questions or suggestions, please feel free to open an issue or contact us directly. Happy coding!

