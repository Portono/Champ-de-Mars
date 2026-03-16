import json
import os


SAVE_FILE = "save.json"


def sauvegarder_jeu(donnee_de_sauvegarde):

    with open(data_path(SAVE_FILE), "w") as fichier:
        json.dump(donnee_de_sauvegarde, fichier, indent=4)

    print("Jeu sauvegardé !")


def charger_jeu():

    if os.path.exists(SAVE_FILE):

        with open(SAVE_FILE, "r") as fichier:
            data = json.load(fichier)

        Main_game.pv_joueur = data.get("pv_joueur", 100)
        Main_game.xp = data.get("xp", 0)
        Main_game.niveau = data.get("niveau", 1)

        Main_game.player_x = data.get("player_x", Main_game.width // 2)
        Main_game.player_y = data.get("player_y", Main_game.height // 2)

        Main_game.nombre_journees = data.get("nombre_journees", 0)
        Main_game.duree_journee = data.get("duree_journee", 0)

        Main_game.armes_possedees = data.get("armes", [])

        Main_game.dico_upgrades_stats = data.get("dico_upgrades_stats", {})
        Main_game.dico_upgrades_uniques = data.get("dico_upgrades_uniques", {})
        Main_game.dico_upgrades_laser = data.get("dico_upgrades_laser", {})
        Main_game.dico_upgrades_roquette = data.get("dico_upgrades_roquette", {})
        Main_game.dico_upgrades_mine = data.get("dico_upgrades_mine", {})
        Main_game.dico_upgrades_aura = data.get("dico_upgrades_aura", {})
        Main_game.dico_upgrades_tourelle = data.get("dico_upgrades_tourelle", {})

        print("Sauvegarde chargée !")

    else:
        print("Aucune sauvegarde trouvée.")
