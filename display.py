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
    def inventory():
        print(r"""   ___   ___
      / /
     / /          __                ___         __     __  ___     ___        __
    / /        //   ) ) ||  / /   //___) )   //   ) )   / /      //   ) )   //  ) )  //   / /
   / /        //   / /  || / /   //         //   / /   / /      //   / /   //       ((___/ /
__/ /___     //   / /   ||/ /   ((____     //   / /   / /      ((___/ /   //            / /
""")
        
    @staticmethod
    def shop():
        print(r"""
    //   ) )
   ((           / __        ___        ___
     \\        //   ) )   //   ) )   //   ) )
       ) )    //   / /   //   / /   //___/ /
((___ / /    //   / /   ((___/ /   //
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

    @staticmethod
    def printhub():
        p(" \n Where do you want to go ? : \n")
        p("1.  [red]See the inventory[/red]")
        p("2.  [blue]Go to shop[/blue]")
        p("3.  [green]Endless cave[/green]")
        p("4.  [yellow]Dungeon (INSANE!)[/yellow] \n \n")

    @staticmethod
    def quitinventory():
        p(" \n Do you want to quit inventory ? \n")
        p("1.  [red]Yes ![/red]")
        p("2.  [blue]Never (If you are angry)[/blue]")

    @staticmethod
    def shopcategories():
        p(" \n What do you want to buy ? \n")
        p("1.  [red]Swords[/red]")
        p("2.  [red]Knives[/red]")
        p("3.  [red]Hammer[/red]")
        p("4.  [red]Mage's sticks[/red]")
        p("5.  [red]Shields[/red]")
        p("6.  [red]Helmet[/red]")
        p("7.  [red]Chestplate[/red]")
        p("8.  [red]Leggings[/red]")
        p("9.  [red]Boots[/red]")
        p("10.  [red]Potions[/red]")
        p("11.  [blue]Nevermind[/blue] \n \n")
        
    
    





        
    