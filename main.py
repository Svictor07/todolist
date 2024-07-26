from controller import Controller
import keyboard
if __name__ == "__main__":

    controller=Controller()
    # Entrer au clavier de la tâche
    nom = input("Entrer votre tâche: ")
    controller.addata(nom)
    print(f"Voulez vous modifier la tâche {nom}")
    while True:
        if keyboard.read_key() == "y":
            print("yes")
            # Modifier une tache
            controller.updatedata(nom)
            break

    # Récupérer une tâche
    controller.retrievedata(nom)

    print(f"Voulez vous supprimer la tâche {nom}")
    while True:
        if keyboard.read_key() == "y":
            print("yes")
            # supprimer une tâche
            controller.deletedata(nom)
            break

    #Fermer la connexion
    controller.closeconnection()