SAVE_FILE = "savegame.json"


def sauvegarder_partie():
    global nombre_journees, niveau, xp, xp_for_level
    global player_x, player_y, pv_joueur, pv_max_joueur
    global upgrades_joueur, type_armes

    data = {
        "nombre_journees": nombre_journees,
        "niveau": niveau,
        "xp": xp,
        "xp_for_level": xp_for_level,
        "player_x": player_x,
        "player_y": player_y,
        "pv_joueur": pv_joueur,
        "pv_max_joueur": pv_max_joueur,
        "upgrades_joueur": upgrades_joueur,
        "armes_debloquees": [arme.classe.__name__ if hasattr(arme, "classe") else "aura" for arme in type_armes]
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

    print("Partie sauvegardée !")


def charger_partie():
    global nombre_journees, niveau, xp, xp_for_level
    global player_x, player_y, pv_joueur, pv_max_joueur
    global upgrades_joueur, type_armes
    global laser, roquette, mine, aura_active

    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

        nombre_journees = data["nombre_journees"]
        niveau = data["niveau"]
        xp = data["xp"]
        xp_for_level = data["xp_for_level"]
        player_x = data["player_x"]
        player_y = data["player_y"]
        pv_joueur = data["pv_joueur"]
        pv_max_joueur = data["pv_max_joueur"]
        upgrades_joueur = data["upgrades_joueur"]

        type_armes.clear()

        for arme_nom in data["armes_debloquees"]:
            if arme_nom == "projectile_laser":
                type_armes.append(laser)
            elif arme_nom == "projectile_roquette":
                type_armes.append(roquette)
            elif arme_nom == "projectile_mine":
                type_armes.append(mine)
            elif arme_nom == "aura":
                type_armes.append(aura_active)

        print("Partie chargée !")

    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
