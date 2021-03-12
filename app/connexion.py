"""
endpoints :
    - infos d'un restaurant à partir de son id,
    - liste des noms de restaurants à partir du type de cuisine,
    - nombre d'inspection d'un restaurant à partir de son id restaurant,
    - noms des 10 premiers restaurants d'un grade donné.
"""
from cassandra.cluster import Cluster
import itertools

class DataAccess :

    @classmethod 
    def connexion(cls):
        cls.cluster = Cluster(['cass1', 'cass2'], port=9042)
        cls.db = cls.cluster.connect('resto')
        cls.db.execute('USE resto')

    @classmethod
    def deconnexion(cls):
        cls.cluster.shutdown()

    #infos d'un restaurant à partir de son id,
    @classmethod
    def get_restaurant_by_id(cls, resto_id):
        cls.connexion()
        result = cls.db.execute(f"SELECT * FROM restaurant WHERE id={resto_id};")
        cls.deconnexion()
        return list(result)
        
    #liste des noms de restaurants à partir du type de cuisine,
    @classmethod
    def get_restaurant_by_cuisine_type(cls, resto_type):
        cls.connexion()
        result = cls.db.execute(f"SELECT * FROM restaurant WHERE cuisinetype='{resto_type}';")
        cls.deconnexion()
        return list(result)

    #nombre d'inspections d'un restaurant à partir de son id restaurant,
    @classmethod
    def get_nb_inspections_by_id(cls, resto_id):
        cls.connexion()
        result = len(cls.db.execute(f"SELECT * FROM inspection WHERE idrestaurant={resto_id}").all())
        cls.deconnexion()
        return result

    #noms des 10 premiers restaurants d'un grade donné
    @classmethod
    def get_10_first_by_grade(cls, grade):
        cls.connexion()
        result1 = cls.db.execute(f"SELECT * FROM inspection WHERE grade='{grade}'")
        ids = result1[:10]
        result2 =[]
        for id_ in ids :
            res = cls.db.execute(f"SELECT name FROM restaurants WHERE id={int(id_)};").all()
            result2.append(res)
        cls.deconnexion()
        return result2
    
