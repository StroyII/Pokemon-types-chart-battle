import os
import random
import time
from type import *
from joueur import *

class main():
    def __init__(self):
        self.types = []

        self.definir_types()
        self.main()

    def definir_types(self):
        # Adding the types in list
        types = []

        normal = Type("Normal",["Fighting"])
        types.append(normal)

        fire = Type("Fire", ["Water","Ground","Rock"])
        types.append(fire)

        water = Type("Water",["Grass","Electric"])
        types.append(water)

        grass = Type("Grass",["Fire","Ice","Poison","Flying","Bug"])
        types.append(grass)

        electric = Type("Electric",["Ground"])
        types.append(electric)

        ice = Type("Ice",["Fire","Fighting","Rock","Steel"])
        types.append(ice)

        fighting = Type("Fighting",["Flying","Psychic","Fairy"])
        types.append(fighting)

        poison = Type("Poison",["Ground","Psychic"])
        types.append(poison)

        ground = Type("Ground",["Water","Grass","Ice"])
        types.append(ground)

        flying = Type("Flying",["Electric","Ice","Rock"])
        types.append(flying)

        psychic = Type("Psychic",["Bug","Ghost","Dark"])
        types.append(psychic)

        bug = Type("Bug",["Fire","Flying","Rock"])
        types.append(bug)

        rock = Type("Rock",["Water","Grass","Fighting","Ground","Steel"])
        types.append(rock)

        ghost = Type("Ghost",["Ghost","Dark"])
        types.append(ghost)

        dragon = Type("Dragon",["Ice","Dragon","Fairy"])
        types.append(dragon)

        dark = Type("Dark",["Fighting","Bug","Fairy"])
        types.append(dark)

        steel = Type("Steel",["Fire","Fighting","Ground"])
        types.append(steel)

        fairy = Type("Fairy",["Poison","Steel"])
        types.append(fairy)

        # Adding in the class attribute
        self.types = type


    def main():
        #Start of loop
        is_game_on = True
        is_choix_mode_ok = True
        while(is_game_on):
            while(is_choix_mode_ok):
                choix_mode = input("Which gamemode ? (1:solo, 2:multiplayer)")
                if(choix_mode == "1"):
                    is_choix_mode_ok = False
                    nom_joueur_solo = input("Choose a username : ")
                    joueur_solo = Joueur(nom_joueur_solo)
                elif(choix_mode == "2"):
                    is_choix_mode_ok = False
                    nom_joueur_1 = input("Player1 : Choose a username : ")
                    joueur1 = Joueur(nom_joueur_1)
                    nom_joueur_2 = input("Player2 : Choose a username : ")
                    joueur2 = Joueur(nom_joueur_2)
                    is_multi_game_on = True
                    print(f"Joueur 1 = {joueur1.nom}\nJoueur 2 = {joueur2.nom}")
                    input("")
                    while(is_multi_game_on):
                        choix_joueur1 = input("")
                        


game = main()