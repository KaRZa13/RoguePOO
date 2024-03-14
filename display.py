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
    def village():
        print(r"""
||   / /
||  / /     ( )     //     //      ___       ___        ___
|| / /     / /     //     //     //   ) )  //   ) )   //___) )
||/ /     / /     //     //     //   / /  ((___/ /   //
|  /     / /     //     //     ((___( (    //__     ((____
""")
        

    @staticmethod
    def printclass():
        p(" \n Choose your class : \n")
        p("1.  [red]Warrior[/red]")
        p("2.  [blue]Mage[/blue]")
        p("3.  [green]Thief[/green]")
        p("4.  [yellow]Colossus[/yellow] \n \n")
    
    @staticmethod
    def printchar(name,charclass):
        p("Hello " + name + " the " + charclass + " !")
        
    
    





        
    