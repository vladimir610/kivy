from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.core.clipboard import clipboard_gtk3


class Primer(Widget):
    text = clipboard_gtk3.clipboard()
    print(text)
    pass


class mainApp(App):
    def build(self):
        return Primer()

if __name__ == '__main__':
    mainApp().run()

git config --global user.name vladimir610
git config --global user.email vladimir610@mail.ru