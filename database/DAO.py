# Importare tutto ciò che sarà necessario successivamente
from database.DB_connect import DBConnect
from model.nerc import Nerc
from model.powerOutages import Event

# Definire la classe DAO
class DAO():

    # Definire il metodo __init__
    def __init__(self):
        pass

    # Definire il metodo statico getAllNerc
    @staticmethod
    def getAllNerc():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT n.*
        FROM nerc n"""
        cursor.execute(query)
        for row in cursor:
            result.append(Nerc(row["id"], row["value"]))
        cursor.close()
        conn.close()
        return result

    # Definire il metodo getAllEvents, che restituisce tutti gli eventi selezionato un determinato nerc
    @staticmethod
    def getAllEvents(nerc):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT p.*
        FROM poweroutages p
        WHERE p.nerc_id = %s"""
        cursor.execute(query, (nerc.id,))
        for row in cursor:
            result.append(
                Event(row["id"], row["event_type_id"],
                      row["tag_id"], row["area_id"],
                      row["nerc_id"], row["responsible_id"],
                      row["customers_affected"], row["date_event_began"],
                      row["date_event_finished"], row["demand_loss"]))
        cursor.close()
        conn.close()
        return result