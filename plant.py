#""" Plant classes for my garden """

from kivy.uix.button import Button
from kivy.properties import ListProperty, NumericProperty
import time

class Plant(Button):
    background_color = ListProperty([0,0,0,0])
    planted = NumericProperty(0)
    def __init__(self, **kwargs):
        
        super(Plant, self).__init__(**kwargs)
        self.name = "tomato"
        self.age = 0
        self.selected = 0
        self.planted = 0
        #self.bind(background_color, redraw)
        	
    
    def sow(self):
        if not self.planted:
            self.planted = 1
        elif self.planted:
            tmp = self.text
            self.text = "already sown"
            # time.sleep(1)
            self.text = tmp
            return "already sown"
    
    def select(self):
        if not self.selected:
            self.selected = 1
            self.background_color = [0,0,1,1]
        else:
            self.selected = 0
            self.background_color = [0,1,0,1]
   

    def unselect(self):
        self.selected = 0
        self.background_color = [0,1,0,1]
        #self.border = None
