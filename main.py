import os
import characters
import weapons



run =True
menu =True
play =False
rules =False

def save():
    list=[name]

def clear():
   os.system("cls")


while run:
    while menu:
        clear()
        if rules:
            print("big dick")
            rules =False
            choice =""
            input("# ")
        else:    
         print("1, NEW GAME ")
         print("2, LOAD GAME ")
         print("3, RULES")
         print("4, EXIT ")

        

          
         choice = input("> ").lower()


         if choice in ["1", "new game", "new"]:
            play = True
            menu=False

         elif choice in ["2", "load game", "load", "saved", "last checkpoint"]:
            f=open("load.txt","r")
            load_list = f.readlines()
            # list for stats of the player in order as index
            # print(name,hp,attack)
            # print(game loaded or welcome back)
            input("> ")
            menu=False
            play=True

         elif choice in ["3", "rules"]:
            rules =True
            

         elif choice in ["4", "exit"]:
            quit()


    while play:
        pass


    while rules:
        pass

    