from kivy.app import App
from kivy.lang.builder import Builder
from editor import editor

bu = Builder.load_file("kvlang.kv")


class Program(App):
    title = "Editor"

    def build(self):
        return bu


if __name__ == "__main__":
    Program().run()
