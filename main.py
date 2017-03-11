#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty, NumericProperty
from plant import Plant
from random import random
import time
from kivy.clock import Clock

class Garden(App):
    def build(self):
        # display a button with the text : Hello QPython 
        #return btn1
        #  return Button(text='Hello QPython')
        layout = GridLayout(rows=2)
        flayout = GridLayout(cols=3, row_force_default=False, size_hint_y =0.8)
        global buttons 
        buttons = []
        for x in range(1,13):
            btn = Plant(text='Plot %s' % x, background_color=[0,1,0,1])
            btn.bind(on_press=callback)
            flayout.add_widget(btn, )
            buttons.append(btn)
        layout.add_widget(flayout)
        s_button = Button(text="sow", border = [16,16,16,16])
        s_button.bind(on_press=sow)
        w_button = Button(text="water")
        w_button.bind(on_press=water)
        clayout = GridLayout(cols=3,size_hint_y=0.2)
        clayout.add_widget(s_button)
        clayout.add_widget(w_button)
 
        layout.add_widget(clayout)
        Clock.schedule_interval(self.mytime, 1.0/1.0)
        return layout

    def mytime(self, dt):
        print dt
        pass



def callback(instance):
    #print('The button <%s> is being pressed' % instance.text)
    instance.text = instance.name
    instance.select()
    #instance.background_color = [0,0,1,0]
        
    
def sow(instance):
    global buttons
    for p in buttons:
        if p.selected:
            p.sow()
            p.text = "sown"
            p.unselect()

def water(instance):
    global buttons
    for p in buttons:
        if p.selected:
            if random() > 0.2 and p.planted:
                p.text = "watered"
            p.unselect()

#btn1 = Button(text='Hello world 1')
#btn1.bind(on_press=callback)
#btn2 = Button(text='Hello world 2')
#btn2.bind(on_press=callback)

Garden().run()
