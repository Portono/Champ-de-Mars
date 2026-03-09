import json
import os

def sauvegarder_jeu():
    data = {
        "pv_joueur": pv_joueur,
        "xp": xp,
        "niveau": niveau,
        "player_x": player_x,
        "player_y": player_y,
        "nombre_journees": nombre_journees,
        "duree_journee": duree_journee,
        "armes": type_armes
    }

    with open("save.json", "w") as fichier:
        json.dump(data, fichier, indent=4)

    print("Jeu sauvegardé !")
    
    
    
    
    def charger_jeu():
        global pv_joueur, xp, niveau
        global player_x, player_y
        global nombre_journees, duree_journee
        global type_armes

        if os.path.exists("save.json"):
            with open("save.json", "r") as fichier:
                data = json.load(fichier)

            pv_joueur = data.get("pv_joueur", 100)
            xp = data.get("xp", 0)
            niveau = data.get("niveau", 1)

            player_x = data.get("player_x", width // 2)
            player_y = data.get("player_y", height // 2)

            nombre_journees = data.get("nombre_journees", 0)
            duree_journee = data.get("duree_journee", 0)

            type_armes = data.get("armes", [])

            print("Sauvegarde chargée !")
        else:
            print("Aucune sauvegarde trouvée.")
