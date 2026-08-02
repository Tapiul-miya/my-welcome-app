from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class WelcomeBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 20

        self.welcome_label = Label(
            text="Welcome to My Welcome App",
            font_size="28sp",
            halign="center",
            valign="middle",
        )
        self.name_input = TextInput(hint_text="Enter your name", multiline=False)
        self.greet_button = Button(text="Say Hello")
        self.greet_button.bind(on_press=self.say_hello)
        self.result_label = Label(text="", halign="center", font_size="20sp")

        self.add_widget(self.welcome_label)
        self.add_widget(self.name_input)
        self.add_widget(self.greet_button)
        self.add_widget(self.result_label)

    def say_hello(self, instance):
        name = self.name_input.text.strip() or "friend"
        self.result_label.text = f"Hello, {name}!"


class WelcomeApp(App):
    def build(self):
        return WelcomeBox()


if __name__ == "__main__":
    WelcomeApp().run()
