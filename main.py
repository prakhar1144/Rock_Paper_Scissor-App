import kivy
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from random import randint
import time
n, y, b, g = 9, 0, 0, 1


class Class1(BoxLayout):
    pra = ObjectProperty(None)
    abh = ObjectProperty(None)
    yes = ObjectProperty(None)
    swa = ObjectProperty(None)
    ayu = ObjectProperty(None)

    def logic(self, response):
        global n, y, b
        n -= 1
        self.pra.text = str(n)
        l = ['Rock', 'Paper', 'Scissor']
        bot = l[randint(0, 2)]
        self.swa.text = str(bot)
        if bot == response:
            self.ayu.text = str(response)
            self.abh.text = str(y)
            self.yes.text = str(b)

        elif response == 'Rock':
            self.ayu.text = str(response)
            if bot == 'Paper':
                self.yes.text = str(b + 1)
                self.abh.text = str(y)
                b += 1
            else:
                self.yes.text = str(b)
                self.abh.text = str(y + 1)
                y += 1
        elif response == 'Paper':
            self.ayu.text = str(response)
            if bot == 'Rock':
                self.yes.text = str(b)
                self.abh.text = str(y + 1)
                y += 1
            else:
                self.yes.text = str(b + 1)
                self.abh.text = str(y)
                b += 1
        else:
            self.ayu.text = str(response)
            if bot == 'Paper':
                self.yes.text = str(b)
                self.abh.text = str(y + 1)
                y += 1
            else:
                self.yes.text = str(b + 1)
                self.abh.text = str(y)
                b += 1
        if n == 1:
            global g
            g = 1
            show_popup()


    def btn1(self):
        return self.logic('Rock')

    def btn2(self):
        return self.logic('Paper')

    def btn3(self):
        return self.logic('Scissor')


class P(BoxLayout):
    btn = ObjectProperty(None)
    def user(self):
        return str(y)

    def cmptr(self):
        return str(b)

    def again(self):
        global g
        g = 0
        print("done")
        n, y, b = 9, 0, 0
        show_popup()


def show_popup():
    if g == 1:
        show = P()
        popupwindow = Popup(title="Score Board", title_align='center', auto_dismiss=False, content=show,size_hint=(0.95, 0.95))
        popupwindow.open()
    if g == 0:
        print("here")
        sys.exit()


class RoPaScApp(App):
    def build(self):
        return Class1()


if __name__ == "__main__":
    RoPaScApp().run()