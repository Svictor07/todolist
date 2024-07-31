"""La Classe controlleur pour l'interaction de la couche Métier et la Vue"""
from tache import Tache
from data import Data

class Controller:
    def __init__(self):
        self.data= Data()
        self.tache = Tache("")

    # Ajouter une tâche
    def addata(self, nom):
        tache2 = Tache(nom)
        self.tache.ajouter(tache2)
        for t in self.tache.taches:
                # Insérer une nouvelle tâche
                self.data.insert_tache(t.nom, False)

    def updatedata(self, nom):
        tache2 = Tache("")
        for nom, status in self.data.retrieve_tache(nom):
            tache2.nom = nom
            tache2.status = status
        tache2.tacheAccomplis()
        self.data.update_tache(tache2.nom, tache2.status)

    def retrievedata(self,nom):
        self.data.retrieve_tache(nom)

    def deletedata(self,nom):
        self.data.delete_tache(nom)
    def closeconnection(self):
        # Fermer la connexion
        self.data.close_connection()
