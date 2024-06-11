from kivy.lang import Builder
from kivymd.app import MDApp
import random

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"
        self.check = random.randint(1, 10)  # Generate the initial random number
        return Builder.load_file('main.kv')
    
    def submit(self):
        try:
            self.now = int(self.root.ids.num_input.text)
        except ValueError:
            self.root.ids.no.text = "Please enter a valid number"
            return

        no = self.now
        if no == self.check:
            self.root.ids.no.text = f"You guessed it! The number was {no}."
            self.check = random.randint(1, 10)  # Generate new random number for next round
        else:
            self.root.ids.no.text = f"Try again! The number is not {no}."

    def reset(self):
        self.check = random.randint(1, 10)  # Generate new random number
        self.root.ids.num_input.text = ""  # Clear text input
        self.root.ids.no.text = "Guess the Number"  # Reset guess message

MainApp().run()
