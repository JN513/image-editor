from kivy.app import App
from kivy.lang.builder import Builder

bu = Builder.load_file('kvlang.kv')

class Program(App):
    def build(self):
        return bu

if __name__ == "__main__":
    Program().run()