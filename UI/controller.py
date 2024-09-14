# Importare tutto ciò che è necessario per lo svolgimento del programma
import flet as ft
from model.nerc import Nerc

# Definire la classe Controller
class Controller:

    # Definire il metodo __init__
    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model
        # Elementi
        self._idMap = {}
        self.fillIDMap()
        self._nerc = None
        self._years = 0
        self._hours = 0

    def handleWorstCase(self, e):
        pass

    # Definire il metodo populate_ddNerc, che inserisce gli elementi all'interno del menù a tendina
    def populate_ddNerc(self):
        nercList = self._model.listNerc
        for element in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(text = element.value,
                                                                 data = element,
                                                                 on_click = self.read_Nerc))
        self._view.update_page()

    # Definire il metodo update_Nerc
    def read_Nerc(self, e):
        self._nerc = e.control.value

    # Definire il metodo update_years
    def read_years(self, e):
        self._years = int(e.control.value)

    # Definire il metodo update_hours
    def read_hours(self, e):
        self._hours = int(e.control.value)

    # Definire il metodo fillIDMap
    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v