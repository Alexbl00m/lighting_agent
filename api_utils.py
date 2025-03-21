import requests

def fetch_dali_products():
    response = requests.get("https://api.dalialliance.org/products")
    if response.status_code == 200:
        return response.json()
    return None
