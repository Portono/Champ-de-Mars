import json
from paths import data_path
import os

SAVE_FILE = "save.json"
SCORE_FILE="score"

def save_existe():
    return os.path.exists(data_path(SAVE_FILE))


def supprimer_sauvegarde():
    if save_existe():
        os.remove(data_path(SAVE_FILE))

from random_module import (dico_upgrades_stats, dico_upgrades_uniques,
                           dico_upgrades_laser, dico_upgrades_roquette,
                           dico_upgrades_mine, dico_upgrades_aura,
                           dico_upgrades_tourelle)
def _charger_donnees_sauvegarde():
    try:
        with open(data_path(SAVE_FILE), "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def charger_meilleur_score():
    try:
        with open(data_path(SCORE_FILE), "r") as f:
            return max(0, int(f.read().strip() or "0"))
    except (FileNotFoundError, ValueError):
        data = _charger_donnees_sauvegarde()
        return max(data.get("meilleur_score", 0), data.get("nombre_journees", 0))

def charger_score():
    return charger_meilleur_score()

def mettre_a_jour_meilleur_score(nombre_journees):
    meilleur_score = max(charger_meilleur_score(), nombre_journees)
    with open(data_path(SCORE_FILE), "w") as f:
        f.write(str(meilleur_score))
    return meilleur_score


def sauvegarder_jeu(armes_possedees,nombre_journees=0):
    meilleur_score = max(charger_meilleur_score(), nombre_journees)
    data = {
        "dico_upgrades_stats": dico_upgrades_stats,
        "dico_upgrades_uniques": dico_upgrades_uniques,
        "dico_upgrades_laser": dico_upgrades_laser,
        "dico_upgrades_roquette": dico_upgrades_roquette,
        "dico_upgrades_mine": dico_upgrades_mine,
        "dico_upgrades_aura": dico_upgrades_aura,
        "dico_upgrades_tourelle": dico_upgrades_tourelle,
        "armes_possedees": armes_possedees,
        "nombre_journees": nombre_journees,
        "meilleur_score":meilleur_score
    }
    with open(data_path(SAVE_FILE), "w") as f:
        json.dump(data, f, indent=4)
    print("Jeu sauvegardé !")

def charger_jeu():
    try:
        with open(data_path(SAVE_FILE), "r") as f:
            data = json.load(f)

        dico_upgrades_stats.update(data.get("dico_upgrades_stats", {}))
        dico_upgrades_laser.update(data.get("dico_upgrades_laser", {}))
        dico_upgrades_roquette.update(data.get("dico_upgrades_roquette", {}))
        dico_upgrades_mine.update(data.get("dico_upgrades_mine", {}))
        dico_upgrades_aura.update(data.get("dico_upgrades_aura", {}))
        dico_upgrades_tourelle.update(data.get("dico_upgrades_tourelle", {}))

        # Pour les uniques, update arme par arme
        for arme, upgrades in data.get("dico_upgrades_uniques", {}).items():
            if arme in dico_upgrades_uniques:
                dico_upgrades_uniques[arme].update(upgrades)

        armes_possedees = data.get("armes_possedees", ["stats"])
        nombre_journees = data.get("nombre_journees", 0)
        print("Sauvegarde chargée !")
        return armes_possedees,nombre_journees

    except (FileNotFoundError, json.JSONDecodeError):
        print("Aucune sauvegarde trouvée.")
        return ["stats"],0
