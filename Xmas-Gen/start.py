import os
from colorama import Fore

print(Fore.MAGENTA+"""

 ██╗░░██╗███╗░░░███╗░█████╗░░██████╗░░░░░░░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
╚██╗██╔╝████╗░████║██╔══██╗██╔════╝░░░░░░██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚███╔╝░██╔████╔██║███████║╚█████╗░█████╗███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░██╔██╗░██║╚██╔╝██║██╔══██║░╚═══██╗╚════╝██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██╔╝╚██╗██║░╚═╝░██║██║░░██║██████╔╝░░░░░░██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░░░░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                                                                                   
                                                                 


""")

print(Fore.YELLOW+"""

1.Generate token
2.How it's works

""")

command = input('> ')

if command == '1':
    os.system('cmd /k "python Xmas-Gen/gen.py"')

elif command == '2':
    os.system('cmd /k "python Xmas-Gen/info.py"')



else:
  print('Please choose the correct one dont be dumb')