import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy import BoxLayout
from kivy import Clock
from fitbit_integration import get_authorization_url, get_access_token, fetch_fitbit_data

class HeartRateApp(App):
    def build(self):
        layout = BoxLayout(orientation'vertical')
        self.heart_rate_label = Label(text='Fetching heart rate data...')
        return Label(text='Welcome to POTS Heartrate Monitor!')

if __name__ == '__main__':
    HeartRateApp().run()