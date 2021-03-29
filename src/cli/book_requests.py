import requests
from typing import Dict, List

def get_book(item_number: int) -> Dict:
    """
    Fetches the book corresponding to item number item_number from the front end server.
    """
    try:
        response = requests.get(f"http://localhost:5002/books/{item_number}")
        #r.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception("Frontend server seems to be down. Failed to fetch the book.")
    # Todo: Add comments for exception handling
    if response.status_code != 200:
        raise Exception(str(response.text))
    return response.json()

def get_books_by_topic(topic: str) -> List[Dict]:
    payload = {"topic": topic}
    try:
        response = requests.get(f"http://localhost:5002/books", params=payload)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Frontend server seems to be down. Failed to fetch the books for topic {topic}.")
    # Todo: Add comments for exception handling.
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the requested data.")
    
    return response.json()

def buy_book(item_number: int) -> Dict:
    try:
        response = requests.post(f"http://localhost:5002/books/{item_number}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Frontend server seems to be down. Failed to buy the book with item number {item_number}.")
    # Todo: Add comments for execption handling.
    if response.status_code != 200:
        raise Exception(str(response.text))
    return response.json()


