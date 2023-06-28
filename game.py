#Name: Victoria
#Text-based Culinary testing game

print("WELCOME TO THE KITCHEN")
name= input("Enter your name: ")
print("Hello " + str(name))

#PLAYER DECIDING WHAT TO DO IN THE KITCHEN
def decisionMaking():
    choice= input("What do you want to prepare? food/snacks: ")
    if choice == "food":
        food()
    elif choice == "snacks":
        snacks()
    else:
        print("please input the correct action")
        decisionMaking() 

#FOOD FUNCTION
def food():
    foodList = ["jollof rice", "jollof spag", "yam & egg sauce"]
    jRice = ["rice", "water", "pepper", "salt", "tomato"]
    jSpag = ["spaghetti", "pepper", "salt", "seasoning", "tomato"]
    yamSauce = ["yam", "pepper", "egg", "water", "salt"]
    playerList = []
    score = 0
    for idx, meal in enumerate(foodList):
        print(idx,meal)
    foodChoice = input("which of the meal above do you wish to prepare?: ")
    if foodChoice in foodList:
    #Listing food recipe
        if foodChoice == "jollof rice":
            recipe1 = input("give me one(1) main recipe to prepare it: ")
            if recipe1 in jRice:
                playerList.append(recipe1)
                score += 1
            else:
                playerList.append(recipe1)
                score += 0
            recipe2 = input("give me another main recipe to prepare it: ")
            if recipe2 in jRice:
                playerList.append(recipe2)
                score += 1
            else:
                playerList.append(recipe2)
                score += 0
            recipe3 = input("give me another main recipe to prepare it: ")
            if recipe3 in jRice:
                playerList.append(recipe3)
                score += 1
            else:
                playerList.append(recipe3)
                score += 0
            recipe4 = input("give me another main recipe to prepare it: ")
            if recipe4 in jRice:
                playerList.append(recipe4)
                score += 1
            else:
                playerList.append(recipe4)
                score += 0
            recipe5 = input("give me another main recipe to prepare it: ")
            if recipe5 in jRice:
                playerList.append(recipe5)
                print(playerList)
                score += 1
            else:
                playerList.append(recipe5)
                score += 0
    else:
        print("please input a food from the list displayed")
        food()

#SNACKS FUNCTION
def snacks():
    snacksList = ["eggroll", "doughnurt", "mince pie"]
    eRoll = ["egg", "flour", "baking powder", "water", "flavour", "salt", "sugar", "groundnut oil", "butter"]
    dnurt = ["flour", "yeast", "warm water", "salt", "sugar", "groundnut oil", "butter"]
    mPie = ["flour", "baking powder", "salt", "butter", "water", "meat"]
    playerList = []
    for idx, snack in enumerate(snacksList):
        print(idx,snack)
    snacksChoice = input("which of the snacks above do you wish to prepare?: ")
    if snacksChoice == snacksList:
        pass
    else:
        print("please input a snacks from the list displayed")
        snacks()

decisionMaking()    