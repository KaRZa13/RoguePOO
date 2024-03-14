import os
from rich import print as p
from rich.pretty import pprint


class Display:

    @staticmethod
    def clear_console():
        os.system("cls")

    @staticmethod
    def title():
        print(r""" #####     ####     ####    ##  ##   ######   #####     ####     ####
 ##  ##   ##  ##   ##  ##   ##  ##   ##       ##  ##   ##  ##   ##  ##
 ##  ##   ##  ##   ##       ##  ##   ##       ##  ##   ##  ##   ##  ##
 #####    ##  ##   ## ###   ##  ##   ####     #####    ##  ##   ##  ##
 ####     ##  ##   ##  ##   ##  ##   ##       ##       ##  ##   ##  ##
 ## ##    ##  ##   ##  ##   ##  ##   ##       ##       ##  ##   ##  ##
 ##  ##    ####     ####     ####    ######   ##        ####     ####

""")
        
    @staticmethod
    def char_choice():
        pass


    @staticmethod
    def menu():
        print(r"""
    /|    //| |
   //|   // | |     ___         __
  // |  //  | |   //___) )   //   ) )   //   / /
 //  | //   | |  //         //   / /   //   / /
//   |//    | | ((____     //   / /   ((___( (
""")
        
    
    @staticmethod
    def name_choice():
        print("Choose your character name :")
        return str(input())
    
    @staticmethod
    def class_choice():
        p(f"Choose between your attacks :\n \n\
        1.  [red]Warrior[/red] \n \n\
        2.  [red]Mage[/red] \n \n\
        3.  [red]Thief[/red] \n \n\
        4.  [red]Colossus[/red] \n \n\
              ")
        choice = int(input())
        return choice
        
    
    





        
    