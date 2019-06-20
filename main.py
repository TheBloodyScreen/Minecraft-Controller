# This file is © TheBloodyscreen
# It was created as part of the Minecraft-Controller project in Jun of 2019
# If you want to use all or part of the code in this file,
# please contact JayDee@TheBloodyScreen.com

import kivy
from rcon import Rcon
from kivy.app import App
from config import config
from kivy.uix.label import Label
from bloodyterminal import btext
from kivy.uix.button import Button
from mc_status import playersOnline
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class Interface(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Button(text="say: "))

        self.message = TextInput(multiline=False)
        self.add_widget(self.message)


class MinecraftController(App):
    def build(self):
        return Interface()


if __name__ == '__main__':
    MinecraftController().run()

