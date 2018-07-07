#t.me/kamran_zone

#instagram.com/kamran._.zone

import os
import sys
os.system('clear')
print("----------------------------------")
print("-                                -") 
print("-       < EaSy InStAlLeR >       -")
print("-                                -")
print("-                                -")
print("- {01} install & update system   -")
print("- {99} exit                      -")
print("----------------------------------")
while True:
      s=input("~> ")
      if s == "01":
         os.system('apt update && apt upgrade')
         os.system('apt install git && apt install figlet')
         os.system('apt install python')
         os.system('apt upgrade python')
         os.system('apt install python2')
         os.system('apt upgrade python2')
         os.system('apt install python3')
         os.system('apt upgrade python3')
         os.system('apt install nano')
         os.system('apt install cmatrix')
         os.system('apt install php')
         os.system('apt upgrade php')
         os.system('clear')
         os.system('figlet -f small Done')
         print("{00} menu")
         s= input("\n~> ")
         if s == "00":
            os.system('clear')
            print("----------------------------------")
            print("-                                -") 
            print("-       < EaSy InStAlLeR >       -")
            print("-                                -")
            print("-                                -")
            print("- {01} install & update system   -")
            print("- {99} exit                      -")
            print("----------------------------------")
      elif s == "99":
           os.system('clear && figlet -f small Good Bye')
           exit()
