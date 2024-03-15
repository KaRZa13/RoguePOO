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
    def castle():
        print(r"""
                                  |>>>
                                  |
                    |>>>      _  _|_  _         |>>>
                    |        |;| |;| |;|        |
                _  _|_  _    \\.    .  /    _  _|_  _
               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
               \\..      /    ||;   . |    \\.    .  /
                \\.  ,  /     ||:  .  |     \\:  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |       \,/
                 ||:   ||:  ,  _______   .   ||: , |            /`\
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~
""")
    @staticmethod
    def skeleton():
        print(r"""
                             _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'

""")
    @staticmethod
    def drake():
        print(r"""
            __                  __
            ( _)                ( _)
           / / \\              / /\_\_
          / /   \\            / / | \ \
         / /     \\          / /  |\ \ \
        /  /   ,  \ ,       / /   /|  \ \
       /  /    |\_ /|      / /   / \   \_\
      /  /  |\/ _ '_| \   / /   /   \    \\
     |  /   |/  0 \0\    / |    |    \    \\
     |    |\|      \_\_ /  /    |     \    \\
     |  | |/    \.\ o\o)  /      \     |    \\
     \    |     /\\`v-v  /        |    |     \\
      | \/    /_| \\_|  /         |    | \    \\
      | |    /__/_ `-` /   _____  |    |  \    \\
      \|    [__]  \_/  |_________  \   |   \    ()
       /    [___] (    \         \  |\ |   |   //
      |    [___]                  |\| \|   /  |/
     /|    [____]                  \  |/\ / / ||
    (  \   [____ /     ) _\      \  \    \| | ||
     \  \  [_____|    / /     __/    \   / / //
     |   \ [_____/   / /        \    |   \/ //
     |   /  '----|   /=\____   _/    |   / //
  __ /  /        |  /   ___/  _/\    \  | ||
 (/-(/-\)       /   \  (/\/\)/  |    /  | /
               (/\/\)           /   /   //
                      _________/   /    /
                     \____________/    (
""")

    @staticmethod
    def demon():
        print(r"""
                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'
""")

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
    def swords():
        print(r"""
    //   ) )
   ((                           ___        __        ___   /      ___
     \\        //  / /  / /   //   ) )   //  ) )   //   ) /     ((   ) )
       ) )    //  / /  / /   //   / /   //        //   / /       \ \
((___ / /    ((__( (__/ /   ((___/ /   //        ((___/ /     //   ) )

""")
    
    @staticmethod
    def knives():
        print(r"""
    //   / /
   //__ / /       __       ( )              ___        ___
  //__  /      //   ) )   / /   ||  / /   //___) )   ((   ) )
 //   \ \     //   / /   / /    || / /   //           \ \
//     \ \   //   / /   / /     ||/ /   ((____     //   ) )

""")
        
    @staticmethod
    def hammers():
        print(r"""
    //    / /
   //___ / /      ___        _   __        _   __        ___        __        ___
  / ___   /     //   ) )   // ) )  ) )   // ) )  ) )   //___) )   //  ) )   ((   ) )
 //    / /     //   / /   // / /  / /   // / /  / /   //         //          \ \
//    / /     ((___( (   // / /  / /   // / /  / /   ((____     //        //   ) )

""")
        
    @staticmethod
    def sticks():
        print(r"""
    //   ) )
   ((         __  ___    ( )      ___       / ___      ___
     \\        / /      / /     //   ) )   //\ \     ((   ) )
       ) )    / /      / /     //         //  \ \     \ \
((___ / /    / /      / /     ((____     //    \ \ //   ) )

""")
        
    @staticmethod
    def shields():
        print(r"""
    //   ) )
   ((           / __       ( )      ___       //      ___   /      ___
     \\        //   ) )   / /     //___) )   //     //   ) /     ((   ) )
       ) )    //   / /   / /     //         //     //   / /       \ \
((___ / /    //   / /   / /     ((____     //     ((___/ /     //   ) )

""")
        
    @staticmethod
    def helmets():
        print(r"""
    //    / /
   //___ / /      ___       //      _   __        ___     __  ___     ___
  / ___   /     //___) )   //     // ) )  ) )   //___) )   / /      ((   ) )
 //    / /     //         //     // / /  / /   //         / /        \ \
//    / /     ((____     //     // / /  / /   ((____     / /      //   ) )

""")

    @staticmethod
    def chestplates():
        print(r"""
    //   ) )
   //           / __        ___        ___     __  ___     ___       //      ___     __  ___     ___        ___
  //           //   ) )   //___) )   ((   ) )   / /      //   ) )   //     //   ) )   / /      //___) )   ((   ) )
 //           //   / /   //           \ \      / /      //___/ /   //     //   / /   / /      //           \ \
((____/ /    //   / /   ((____     //   ) )   / /      //         //     ((___( (   / /      ((____     //   ) )

""")

    @staticmethod
    def leggings():
        print(r"""
    / /
   / /         ___       ___       ___       ( )       __       ___        ___
  / /        //___) )  //   ) )  //   ) )   / /     //   ) )  //   ) )   ((   ) )
 / /        //        ((___/ /  ((___/ /   / /     //   / /  ((___/ /     \ \
/ /____/ / ((____      //__      //__     / /     //   / /    //__     //   ) )

""")

    @staticmethod
    def boots():
        print(r"""
    //   ) )
   //___/ /      ___        ___     __  ___     ___
  / __  (      //   ) )   //   ) )   / /      ((   ) )
 //    ) )    //   / /   //   / /   / /        \ \
//____/ /    ((___/ /   ((___/ /   / /      //   ) )

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
        p("10.  [red]Potions WIP[/red]")
        p("11.  [blue]Nevermind[/blue] \n \n")

    @staticmethod
    def cantafford():
        p("You can't afford this item")
        
    
    





        
    