#в первой же строчке что-то :(
'''from.kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation

from kivy.uix.boxlayout import BoxLayout

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)


    def __init__(self, 
                total=10, steptime=1,
                **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.text_inprogress = 'Приседание'
        self.animation = (Animation(pos_hint={'top': 0.1}, duration= steptime/2))+ (Animation(pos_hint= {'top': 1.0},duration= steptime/2 ))
        self.animation.repeat = True
        self.btn = Button(size_hint=(1, 0.1), pos_hint= {'top':1.0}, background=(0.6, 0.38, 0.2, 1))
        self.add_widget(self.btn)

    def start(self):
        self.value = 0
        self.finished = False
        self.btn.text = self.text_inprogress
        self.animation.repeat = True
        self.animation.start(self.btn)


    def next(self, widget, step):
        if step == 1.0:
            self.value +=1
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True'''