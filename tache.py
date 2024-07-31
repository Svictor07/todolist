
"""Classe principale qui définit une tâche
et ses différentes méthodes CRUD"""
class Tache:

    def __init__(self,nom):
        self.nom=nom
        self.status=False
        self.taches = []

    def ajouter(self,tache):
        self.taches.append(tache)

    def tacheAccomplis(self):
        if self.status==False:
            self.status=True

    def supprimer(self,tache):
        index = self.taches.index()
        del self.taches[index]

    def __repr__(self):
        return f"la tâche {self.nom} est {self.status}"
