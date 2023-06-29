#Name: Victoria
#Text-based Culinary testing game

"""
ADD EFFECTS AND PLAY THE GAME
"""

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
    jSpag = ["spaghetti", "pepper", "salt", "spices", "tomato", "broth", "veggies", "onions", "seasoning"]
    yamSauce = ["yam", "pepper", "egg", "water", "salt", "sugar", "onions", "oil", "seasoning", "tomato"]
    for idx, meal in enumerate(foodList):
        print(idx,meal)
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
                score += 0
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
                score += 0
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
                score += 0 
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
    else: #validation check in concordance to food list
        print("please input a food from the list displayed")
        food()
#SNACKS FUNCTION
def snacks():
    snacksList = ["EGGROLL", "DOUGHNUT", "MEAT PIE"]
    eRoll = ["egg", "flour", "baking powder", "margarine", "flavour", "salt", "sugar", "groundnut oil"]
    dnurt = ["flour", "yeast", "warm water", "salt", "sugar", "groundnut oil", "margarine", "milk", "egg"]
    mPie = ["flour", "baking powder", "salt", "margarine", "meat", "butter", "egg", "beef", "onions", "potato", "carrot", "spices"]
    for idx, snack in enumerate(snacksList):
        print(idx,snack)
    snacksChoice = str(input("which of the snacks above do you wish to prepare?: ").upper)
    if snacksChoice in snacksList:
        if snacksChoice == "EGGROLL":
            recipe1 = str(input("give me one(1) main ingrdients to prepare it: ").lower())
            if recipe1 in eRoll:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score += 0
            recipe2 = str(input("give me another main ingredient to prepare it: ").lower())
            if recipe2 in eRoll and recipe2 not in playerList:
                playerList.append(recipe2)
                score += 1
                print (score)
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
        if snacksChoice == "DOUGHNUT":
            recipe1 = str(input("give me one(1) main ingredient to prepare it: ").lower())
            if recipe1 in dnurt:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score += 0
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
                winORlose()
#list for meat pie ingredient
        else:
            recipe1 = str(input("give me one(1) main ingredient to prepare it: ").lower())
            if recipe1 in mPie:
                playerList.append(recipe1)
                score = +1
            else:
                playerList.append(recipe1)
                score += 0
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
                winORlose()
            else:
                playerList.append(recipe5)
                score += 0 
                winORlose()
    else: #validation check in concordance to food list
        print("please input a snacks from the list displayed")
        snacks()
        
#ACCESS OR DENIAL TO STORE
def winORlose(score):
    print ("you got ",score," correctly")
    print ("here is your list: ",playerList)
    if score >= 3:
        print("CONGRATULATIONS, CHEF " + str(name).upper() + " YOU CAN HAVE THE KEY AND START COOKING")
    else:
        print("I'm sorry, you need to learn more to access the food store.")

#PLAYER DECIDING WHAT TO DO IN THE KITCHEN
def decisionMaking():
    choice= str(input("What do you want to prepare? FOOD/SNACKS: ").upper)
    if choice == "FOOD":
        food()
    elif choice == "SNACKS":
        snacks()
    else:
        print("please input the correct action")
        decisionMaking() 

decisionMaking()   