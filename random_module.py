import pygame
import random
import math

pygame.init()


dico_upgrades={
                "chance":1,         ##fait
                "gain_xp":0,        ##fait
                "pv":0,             ##fait
                "vitesse":1,        ##fait
                "vitesse_balles":0, ##fait
                "cadence_de_tir":0, ##fait
                "degats":0,         ##fait
                "portee":0,         ##fait
                "regen_pv":0,       ##fait
                "degats_aoe":0,     ##fait
                "vol_de_vie":0,
                "taille_projectiles":0,##fait
                "duree_aoe":0,
                "multishot":0,
                "deflagrations":0,  ##fait
                "esquive":0,
                "renvoi":0,
                "perforation":0,
                "arc_degats":0,
                "tirs_ralentissants":0,
                "resistance":0,
                "summon_allies":0,
                "distance_damage":0,
                }

dico_rarete_upgrades={
                "chance":"commun",
                "pv":"commun",
                "vitesse":"commun",
                "vitesse_balles":"commun",
                "degats":"commun",
                "portee":"commun",
                "cadence_de_tir":"commun",
                "gain_xp":"commun",
                "degats_aoe":"rare",
                "duree_aoe":"rare",
                "regen_pv":"rare",
                "taille_projectiles":"rare",
                "resistance":"rare",
                "deflagrations":"rare",
                "vol_de_vie":"epique",
                "renvoi":"epique",
                "perforation":"epique",
                "arc_degats":"epique",
                "tirs_ralentissants":"epique",
                "distance_damage":"epique",
                "esquive":"epique",
                "multishot":"legendaire",
                "summon_allies":"legendaire"
                }

dico_poids_upgrade={
                "chance":1,
                "gain_xp":0,
                "pv":0,
                "vitesse":0,
                "vitesse_balles":0,
                "cadence_de_tir":0,
                "degats":0,
                "portee":0,
                "regen_pv":0,
                "degats_aoe":0,
                "duree_aoe":0,
                "vol_de_vie":0,
                "taille_projectiles":0,
                "multishot":0,
                "deflagrations":0,
                "esquive":0,
                "renvoi":0,
                "perforation":0,
                "arc_degats":0,
                "tirs_ralentissants":0,
                "resistance":0,
                "summon_allies":0,
                "distance_damage":0,
                }

def get_coef_rarete(upgrade):
    table_rarete={"commun":9,"rare":6,"epique":3,"legendaire":1}
    return table_rarete.get(dico_rarete_upgrades[upgrade],1)

def random_upgrade(dico_cible):
    total_points=sum(v for k,v in dico_cible.items() if k!="chance")
    multipl_rarete=dico_cible["chance"]
    poids_resultat={}
    for upgrade in dico_cible:
        if upgrade=="chance":
            poids_resultat[upgrade]=1
            continue
        r=get_coef_rarete(upgrade)
        if total_points>0:
            ratio=dico_cible[upgrade]/total_points
            malus=(ratio/multipl_rarete)
            poids=r*(1-malus)
        else:
            poids=r
        poids_resultat[upgrade]=max(0,poids)
    return poids_resultat

def choisir_upgrades(dico_cible,nb_options=3):
    poids_resultat=random_upgrade(dico_cible)
    options=[]
    poids_temp=poids_resultat.copy()
    for _ in range(nb_options):
        noms=list(poids_temp.keys())
        poids=list(poids_temp.values())
        if sum(poids)==0:
            break   ##au cas ou tous les poids serait a 0, on sait jamais
        choix=random.choices(noms,weights=poids,k=1)[0] ##renvoie une selection au hasard de facon aleatoire en prenant compte le poids
        options.append(choix)
        poids_temp[choix]=0
    return options

def level_up(screen, width, height, cible):
    # Initialisation...
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, int(height*0.05))
    
    # DÉTERMINER LES OPTIONS
    if isinstance(cible, list):
        options = cible  # On utilise directement la liste d'armes bloquées
    else:
        options = choisir_upgrades(cible) # On utilise ta logique de poids/rarete
        
    while True:
        # Gestion des événements et dessin (ton code actuel)...
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(rects):
                    if rect.collidepoint(event.pos):
                        choix = options[i]
                        
                        # LOGIQUE DE RETOUR
                        if isinstance(cible, list):
                            return choix # On renvoie juste le nom de l'arme ("roquette")
                        else:
                            cible[choix] += 1 # On incrémente la stat dans le dico
                            return cible

        screen.fill((255,255,255))

        r_width=width/4
        r_height=height/3
        gap=(width - 3*r_width)/4

        rects=[]
        for i in range(3):
            pos_x=gap+i*(r_width+gap)
            rect=pygame.Rect(pos_x,height/2-r_height/2,r_width,r_height)
            rects.append(rect)
            pygame.draw.rect(screen,(155,155,155),rect,border_radius=15)
            texte_surface=font.render(options[i].replace("_"," ").upper(),True,(255,255,255))
            texte_rect=texte_surface.get_rect(center=rect.center)
            screen.blit(texte_surface,texte_rect)
        pygame.display.flip()
        clock.tick(60)

def choisir_nouvelle_arme(dico_armes,nb_options=3):
    armes_disponibles=[nom for nom, niveau in dico_armes.items() if niveau==0]
    n=min(len(armes_disponibles),nb_options)
    if n>0:
        return random.sample(armes_disponibles, n)

