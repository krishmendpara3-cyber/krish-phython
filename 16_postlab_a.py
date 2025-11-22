

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):

    def build(self):
        self.counter = 0

        main_layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        self.counter_label = Label(
            text=str(self.counter),
            font_size=100,
            size_hint=(1, 0.7)
        )

        increment_button = Button(
            text="Increment Counter",
            font_size=40,
            size_hint=(1, 0.3)
        )

        increment_button.bind(on_press=self.increment_counter)

        main_layout.add_widget(self.counter_label)
        main_layout.add_widget(increment_button)

        return main_layout

    def increment_counter(self, instance):
        self.counter += 1
        self.counter_label.text = str(self.counter)

if __name__ == '__main__':
    CounterApp().run()
    
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):

    def build(self):
        self.counter = 0

        main_layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        self.counter_label = Label(
            text=str(self.counter),
            font_size=100,
            size_hint=(1, 0.7)
        )

        increment_button = Button(
            text="Increment Counter",
            font_size=40,
            size_hint=(1, 0.3)
        )

        increment_button.bind(on_press=self.increment_counter)

        main_layout.add_widget(self.counter_label)
        main_layout.add_widget(increment_button)

        return main_layout

    def increment_counter(self, instance):
        self.counter += 1
        self.counter_label.text = str(self.counter)

if __name__ == '__main__':
    CounterApp().run()
    