import requests
from base64 import b64encode

# Fitbit OAuth 2.0 credentials and URLs
CLIENT_ID = '23PKKT'
CLIENT_SECRET = '849d797008283a32fa95d1d26f7b849a'
REDIRECT_URI = 'http://localhost:8080/callback'
AUTHORIZATION_URL = 'https://www.fitbit.com/oauth2/authorize'
TOKEN_URL = 'https://api.fitbit.com/oauth2/token'
HEART_RATE_URL = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json'

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
