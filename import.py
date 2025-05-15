import requests

API_KEY = "CONGRESS_API_KEY"
BASE_URL = "https://api.congress.gov/v3/bill"

def fetch_bills():
    response = requests.get(BASE_URL, params={"api_key": API_KEY})
    data = response.json()
    return data['bills']  # Adjust this based on actual API response
