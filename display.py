import os 

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
        
    