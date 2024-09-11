import kivy
from kivy.app import App
from kivy.uix.label import Label

class HeartRateApp(App):
    def build(self):
        return Label(text='Welcome to POTS Heartrate Monitor!')

if __name__ == '__main__':
    HeartRateApp().run()