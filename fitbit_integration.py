import requests
from base64 import b64encode
import config  # Import the configuration settings

# Use constants from config.py
CLIENT_ID = config.FITBIT_CLIENT_ID
CLIENT_SECRET = config.FITBIT_CLIENT_SECRET
REDIRECT_URI = config.REDIRECT_URI
AUTHORIZATION_URL = config.AUTHORIZATION_URL
TOKEN_URL = config.TOKEN_URL
HEART_RATE_URL = config.HEART_RATE_URL

def get_authorization_url():
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': 'heartrate',
        'expires_in': '604800'
    }
    url = requests.Request('GET', AUTHORIZATION_URL, params=params).prepare().url
    return url

def get_access_token(auth_code):
    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI
    }
    headers = {
        'Authorization': f'Basic {b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode()).decode()}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(TOKEN_URL, data=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print(f"Error fetching access token: {response.status_code}")
        return None

def fetch_fitbit_data(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(HEART_RATE_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching Fitbit data: {response.status_code}")
        return None