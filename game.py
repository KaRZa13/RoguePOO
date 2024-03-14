from rich import print
from display import Display
from player import *
from dice import Dice
from attack import Attack

HALF = 50
THREE_QUARTERS = 75
QUARTER = 25

ATTACK_DICE = Dice(100)
ATT1 = Attack("Normal attack", 6, THREE_QUARTERS, 1.25, QUARTER, "Just a normal sword strike", ATTACK_DICE)
ATT2 = Attack("Big attack", 4, HALF, 2.25, HALF, "A big attack , 50/50 either you destroy the opponent or you just miss your attack", ATTACK_DICE)

CLASS_TYPES = [0, "Warrior", "Mage", "Thief", "Colossus"]

class Game:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.display = Display()

    def start(self):
        self.display.clear_console()
        self.display.title()
        self.display.menu()
        if self.player == None:
            self.player = self.choose_class()


    def choose_class(self):

        name = input(" \n Choose your name : ")

        self.display.printclass()

        class_input = int(input(""))


        if class_input == 1:
            self.player =  Warrior(name, 20, 3, ATT1,ATT2)
        elif class_input == 2:
            self.player = Mage(name, 20, 3, ATT1,ATT2)
        elif class_input == 3:
            self.player = Thief(name, 20, 3, ATT1,ATT2)
        elif class_input == 4:
            self.player = Colossus(name, 20, 3, ATT1,ATT2)
        else:
            print("Entrée invalide. Veuillez choisir un numéro entre 1 et 4.")
            return self.choose_class()
        
        self.display.printchar(name,CLASS_TYPES[class_input])