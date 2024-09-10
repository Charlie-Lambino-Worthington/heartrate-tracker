import pygame
import time

def test_sounds():
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load sound files
    sound_files = {
        "60-": pygame.mixer.Sound('sound/60-.wav'),
        "100+": pygame.mixer.Sound('sound/100+.wav'),
        "115+": pygame.mixer.Sound('sound/115+.wav'),
        "140+": pygame.mixer.Sound('sound/140+.wav')
    }

    try:
        for label, sound in sound_files.items():
            print(f"Playing {label} sound...")
            sound.play()
            time.sleep(2)  # Wait for the sound to finish playing
            print(f"{label} sound played successfully.")
    except Exception as e:
        print(f"Error playing sound: {e}")

if __name__ == "__main__":
    test_sounds()