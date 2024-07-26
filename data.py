#!/usr/bin/python
import mariadb

class Data:

    def __init__(self, user="root", password="", host="localhost", database="taches"):
        """Initialise la connexion à la base de données"""
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                database=database
            )
            self.cur = self.conn.cursor()
            print("Connexion réussie à la base de données.")
        except mariadb.Error as e:
            print(f"Erreur de connexion : {e}")

    def insert_tache(self, nom, status=False):
        """Insère une tâche dans la table `taches`."""
        try:
            self.cur.execute("INSERT INTO taches (nom, status) VALUES (?, ?)", (nom, status))
            self.conn.commit()
            print(f"Dernier ID inséré : {self.cur.lastrowid}")
        except mariadb.Error as e:
            print(f"Erreur lors de l'insertion : {e}")

    def retrieve_tache(self, nom):
        """Récupère les informations d'une tâche en fonction du nom."""
        try:
            self.cur.execute("SELECT nom, status FROM taches WHERE nom=?", (nom,))
            results = self.cur.fetchall()
            for nom, status in results:
                print(f"Nom : {nom}, Statut : {'Accompli' if status else 'Non accompli'}")
            return results
        except mariadb.Error as e:
            print(f"Erreur lors de la récupération : {e}")



    def delete_tache(self, nom):
        """Supprime une tâche de la table `taches`."""
        try:
            self.cur.execute("DELETE FROM taches WHERE nom=?", (nom,))
            self.conn.commit()
            print(f"Tâche '{nom}' supprimée avec succès.")
        except mariadb.Error as e:
            print(f"Erreur lors de la suppression : {e}")

    def update_tache(self,nom,status):
        """Mettre à jour une tâche"""
        try:
            self.cur.execute("UPDATE taches SET status=? WHERE nom=?",(status, nom))
            self.conn.commit()
            print(f"La tâche {nom} a été mise à jour")
        except mariadb.Error as e:
            print(f"Erreur lors de la mise à jour : {e}")
    def close_connection(self):
        """Ferme la connexion à la base de données."""
        try:
            self.cur.close()
            self.conn.close()
            print("Connexion à la base de données fermée.")
        except mariadb.Error as e:
            print(f"Erreur lors de la fermeture de la connexion : {e}")
