# config.py
FITBIT_CLIENT_ID = "23PKKT"
FITBIT_CLIENT_SECRET = "849d797008283a32fa95d1d26f7b849a"
REDIRECT_URI = "https://github.com/Charlie-Lambino-Worthington/heartrate-tracker"  # e.g., "https://your-redirect-uri.com"
AUTHORIZATION_URL = 'https://www.fitbit.com/oauth2/authorize'
TOKEN_URL = 'https://api.fitbit.com/oauth2/token'
HEART_RATE_URL = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json'