# Importare flet
import flet as ft

# Importare le varie classi che verranno utilizzate in seguito
from model.model import Model
from UI.view import View
from UI.controller import Controller

# Definire il main
def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()

# Introdurre il seguente codice che permette di visualizzare l'interfaccia grafica sullo schermo
ft.app(target = main)