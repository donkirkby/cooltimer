from datetime import datetime, timedelta
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

__version__ = '0.1.0'

class TimerDisplay(Widget):
    timer = ObjectProperty(None)

    def start(self):
        self.end_time = datetime.now() + timedelta(minutes=2, seconds=1)
        self.tick(0)
        
    def tick(self, dt):
        time_left = self.end_time - datetime.now()
        if time_left.days < 0:
            seconds_left = 0
        else:
            seconds_left = time_left.seconds
        minutes, seconds = divmod(seconds_left, 60)
        self.timer.text = "{}:{:02}".format(minutes, seconds)

class CoolTimerApp(App):
    def build(self):
        display = TimerDisplay()
        display.start()
        
        Clock.schedule_interval(display.tick, 0.01)
        return display
    
if __name__ == '__main__':
    CoolTimerApp().run()