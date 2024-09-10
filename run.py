import numpy as np
import heartpy as hp
import time
from playsound import playsound

#defines thresholds
LOWER_THRESHOLD = 60  # Below this is considered too low
NORMAL_LOWER = 60     # Start of the normal range
NORMAL_UPPER = 100    # End of the normal range
MINOR_CONCERN_UPPER = 115  # Upper bound of minor concern range
MID_CONCERN_UPPER = 135    # Upper bound of mid concern range

# generates fake heartrate for testing purposes

def generate_mock_heart_rate_data(num_samples=1000):
    return np.random.randint(60, 150, size=num_samples)  # Simulated heart rate values

def check_heart_rate(heart_rate):
    if heart_rate < LOWER_THRESHOLD
        print(f"Alert: Heart rate is too low! ({heart_rate} bpm)")
