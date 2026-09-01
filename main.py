from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex('#0a0a0a')

class ShailendraCalculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = 15
        self.spacing = 10

        self.display = TextInput(
            text='0',
            font_size=42,
            halign='right',
            multiline=False,
            readonly=True,
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(0.2, 1.0, 0.4, 1)
        )
        self.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=10, size_hint_y=4)

        # Yaha se error fix hai - pehle '.' ka quote close nahi tha
        buttons = [
            'C', '%', '/', '*',
            '7', '8', '9', '-',
            '4', '5', '6', '+',
            '1', '2', '3', '=',
            '0', '.', '', ''
        ]

        for label in buttons:
            if label == '':
                # Khali button skip
                grid.add_widget(Button(text='', disabled=True, background_color=(0,0,0,0)))
                continue
            
            btn = Button(
                text=label,
                font_size=32,
                bold=True,
                background_normal='',
                background_color=get_color_from_hex('#1f1f1f') if label not in ['=', 'C'] else get_color_from_hex('#00C853' if label == '=' else '#D50000')
            )
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)

        self.add_widget(grid)

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text

        if text == 'C':
            self.display.text = '0'
        elif text == '=':
            try:
                # % ko /100 me badlo
                result = str(eval(current.replace('%', '/100')))
                self.display.text = result
            except Exception:
                self.display.text = 'Error'
        else:
            if current == '0' or current == 'Error':
                self.display.text = text
            else:
                self.display.text = current + text

class CalculatorApp(App):
    def build(self):
        self.title = "Shailendra Calculator v2.0"
        return ShailendraCalculator()

if __name__ == '__main__':
    CalculatorApp().run()
