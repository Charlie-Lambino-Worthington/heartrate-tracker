import numpy as np
import heartpy as hp
import time
from playsound import playsound

#defines thresholds
LOWER_THRESHOLD = 60  # Below this is considered too low
NORMAL_LOWER = 60     # Start of the normal range
NORMAL_UPPER = 100    # End of the normal range
MINOR_CONCERN_UPPER = 115  # Upper bound of minor concern range
MID_CONCERN_UPPER = 140    # Upper bound of mid concern range

# generates fake heartrate for testing purposes

def generate_mock_heart_rate_data(num_samples=1000):
    return np.random.randint(60, 150, size=num_samples)  # Simulated heart rate values

def check_heart_rate(heart_rate):
    if heart_rate < LOWER_THRESHOLD:
        playsound('sound/60-.wav')
        print(f"Alert: Heart rate is too low! ({heart_rate} bpm)")
    elif heart_rate > NORMAL_UPPER and heart_rate < MINOR_CONCERN_UPPER:
        playsound('sound/100+.wav')
        print(f"Alert: Heart rate is a little high, get some rest! ({heart_rate} bpm)")    
    elif heart_rate > MINOR_CONCERN_UPPER and heart_rate < MID_CONCERN_UPPER:
        playsound('sound/115+.wav')
        print(f"Alert: Heart rate is a quite high, take your meds and get some rest! ({heart_rate} bpm)")    
    elif heart_rate > MID_CONCERN_UPPER:
        playsound('sound/140+.wav')
        print(f"Alert: Heart rate is a really very high, are you doing intense exercise? there may be a problem, take your meds and get some rest! ({heart_rate} bpm)")   
