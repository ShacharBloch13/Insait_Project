import openai
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('INSAIT_OPENAI_API_KEY')

def get_openai_answer(question):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    body = json.dumps({
        'messages': [
            {'role': 'system',
             'content': 'You are the smartest person in the world, making money by answering questions. When someone asks you a question you must answer to the best of your ability.'
             },
            {'role': 'user',
             'content': f'{question}'
            }
        ],
        'model': 'gpt-3.5-turbo',
        'temperature': 0.5
    })

    try:
        response = requests.post(url, headers=headers, data=body)
        response
        answer = response.json()['choices'][0]['message']['content'].strip()
        return answer
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Looks like your API key is incorrect. Please check your API key and try again.")
        else:
            print(f"Failed to fetch recommendations. Status code: {response.status_code}")
    except Exception as err:
        print(f"An error occurred returning recommendations: {err}")
