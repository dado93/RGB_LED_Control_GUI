from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty  # pylint: disable=E0611
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from serialport import Board


class BottomLabel(BoxLayout):
    bottom_label = ObjectProperty(None)

    def update(self, text):
        self.bottom_label.text = text


class ColorSlider(BoxLayout):
    color_label = ObjectProperty(None)
    value_slider = ObjectProperty(None)
    value_label = ObjectProperty(None)

    def update_color_label(self, text):
        self.color_label.text = text

    def on_value_slider(self, instance, value):
        self.value_slider.bind(value=self.update_value_label)

    def update_value_label(self, instance, value):
        self.value_label.text = str(value)

    def update_label_color(self, color):
        self.color_label.color = color
        self.value_label.color = color

    def get_current_value(self):
        return self.value_slider.value


class Container(BoxLayout):
    bottom_label = ObjectProperty(None)
    red_slider = ObjectProperty(None)
    green_slider = ObjectProperty(None)
    blue_slider = ObjectProperty(None)
    send_button = ObjectProperty(None)
    data_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.board = Board()
        self.board.add_callback(self.on_connect)

    def on_bottom_label(self, instance, value):
        self.bottom_label.update(
            "RGB Led Control application. Scanning serial ports..")

    def on_red_slider(self, instance, value):
        self.red_slider.update_color_label("Red")

    def on_green_slider(self, instance, value):
        self.green_slider.update_color_label("Green")

    def on_blue_slider(self, instance, value):
        self.blue_slider.update_color_label("Blue")

    def on_send_button(self, instance, value):
        self.send_button.bind(on_release=self.send_button_clicked)

    def send_button_clicked(self, dt):
        if (self.board.is_connected):

            self.board.ser.write(bytearray([0xA0, 0x10, 0x00, 0xFF, 0xC0]))
            #print(bytearray([int(self.data_input.text, 16)]))
            #self.board.ser.write(bytearray([int(self.data_input.text, 16)]))

    def update_background(self, dt):
        self.canvas.before.clear()
        r = self.red_slider.get_current_value()
        g = self.green_slider.get_current_value()
        b = self.blue_slider.get_current_value()
        r_norm = r/255
        g_norm = g/255
        b_norm = b/255
        self.red_slider.update_label_color((1-r_norm, 1-g_norm, 1-b_norm, 1.0))
        self.green_slider.update_label_color(
            (1-r_norm, 1-g_norm, 1-b_norm, 1.0))
        self.blue_slider.update_label_color(
            (1-r_norm, 1-g_norm, 1-b_norm, 1.0))
        with self.canvas.before:
            Color(r_norm, g_norm, b_norm, 0.8)
            Rectangle(pos=self.pos, size=self.size)
        self.board.write_new_color(r, g, b)

    def on_connect(self):
        self.red_slider.disabled = False
        self.green_slider.disabled = False
        self.blue_slider.disabled = False
        Clock.schedule_interval(self.update_background, .1)
        #self.board.write_new_color(100, 100, 0)


class RGBLedApp(App):
    '''
    This is the main app class that returns the
    root widget, which is Container.
    '''

    def build(self):
        return Container()


# If we're calling main, start the Kivy App
if __name__ == "__main__":
    RGBLedApp().run()
