# Importare le classi necessarie per l'esecuzione del programma
from database.DAO import DAO

# Definire la classe Model
class Model:

    # Definire il metodo __init__
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()

    # Definire il metodo worstCase
    def worstCase(self, nerc, maxY, maxH):
        pass

    # Definire il metodo _ricorsione
    def _ricorsione(self, parziale, maxY, maxH, pos):
        pass

    # Definire il metodo loadEvents, che restituisce il risultato del metodo DAO getAllEvents
    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    # Definire il metodo laodNerc, che restituisce il risultato del metodo DAO getAllNerc
    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()

    # Definire la property listNerc
    @property
    def listNerc(self):
        return self._listNerc