# Implementare le funzioni che verranno utilizzate in seguito
import flet as ft
import os

# Definire la classe View
class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # Page stuff
        self._txtOut = None
        self._page = page
        self._page.title = "TdP 2024 - Insurance Unit"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        page.window_width = 1000  # window's width is 200 px
        page.window_height = 1000
        page.window_center()
        # Controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # Graphical elements
        self._title = None
        self._ddNerc = None
        self._txtYears = None
        self._txtHours = None
        self._btnWorstCase = None
        self._logo = None

    # Definire il metodo load_interface, che carica l'interfaccia grafica
    def load_interface(self):

        # Title
        self._title = ft.Text("TdP 2024 - Insurance Unit", color = "blue", size = 24)
        self._page.controls.append(self._title)

        # Row 1
        img_path = os.path.join(os.getcwd(), 'UI/NERC-map.png')
        self._logo = ft.Image(src = img_path,
                              width = 500,
                              height = 500,
                              )
        self._ddNerc = ft.Dropdown(label = "NERC",
                                   hint_text = "Selezionare il NERC",
                                   on_change = self._controller.read_Nerc)
        self._controller.populate_ddNerc()
        self._txtYears = ft.TextField(label = "Numero massimo di anni",
                                      hint_text = "Inserire il numero massimo di anni",
                                      on_change = self._controller.read_years)
        self._txtHours = ft.TextField(label = "Numero massimo di ore",
                                      hint_text = "Inserire il numero massimo di ore",
                                      on_change = self._controller.read_hours)
        self._btnWorstCase = ft.ElevatedButton(text = "Worst-Case analysis",
                                               tooltip = "Calcola il peggior caso possibile",
                                               on_click = self._controller.handleWorstCase)

        row_01 = ft.Row([ft.Column([self._logo]),
            ft.Column([self._ddNerc, self._txtYears, self._txtHours, self._btnWorstCase], spacing=60)],
            alignment = ft.MainAxisAlignment.CENTER,
            spacing = 30)

        # Aggiungere la riga alla pagina
        self._page.add(row_01)

        # List view
        self._lv = ft.ListView(expand = 1, spacing = 10, padding = 20, auto_scroll = False)

        # Aggiungere alla pagina la list view
        self._page.add(self._txtOut)

        # Update della pagina
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()