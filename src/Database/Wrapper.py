from Database import GraphObject
from Database.Database import Database


class Wrapper:
    db: Database

    def __init__(self):
        self.db = Database()


    def add_graph(self, graph_object: GraphObject):
        conn = Database.get_pool()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO ')