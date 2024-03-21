from colorama import Fore,Back,Style
import platform,os
import time 

OsName = platform.uname()[0]



def banner():
    if OsName == "Windows":
      os.system("cls")
      hello = Fore.GREEN+"************ Hello Friend ***************"
      def type_text(text, delay):
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(delay)

      def print_variable_text():
            type_text(hello , 0.1)
      print_variable_text()

    else:
      os.system("clear")
      
    print()
    print()
    print(Fore.GREEN+"             Make By ")   
    print(Fore.RED+"███████╗   ███╗   ███╗   ██╗  ██╗")  
    print(Fore.RED+"██╔════╝   ████╗ ████║   ██║  ██║" )
    print(Fore.GREEN+"███████╗   ██╔████╔██║   ███████║")
    print(Fore.GREEN+"╚════██║   ██║╚██╔╝██║   ██╔══██║ "  )
    print(Fore.BLUE+"███████║██╗██║ ╚═╝ ██║██╗██║  ██║" )
    print(Fore.BLUE+"╚══════╝╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝" )
    print(Fore.GREEN)
    print(Style.BRIGHT)

banner()