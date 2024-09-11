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

        # Print Fitbit authorization URL
        print("Please go to the following URL and authorize the application:")
        print(get_authorization_url())

        return layout

    def start_monitoring(self, instance):
        auth_code = self.auth_code_input.text
        if not auth_code:
            self.heart_rate_label.text = "Please enter the authorization code."
            return

        access_token = get_access_token(auth_code)
        if access_token:
            # Use Clock to periodically fetch heart rate data
            Clock.schedule_interval(lambda dt: self.update_heart_rate_data(access_token), 60)
            self.heart_rate_label.text = "Monitoring started..."
        else:
            self.heart_rate_label.text = "Error obtaining access token."

    def update_heart_rate_data(self, access_token):
        print("Updating heart rate data...")
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
            self.heart_rate_label.text = "Error fetching Fitbit data."

    # Defines thresholds
    LOWER_THRESHOLD = 60
    NORMAL_UPPER = 100
    MINOR_CONCERN_UPPER = 115
    MID_CONCERN_UPPER = 140

    # Checks heart rate against thresholds and alerts
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

     def handle_alert(self, message):
        if message:
            # Schedule the next check after 5 minutes
            Clock.schedule_once(lambda dt: self.update_heart_rate_data(), 300)  # 300 seconds = 5 minutes
        else:
            # If no alert, check immediately
            self.update_heart_rate_data()
     # Checks heart rate after waiting period and provides post-alert messages
    def check_post_alert_heart_rate(self, heart_rate):
        if heart_rate > self.LOWER_THRESHOLD and heart_rate < self.NORMAL_UPPER:
            playsound('sound/stilllow.wav')
            return f"Post-Alert: Heart rate is back to normal! ({heart_rate} bpm)."
        elif heart_rate < self.LOWER_THRESHOLD: 
             playsound('sound/stillhigh.wav')
             return f"Post-Alert: Heart rate is still too low! ({heart_rate} bpm). Please get some rest."
        elif heart_rate > self.NORMAL_UPPER:
             playsound('sound/normal.wav')
             return f"Post-Alert: Heart rate is still too high! ({heart_rate} bpm). Please get some rest."


if __name__ == '__main__':
    HeartRateApp().run()