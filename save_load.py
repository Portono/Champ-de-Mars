import json
import os

dico_all = {
    #-------------------Upgrades stats classiques-------------------------------------
    "dico_upgrades_stats":{
        "chance": 1,
        "gain_xp": 0,
        "pv": 0,
        "vitesse": 0,
        "regen_pv": 0,
        "vol_de_vie": 0,
        "esquive": 0,
        "renvoi": 0,
    },

    #------------------Upgrades armes uniques----------------------------------------
    "dico_upgrades_uniques": {
        "laser": {
            "laser_electrique": False,
            "laser_ralentissant": False,
            "laser_perforant": False
        },
        "roquette": {
            "roquette_shrapnel": False,
            "roquette_enflammee": False,
            "roquette_ricochet": False
        },
        "mine": {
            "mine_empoisonnee": False,
            "mine_fragmentation": False,
            "mine_double_vie": False
        },
        "aura": {
            "aura_trainee": False,
            "aura_scaling": False,
            "aura_pulse": False
        },
        "tourelle": {
            "tourelle_explosive": False,
            "tourelle_aoe_defensive": False,
            "tourelle_leurre": False
        },
    },

    #------------------Upgrades stats laser------------------------------------------
    "dico_upgrades_laser": {
        "cadence_de_tir": 0,
        "degat": 0,
        "taille_projectile": 0,
        "vitesse_balles": 0,
        "portee": 0,
    },

    #------------------Upgrades stats roquette------------------------------------------
    "dico_upgrades_roquette": {
        "cadence_de_tir": 0,
        "degat": 0,
        "taille_projectile": 0,
        "vitesse_balles": 0,
        "portee": 0,
    },

    #------------------Upgrades stats mine------------------------------------------
    "dico_upgrades_mine": {
        "cadence_de_tir": 0,
        "degat": 0,
        "taille_projectile": 0,
        "portee": 0
    },

    #------------------Upgrades stats aura------------------------------------------
    "dico_upgrades_aura": {
        "cadence_de_tir": 0,
        "degat": 0,
        "portee": 0
    },

    #------------------Upgrades stats tourelle------------------------------------------
    "dico_upgrades_tourelle": {
        "cadence_de_tir": 0,
        "degat": 0,
        "hp": 0,
        "vitesse_balles": 0,
        "portee": 0
    }
}


def sauvegarder_jeu():
    with open("save.json", "w") as fichier:
        json.dump(dico_all, fichier, indent=4)
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

        # Assure-toi que width et height sont définis globalement quelque part avant cet appel
        player_x = data.get("player_x", width // 2)
        player_y = data.get("player_y", height // 2)

        nombre_journees = data.get("nombre_journees", 0)
        duree_journee = data.get("duree_journee", 0)

        type_armes = data.get("armes", [])

        print("Sauvegarde chargée !")
    else:
        print("Aucune sauvegarde trouvée.")

