from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image  import AsyncImage

class RootWidget(RelativeLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        root = RelativeLayout()
        self.add_widget(Label(text='User Name'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)
        self.add_widget(AsyncImage(source='images/clo.jpg'))


    def btn_pressed(self, instance, pos):
        print ('pos: printed from root widget: {pos}'.format(pos=pos))

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # if the touch collides with our widget, let's grab it
            touch.grab(self)

            # and accept the touch.
            return True


class TestApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()
