#Name: Victoria
#Text-based Culinary testing game

#IMPORTING NECESSARY MODULES
from tkinter import*
import pygame
import time
#BACKGROUND MUSIC
root = Tk()
root.title('Culinary game sound player')
 
root.geometry("400x200")
 
pygame.mixer.init()# initialise the pygame
 
def play():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(loops=-1)
 
title=Label(root,text="CULINARY TEST",bd=5,relief=GROOVE,
            font=("times new roman",18,"bold"),bg="white",fg="green")
title.pack(side=TOP,fill=X)
 
play_button = Button(root, text="Play Song", font=("Helvetica", 12), command=play)
play_button.pack(pady=10)

info=Label(root,text="Click on the button above to play song and continue the game by clicking on the exit button",
           font=("times new roman",7,"bold")).pack(pady=5)
info=Label(root,text="or you can just click the exit button if you  don't want background music",
           font=("times new roman",7,"bold")).pack(pady=5)
root.mainloop()

#SCREEN SIZE
"""screen = pygame.display.set_mode((800,600))
background= pygame.image.load('kitchen.png')
background = pygame.transform.scale(background,(800,600))
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
#TITLE AND ICON
pygame.display.set_caption("CULINARY SKILL TEST")
icon = pygame.image.load('catering.png')
pygame.display.set_icon(icon)"""

#GREETINGS
print("WELCOME TO THE KITCHEN")
name= input("Enter your name: ")
print("Hello " + str(name))

#GLOBAL VAR
score = 0
playerList = []

#FOOD FUNCTION
def food():
    foodList = ["JOLLOF RICE", "JOLLOF SPAGHETTI", "YAM AND EGG SAUCE"]
    jRice = ["rice", "pepper", "salt", "tomatoes", "tomato paste", "onions", "spices", "seasoning", "broth"]
    jSpag = ["spaghetti", "pepper", "salt", "spices", "tomatoes", "tomato paste",  "broth", "veggies", "onions", "seasoning"]
    yamSauce = ["yam", "pepper", "egg", "water", "salt", "sugar", "onions", "oil", "seasoning", "tomato"]
    for meal in foodList:
        print(meal)
    foodChoice = str(input("which of the meal above do you wish to prepare?: ").upper())
    if foodChoice in foodList:
#Listing ingredients for J RICE
        if foodChoice == "JOLLOF RICE":
            recipe1 = str(input("give me one(1) main ingredient to prepare it: ").lower())
            if recipe1 in jRice:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score = +0
            recipe2 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe2 in jRice and recipe2 not in playerList:
                playerList.append(recipe2)
                score += 1
            else:
                playerList.append(recipe2)
                score += 0
            recipe3 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe3 in jRice and recipe3 not in playerList:
                playerList.append(recipe3)
                score += 1
            else:
                playerList.append(recipe3)
                score += 0
            recipe4 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe4 in jRice and recipe4 not in playerList:
                playerList.append(recipe4)
                score += 1
            else:
                playerList.append(recipe4)
                score += 0
            recipe5 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe5 in jRice and recipe5 not in playerList:
                playerList.append(recipe5)
                score += 1
                winORlose(score)
            else:
                playerList.append(recipe5)
                score += 0
                winORlose(score)
#Listing ingredients for J SPAG
        elif foodChoice == "JOLLOF SPAGHETTI":
            recipe1 = str(input("give me one(1) main ingredient to prepare it: ").lower())
            if recipe1 in jSpag:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score = +0
            recipe2 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe2 in jSpag and recipe2 not in playerList:
                playerList.append(recipe2)
                score += 1
            else:
                playerList.append(recipe2)
                score += 0
            recipe3 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe3 in jSpag and recipe3 not in playerList:
                playerList.append(recipe3)
                score += 1
            else:
                playerList.append(recipe3)
                score += 0
            recipe4 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe4 in jSpag and recipe4 not in playerList:
                playerList.append(recipe4)
                score += 1
            else:
                playerList.append(recipe4)
                score += 0
            recipe5 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe5 in jSpag and recipe5 not in playerList:
                playerList.append(recipe5)
                score += 1
                winORlose(score)
            else:
                playerList.append(recipe5)
                score += 0
                winORlose(score)
#List recipe for yam and egg sauce
        else :
            recipe1 = str(input("give me one(1) main ingredient to prepare it: ").lower())
            if recipe1 in yamSauce:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score = +0 
            recipe2 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe2 in yamSauce and recipe2 not in playerList:
                playerList.append(recipe2)
                score += 1
            else:
                playerList.append(recipe2)
                score += 0
            recipe3 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe3 in yamSauce and recipe3 not in playerList:
                playerList.append(recipe3)
                score += 1
            else:
                playerList.append(recipe3)
                score += 0
            recipe4 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe4 in yamSauce and recipe4 not in playerList:
                playerList.append(recipe4)
                score += 1
            else:
                playerList.append(recipe4)
                score += 0
            recipe5 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe5 in yamSauce and recipe5 not in playerList:
                playerList.append(recipe5)
                score += 1
                winORlose(score)
            else:
                playerList.append(recipe5)
                score += 0       
                winORlose(score)
    else: #input check 
        print("please input a food from the list displayed")
        food()
#SNACKS FUNCTION
def snacks():
    snacksList = ["EGGROLL", "DOUGHNUT", "MEAT PIE"]
    eRoll = ["egg", "flour", "baking powder", "margarine", "flavour", "salt", "sugar", "groundnut oil"]
    dnurt = ["flour", "yeast", "warm water", "salt", "sugar", "groundnut oil", "margarine", "milk", "egg"]
    mPie = ["flour", "baking powder", "salt", "margarine", "meat", "butter", "egg", "beef", "onions", "potato", "carrot", "spices"]
    for snack in snacksList:
        print(snack)
    snacksChoice = str(input("which of the snacks above do you wish to prepare?: ").upper())
    if snacksChoice in snacksList:
        if snacksChoice == "EGGROLL":
            recipe1 = str(input("give me one(1) main ingrdients to prepare it: ").lower())
            if recipe1 in eRoll:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score = +0
            recipe2 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe2 in eRoll and recipe2 not in playerList:
                playerList.append(recipe2)
                score += 1
            else:
                playerList.append(recipe2)
                score += 0 
            recipe3 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe3 in eRoll and recipe3 not in playerList:
                playerList.append(recipe3)
                score += 1
            else:
                playerList.append(recipe3)
                score += 0 
            recipe4 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe4 in eRoll and recipe4 not in playerList:
                playerList.append(recipe4)
                score += 1
            else:
                playerList.append(recipe4)
                score += 0 
            recipe5 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe5 in eRoll and recipe5 not in playerList:
                playerList.append(recipe5)
                score += 1
                winORlose(score)
            else:
                playerList.append(recipe5)
                score += 0 
                winORlose(score)
#list for doughnut recipe
        elif snacksChoice == "DOUGHNUT":
            recipe1 = str(input("give me one(1) main ingredient to prepare it: ").lower())
            if recipe1 in dnurt:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score = +0
            recipe2 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe2 in dnurt and recipe2 not in playerList:
                playerList.append(recipe2)
                score += 1
            else:
                playerList.append(recipe2)
                score += 0 
            recipe3 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe3 in dnurt and recipe3 not in playerList:
                playerList.append(recipe3)
                score += 1
            else:
                playerList.append(recipe3)
                score += 0 
            recipe4 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe4 in dnurt and recipe4 not in playerList:
                playerList.append(recipe4)
                score += 1
            else:
                playerList.append(recipe4)
                score += 0 
            recipe5 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe5 in dnurt and recipe5 not in playerList:
                playerList.append(recipe5)
                score += 1
                winORlose(score)
            else:
                playerList.append(recipe5)
                score += 0 
                winORlose(score)
#list for meat pie ingredient
        else:
            recipe1 = str(input("give me one(1) main ingredient to prepare it: ").lower())
            if recipe1 in mPie:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score = +0
            recipe2 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe2 in mPie and recipe2 not in playerList:
                playerList.append(recipe2)
                score += 1
            else:
                playerList.append(recipe2)
                score += 0 
            recipe3 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe3 in mPie and recipe3 not in playerList:
                playerList.append(recipe3)
                score += 1
            else:
                playerList.append(recipe3)
                score += 0 
            recipe4 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe4 in mPie and recipe4 not in playerList:
                playerList.append(recipe4)
                score += 1
            else:
                playerList.append(recipe4)
                score += 0 
            recipe5 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe5 in mPie and recipe5 not in playerList:
                playerList.append(recipe5)
                score += 1
                winORlose(score)
            else:
                playerList.append(recipe5)
                score += 0 
                winORlose(score)
    else: #input check 
        print("please input a snacks from the list displayed")
        snacks()
        
#ACCESS OR DENIAL TO STORE
def winORlose(score):
    print ("you got ",score," correctly")
    print ("here is the list of the ingredients you typed: ",playerList)
    if score >= 3:
        time.sleep(1)
        print("CONGRATULATIONS, CHEF " + str(name).upper() + " YOU NOW HAVE ACCESS TO ALL YOU NEED IN THE KITCHEN")
    else:
        time.sleep(2)
        print("SORRY, YOU NEED TO LEARN MORE TO COOK IN THE KITCHEN.")

#PLAYER DECIDING WHAT TO DO IN THE KITCHEN
def decisionMaking():
    choice= str(input("What do you want to prepare? FOOD/SNACKS: ").upper())
    if choice == "FOOD":
        food()
    elif choice == "SNACKS":
        snacks()
    else:
        print("please input the correct action")
        decisionMaking()
    
#WHILE LOOP
playagain = "yes"
while playagain == "yes" or playagain == "y":

    decisionMaking()
    playagain = input("Do you want to play again? (yes or y to continue playing): ").lower()
