from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.clearcolor = (.92, .92, .92, 1)

from editor import editor

bu = Builder.load_file("kvlang.kv")


class Program(App):
    title = "Editor"

    def build(self):
        return bu


if __name__ == "__main__":
    Program().run()
