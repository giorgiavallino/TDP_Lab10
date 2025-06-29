from database.DB_connect import DBConnect
from model.country import Country
from model.contiguity import Contiguity

class DAO():

    def __init__(self):
        pass

    @staticmethod
    def getAllNodes(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT *
                FROM contiguity c
                where c.`year` <= %s"""
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Contiguity(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT c.state1no AS s1, c.state2no AS s2
                FROM contiguity c 
                WHERE c.`year` <= %s"""
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append((row["s1"], row["s2"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT *
                FROM country c"""
        cursor.execute(query,)
        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result