import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from playsound import playsound
from fitbit_integration import get_authorization_url, get_access_token, fetch_fitbit_data

class HeartRateApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Label to display heart rate data or messages
        self.heart_rate_label = Label(text='Fetching heart rate data...')
        layout.add_widget(self.heart_rate_label)

        # TextInput for user to enter the authorization code
        self.auth_code_input = TextInput(hint_text='Enter the authorization code', multiline=False)
        layout.add_widget(self.auth_code_input)

        # Button to start monitoring heart rate
        self.start_button = Button(text='Start Monitoring')
        self.start_button.bind(on_press=self.start_monitoring)
        layout.add_widget(self.start_button)

        # Direct user to Fitbit authorization URL on start
        print("Please go to the following URL and authorize the application:")
        print(get_authorization_url())
        # Use Clock to periodically fetch heart rate data
        Clock.schedule_interval(self.update_heart_rate_data, 60) # Update every 60 seconds
        return layout

    def update_heart_rate_data(self, *args):
         auth_code = input("Enter the authorization code: ")  # Replace this with a better method for getting the auth code
        access_token = get_access_token(auth_code)
        if access_token:
            fitbit_data = fetch_fitbit_data(access_token)
            if fitbit_data:
                try:
                    heart_rate_values = fitbit_data['activities-heart'][0]['value']['heartRateZones']
                    current_heart_rate = heart_rate_values[-1]['min']  # Adjust as needed
                    message = self.check_heart_rate(current_heart_rate)
                    self.heart_rate_label.text = message
                except (KeyError, IndexError):
                    self.heart_rate_label.text = "Error extracting heart rate data."
        else:
            self.heart_rate_label.text = "Error obtaining access token."

    #defines thresholds
    LOWER_THRESHOLD = 60  # Below this is considered too low
    NORMAL_LOWER = 60     # Start of the normal range
    NORMAL_UPPER = 100    # End of the normal range
    MINOR_CONCERN_UPPER = 115  # Upper bound of minor concern range
    MID_CONCERN_UPPER = 140    # Upper bound of mid concern range

    #checks heratrate agaist thresholds and alerts by printing warning and playing sound
    def check_heart_rate(self, heart_rate):
        if heart_rate < self.LOWER_THRESHOLD:
            playsound('sound/60-.wav')
            return f"Alert: Heart rate is too low! ({heart_rate} bpm)"
        elif heart_rate > self.NORMAL_UPPER and heart_rate < self.MINOR_CONCERN_UPPER:
            playsound('sound/100+.wav')
            return f"Alert: Heart rate is a little high, get some rest! ({heart_rate} bpm)"    
        elif heart_rate > self.MINOR_CONCERN_UPPER and heart_rate < self.MID_CONCERN_UPPER:
            playsound('sound/115+.wav')
            return f"Alert: Heart rate is quite high, take your meds and get some rest! ({heart_rate} bpm)"    
        elif heart_rate > self.MID_CONCERN_UPPER:
            playsound('sound/140+.wav')
            return f"Alert: Heart rate is very high, there may be a problem! ({heart_rate} bpm)"  

if __name__ == '__main__':
    HeartRateApp().run()