import pygame
import random
import math

pygame.init()

#-------------------Upgrades stats classiques-------------------------------------
dico_upgrades_stats={
                "chance":1,         
                "gain_xp":0,        
                "pv":0,             
                "vitesse":0,                        
                "regen_pv":0,           
                "vol_de_vie":0,  
                "esquive":0,
                "renvoi":0,
                }

#------------------Upgrades armes uniques----------------------------------------
dico_upgrades_uniques={
                "laser":{"laser_electrique":False,
                         "laser_ralentissant":False,
                         "laser_perforant":False
                         },
                "roquette":{"roquette_shrapnel":False,
                            "roquette_enflammee":False,
                            "roquette_ricochet":False
                            },
                "mine":{"mine_empoisonnee":False,
                        "mine_fragmentation":False,
                        "mine_double_vie":False
                        },
                "aura":{"aura_trainee":False,
                        "aura_scaling":False,
                        "aura_pulse":False
                        },
                "tourelle":{"tourelle_explosive":False,
                            "tourelle_aoe_defensive":False,
                            "tourelle_leurre":False
                            },
                "airstrike":{"airstrike_stun":False,
                             "airstrike_":False,
                             "airstrike_":False
                            }
                }
#------------------Upgrades stats laser------------------------------------------
dico_upgrades_laser={
                "cadence_de_tir":0,
                "degat":0,
                "taille_projectile":0,
                "vitesse_balles":0,
                "portee":0,
                }  
#------------------Upgrades stats roquette------------------------------------------   
dico_upgrades_roquette={
                "cadence_de_tir":0,
                "degat":0,
                "taille_projectile":0,
                "vitesse_balles":0,
                "portee":0,
                }
#------------------Upgrades stats mine------------------------------------------
dico_upgrades_mine={
                "cadence_de_tir":0,
                "degat":0,
                "taille_projectile":0,
                "portee":0
                }
#------------------Upgrades stats aura------------------------------------------
dico_upgrades_aura={
                "cadence_de_tir":0,
                "degat":0,
                "portee":0
                }
#------------------Upgrades stats tourelle------------------------------------------
dico_upgrades_tourelle={
                "cadence_de_tir":0,
                "degat":0,
                "hp":0,
                "vitesse_balles":0,
                "portee":0
                }
#------------------Upgrades stats tourelle------------------------------------------
dico_upgrades_airstrike={
                "cadence_de_tir":0,
                "degat":0,
                }
