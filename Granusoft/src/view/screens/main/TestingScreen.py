"""
Testing Menu
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Sensor import Sensor

from view.BaseScreen import BaseScreen
from view.StaticList import StaticList
import configurator as config
from view.elements import *
import datetime

Builder.load_file('view/screens/main/TestingScreen.kv')

ONE_SEC = 1

class TestingScreen(BaseScreen):
    height_num = StringProperty("N/A")
    plot = StringProperty("N/A")
    operator = StringProperty("N/A")
    time = StringProperty("N/A")
    current_date = StringProperty("N/A")
    date_time = StringProperty("N/A")
    folder = StringProperty("N/A")
    datasets = []

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        list of notes. Show the default buttons."""
        self.event = Clock.schedule_interval(self.update_time, ONE_SEC)
        self.height_num = self.get_height()
        config.set('height', float(self.height_num))
        self.plot = str(config.get('plot_num',0))
        self.operator = str(config.get('operator','N/A'))
        self.folder = str(config.get('folder','N/A'))
        self.time = datetime.datetime.now().strftime("%I:%M %p")
        self.current_date = datetime.date.today().strftime("%d/%m/%Y")
        # Get notes from config file
        notes = config.get('notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        # Set the data
        self.ids['pretest'].list_data = notes["pretest"]
        self.ids['posttest'].list_data = notes["posttest"]

    def update_time(self, obj):
        self.time = datetime.datetime.now().strftime("%I:%M %p")
        self.date_time = self.current_date+": "+self.time

    def on_leave(self):
        self.event.cancel()

    def get_height(self):
        if str(config.get('height_sensor',0)) == 'ON':
            return self.get_load_cell_sensor_height()
        else:
            return str(config.get('height',0))

    def get_load_cell_sensor_height(self):
        sensor = Sensor()
        if sensor.REAL_DATA is False:
            adc_out = 1
        else:
            adc_out = 0
        sensor.get_header_data()
        sensor_data = sensor.get_sensor_data(adc_out)
        return str("%.2f" % sensor_data["Load Cell Height"])
        


