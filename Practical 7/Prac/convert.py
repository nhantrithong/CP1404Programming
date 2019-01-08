from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertNumber(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Convert m to km"
        self.root = Builder.load_file('convert.kv')
        return self.root

    def handle_convert(self):
        no_error = False
        while no_error == False:
            try:
                result = int(self.root.ids.input_number.text ) * 1.609344
                self.root.ids.output_label.text = str(result)
                no_error = True
            except ValueError:
                result = 0
                self.root.ids.input_number.text = str(result)

    def handle_plus(self):
        no_error = False
        while no_error == False:
            try:
                plus = int(self.root.ids.input_number.text) + 1
                self.root.ids.input_number.text = str(plus)
                no_error = True
            except ValueError:
                plus = 0
                self.root.ids.input_number.text = str(plus)

    def handle_minus(self):
        no_error = False
        while no_error == False:
            try:
                minus = int(self.root.ids.input_number.text )- 1
                self.root.ids.input_number.text = str(minus)
                no_error = True
            except ValueError:
                minus = 0
                self.root.ids.input_number.text = str(minus)

ConvertNumber().run()
