from kivy.uix.label import Label
from unicodedata import name
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.properties import BooleanProperty
from kivy.uix.switch import Switch
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup


class ItemBoxLayout(BoxLayout):
    pass

class MainScreenTop(BoxLayout):
    sm = ScreenManager()
    def on_goback_press(self):
        self.sm.current = "loginscreen"


class LoginScreen(Screen):
    pass
    

class MainScreen(Screen):
    pass

class Items(BoxLayout):
    pass

class Tracking(BoxLayout):
    i = 0
    Confirmado = BooleanProperty(False)
    Enviado = BooleanProperty(False)
    Enviado2 = BooleanProperty(False)
    Entregado = BooleanProperty(False)
    def on_button_click(self):
        if self.i == 0:
            print("El pedido ha sido confirmado")
            self.i = self.i + 1
            self.Confirmado = True
            popup = Popup(title="¿Está seguro de que el pedido ha sido confirmado?", content = Label(text = "Texto explanatorio"),
            size_hint=(.5,.5))
            popup.open()
        elif self.i == 1:
            print("El pedido ha sido enviado")
            self.i = self.i + 1
            self.Enviado = True
            popup = Popup(title="¿Está seguro de que el pedido ha sido enviado?", content = Label(text = "Texto explanatorio"),
            size_hint=(.5,.5))
            popup.open()
        elif self.i == 2:
            print("El pedido ha sido enviado al almacén")
            self.i = self.i + 1
            self.Enviado2 = True
            popup = Popup(title="¿Está seguro de que el pedido ha sido enviado al almacén?", content = Label(text = "Texto explanatorio"),
            size_hint=(.5,.5))
            popup.open()
        elif self.i == 3:
            print("El pedido ha sido entregado")
            self.i = self.i + 1
            self.Entregado = True
            popup = Popup(title="¿Está seguro de que el pedido ha sido entregado?", content = Label(text = "Texto explanatorio"),
            size_hint=(.5,.5))
            popup.open()
        else:
            print("Ha ocurrido un error, por favor espere")
            self.i = self.i + 1
            


class SelectedItems(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for _ in range(10):
            itembox = ItemBox()
            self.add_widget(itembox)

class ItemBox(BoxLayout):
    pass


class Items(BoxLayout):
    pass


class MainInterface(BoxLayout):
    pass

class SupplierApp(App):
    pass

SupplierApp().run()