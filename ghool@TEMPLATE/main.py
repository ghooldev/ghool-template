# This is the main file which brings everything together!

from pystyle import Colorate, Colors
import os
import time
# if you have any core folder files, use "from core.{FILE_NAME} import *"
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

class GhoolTemplate:
    def __init__(self):
        self.banner_art = r'''
                                                     __                __
                                              ____ _/ /_  ____  ____  / /
                                             / __ `/ __ \/ __ \/ __ \/ / 
                                            / /_/ / / / / /_/ / /_/ / /  
                                            \__, /_/ /_/\____/\____/_/   
                                            /____/                     
                                        - Template Made By ghooldev!
                                         _________________________________

'''
        self.home_art = r'''
                        [01] > Option 1         [02] > Option 2         [03] > Option 3
                        [04] > Option 4         [05] > Option 5         [06] > Option 6
                                                [07] > Option 7 (Usually "Exit")

'''
        self.setup()

    def setup(self):
        # update() (optional)
        os.system('cls')
        self.homemenu()

    def banner(self):
        # Colors.red_to_black controls the gradient's colors.
        print(Colorate.Vertical(Colors.red_to_black, self.banner_art))
    
    def homemenu(self):
        while True:
            os.system('title ghooltemp@MAIN')
            os.system('cls')
            self.banner()
            print(Colorate.Vertical(Colors.red_to_black, self.home_art))
            inp = input(Fore.RED + "[ghooltemp@MENU] > ")

            if inp == "1":
                # Put option 1 function here.
                pass
            elif inp == "2":
                # Put option 2 function here.
                pass
            elif inp == "3":
                # Put option 3 function here.
                pass
            elif inp == "4":
                # Put option 4 function here.
                pass
            elif inp == "5":
                # Put option 5 function here.
                pass
            elif inp == "6":
                # Put option 6 function here.
                pass
            elif inp == "7":
                # Put option 7 function here.
                pass
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.homemenu()

    # '''If you want to make a new page handler, use this as a template.
    # def {PAGE_NAME}(self):
    #   while True:
    #   os.system('title {TITLE_HERE}')
    #   os.system('cls')
    #   self.banner()
    #   print({Page_Options})
    #   inp = input(Fore.RED + "{INPUT_HERE}" + Fore.Reset)
    #   
    #   if inp = "1":
    #       {OPTION 1 FUNCTION}
    #   else:
    #       print(Fore.RED + "{INVALID_OPTION}" + Fore.RESET)
    #       time.sleep(1)
    #       self.{PAGE_NAME}'''

# Usage
if __name__ == "__main__":
    ghooltemp = GhoolTemplate()