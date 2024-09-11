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
        layout.add_widget(self.heart_rate_label)
        # Direct user to Fitbit authorization URL on start
        print("Please go to the following URL and authorize the application:")
        print(get_authorization_url())
        # Use Clock to periodically fetch heart rate data
        Clock.schedule_interval(self.update_heart_rate_data, 60) # Update every 60 seconds
        return layout

if __name__ == '__main__':
    HeartRateApp().run()