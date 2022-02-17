from pystyle import *
from pycenter import center 


banner1 = """
 █████                   █████ █████            █████                                 
░░███                   ░░███ ░░███            ░░███                                  
 ░███████  █████ ████    ░░███ ███    ██████   ███████    █████  █████ ████ █████ ████
 ░███░░███░░███ ░███      ░░█████    ░░░░░███ ░░░███░    ███░░  ░░███ ░███ ░░███ ░███ 
 ░███ ░███ ░███ ░███       ░░███      ███████   ░███    ░░█████  ░███ ░███  ░███ ░███ 
 ░███ ░███ ░███ ░███        ░███     ███░░███   ░███ ███ ░░░░███ ░███ ░███  ░███ ░███ 
 ████████  ░░███████        █████   ░░████████  ░░█████  ██████  ░░████████ ░░████████
░░░░░░░░    ░░░░░███       ░░░░░     ░░░░░░░░    ░░░░░  ░░░░░░    ░░░░░░░░   ░░░░░░░░ 
            ███ ░███                                                                  
           ░░██████                                                                   
            ░░░░░░                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
"""

Anime.Fade(Center.Center(banner1), Colors.red_to_blue,Colorate.Vertical, interval=0.005, enter=True)

from os import system
from pyfade import Colors, Fade
import random, string
from os import system

sxzweb = """
                              
 ██████╗ ███████╗███╗   ██╗    
██╔════╝ ██╔════╝████╗  ██║    
██║  ███╗█████╗  ██╔██╗ ██║    
██║   ██║██╔══╝  ██║╚██╗██║    
╚██████╔╝███████╗██║ ╚████║    
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝    
                                    
                                             
                                                                                       
"""
print(Fade.Vertical (Colors.blue_to_green_reversed, sxzweb))
amount = int(input('Enter 1 for Gen a nitro: '))
value = 1
while value <= amount :
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open ('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'Generer | {code}')
    value *=1
    system("cls")
    