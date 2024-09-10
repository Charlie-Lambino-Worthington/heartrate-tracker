#import numpy as np
import requests
import heartpy as hp
import time
from playsound import playsound
import os
from base64 import b64encode

#defines thresholds
LOWER_THRESHOLD = 60  # Below this is considered too low
NORMAL_LOWER = 60     # Start of the normal range
NORMAL_UPPER = 100    # End of the normal range
MINOR_CONCERN_UPPER = 115  # Upper bound of minor concern range
MID_CONCERN_UPPER = 140    # Upper bound of mid concern range

# generates fake heartrate for testing purposes

#def generate_mock_heart_rate_data(num_samples=1000):
 #   return np.random.randint(60, 150, size=num_samples)  # Simulated heart rate values

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


def check_heart_rate(heart_rate):
    if heart_rate < LOWER_THRESHOLD:
      #  playsound('sound/60-.wav')
        print(f"Alert: Heart rate is too low! ({heart_rate} bpm)")
    elif heart_rate > NORMAL_UPPER and heart_rate < MINOR_CONCERN_UPPER:
      #  playsound('sound/100+.wav')
        print(f"Alert: Heart rate is a little high, get some rest! ({heart_rate} bpm)")    
    elif heart_rate > MINOR_CONCERN_UPPER and heart_rate < MID_CONCERN_UPPER:
       # playsound('sound/115+.wav')
        print(f"Alert: Heart rate is a quite high, take your meds and get some rest! ({heart_rate} bpm)")    
    elif heart_rate > MID_CONCERN_UPPER:
       # playsound('sound/140+.wav')
        print(f"Alert: Heart rate is a really very high, are you doing intense exercise? there may be a problem, take your meds and get some rest! ({heart_rate} bpm)")   

def real_time_monitoring():
    """Continuously monitor and check heart rate data."""
    while True:
        heart_rate_data = generate_mock_heart_rate_data(num_samples=1)
        current_heart_rate = heart_rate_data[0]
        check_heart_rate(current_heart_rate)
        time.sleep(5)  # Adjust the sleep time for your testing

def main():
    # Step 1: Direct user to Fitbit authorization URL
    print("Please go to the following URL and authorize the application:")
    print(get_authorization_url())
    
    # Step 2: After authorization, obtain the authorization code
    auth_code = input("Enter the authorization code: ")
    
    # Step 3: Get access token using the authorization code
    access_token = get_access_token(auth_code)
    
    if access_token:
        print("Access token obtained.")
        
        # Continuous data collection loop
        while True:
            fitbit_data = fetch_fitbit_data(access_token)
            if fitbit_data:
                # Extract heart rate data (example structure; adjust as needed)
                try:
                    heart_rate_values = fitbit_data['activities-heart'][0]['value']['heartRateZones']
                    # Assume you want the current heart rate from the 'outOfRange' zone for simplicity
                    current_heart_rate = heart_rate_values[-1]['min']  # Adjust to get actual heart rate data
                    check_heart_rate(current_heart_rate)
                except (KeyError, IndexError):
                    print("Error extracting heart rate data.")
            
            # Wait before fetching new data
            time.sleep(60)  # Adjust the interval as needed (e.g., 60 seconds)

if __name__ == "__main__":
    main()