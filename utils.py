import time
import requests
from functools import wraps


def retry_request(retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    attempt += 1
                    time.sleep(delay)
            return None  # Or raise an error as needed
        return wrapper
    return decorator


@retry_request(retries=5, delay=3)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Example usage:
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    data = fetch_data(url)
    print(data)