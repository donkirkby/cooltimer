from datetime import datetime, timedelta
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

class TimerDisplay(Widget):
    timer = ObjectProperty(None)

    def start(self):
        self.end_time = datetime.now() + timedelta(seconds=20)
        self.tick(0)
        
    def tick(self, dt):
        time_left = self.end_time - datetime.now()
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