
import animal_name_gen
import random
import os
from datetime import datetime
import sys


animal_name_file = open("./animal_name.txt")
animal_list = []
for line in animal_name_file:
    newline = line.replace("\n",'')
    animal_list.append(newline)
animal_name_file.close()



codes = [
    "HALBERT",
    "ZILLA",
    "THANKS"
]

animal_list = sorted(animal_list)

screen = "homescreen"
animals = []
ages = []
species = []
time_acquired = []
now = datetime.now()

shop_animals = []
shop_ages = []
shop_species = []
shop_cost = []
shop_data = []
shopagain = False
balance = 10000000

myZoo = [["n/a", "n/a", "n/a", "n/a"], ["n/a", "n/a", "n/a", "n/a"], ["n/a", "n/a", "n/a", "n/a"], ["n/a", "n/a", "n/a", "n/a"]]
available_animals = []
available_ages = []
available_species = []

idc = -1
#idc means id code

coordinate_x = 0
coordinate_y = 0

animal_name_gen.generate_animal_name()

def gen_anim():
    return animal_list[random.randint(0, len(animal_list)-1)]

def gen_shop():
    if inp != "order species":
        for namegen in range(random.randint(20, 300)):
            shop_animals.append(animal_name_gen.generate_animal_name())
            shop_ages.append(str(random.randint(1, 22)))
            shop_species.append(gen_anim())
            shop_cost.append(str(random.randint(30000, 2000000))) #30,000 and 2,000,000
    else:
        return None
    
def clear_console():
    os.system('clear')  # This clears the console in macOS and Linux


    
    

while True:
    if screen == "homescreen":

        print("Zooscape 0.1.0".center(100," "))
        
        print()
        

        print("Press [Enter] to play!".center(100," "))
        
        inp = input()
        
        screen = "play"
    
    if screen == "play":
        print("Welcome to Zooscape!\n\n")
        if animals == []:
            print("You have no animals. Enter 'shop' to view animals on sale!")
            print("Type other commands to go to other pages, now limited to you.")
            print("You will see more when you have animals. ")
            print("'codes' will let you enter codes")
            print("'animal book' will show your animal book directory")
            print("'shop' to view animals on sale")
            print("'exit' to exit the game")
            
            inp = input()
            if inp == "shop":
                screen = "shop"
            if inp == "animal book":
                screen = "animal book"
            if inp == "codes":
                screen = "codes"
            clear_console()
        else:
            print("There are many things to do in the zoo. Here are some of them")
            print("'shop' to view animals on sale")
            print("'zoo' will show your zoo")
            print("'codes' will let you enter codes")
            print("'animal book' will show your animal book directory")
            inp = input()
            if inp == "shop":
                screen = "shop"
            if inp == "zoo":
                screen = "zoo"
            if inp == "animal book":
                screen = "animal book"
            if inp == "codes":
                screen = "codes"
            if inp == "exit":
                quit()
            clear_console()
        
    
    if screen == "shop":
        gen_shop()
        if shop_animals == []:
            print("Sorry, we do not have any animals. Try again later.".center(100," "))
            print()
            screen = "homescreen"
        else:
            if shopagain == False: #new time
                print("Welcome to the Animal Shop!".center(100," "))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(100," "))
                print()
                print("You can do many things in shop. Here are the commands!")
                print("(buy item when asked) will get you an animal of your choice.")
                print("'order species' would order them by species. ")
                print("\n\nYou have $",("{:,}".format(int(balance))))
            else: #old time
                clear_screen()
            
            for i in range(len(shop_animals)):
                print("ID " + str(i) + ": " + (shop_animals[i]) + " (" + (shop_ages[i]) + " year old " + (shop_species[i]) + ") for $" + ("{:,}".format(int(shop_cost[i]))))
            print("What would'tchu like? Gimme the ID, please.")
            inp = input()
            clear_screen()
            if inp != "" or " ":
                
                
                
                if inp == "order species":
                    ordered_by_species = sorted(zip(shop_animals, shop_ages, shop_species), key=lambda x: x[2])
                    shop_animals, shop_ages, shop_species = zip(*ordered_by_species)

                    print("Animals ordered by species!")
                    
                    shopagain = True
                elif int(inp) >= 0 and int(inp) < len(shop_animals):
                    print("OK! I'll get it for ya.")
                    animals.append(shop_animals[int(inp)])
                    available_animals.append(shop_animals[int(inp)])
                    
                    ages.append(shop_ages[int(inp)])
                    available_ages.append(shop_ages[int(inp)])
                    
                    species.append(shop_species[int(inp)])
                    available_species.append(shop_species[int(inp)])
                    
                    balance -= int(shop_cost[int(inp)])
                    
                    
                    
                    idc += 1
                    print("ID " + str(idc) + ": " + (animals[idc]) + " (" + (ages[idc]) + ") is your very own " + (species[idc]) + "!")
                    print("\n\nYou have $",("{:,}".format(int(balance))))
                    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                    time_acquired.append(date_time)
        
                    shop_animals = list(shop_animals)
                    shop_ages = list(shop_ages)
                    shop_species = list(shop_species)
            
                    shop_animals.pop(int(inp))
                    shop_ages.pop(int(inp))
                    shop_species.pop(int(inp))
        
                    print("Anything else? (yes/no)")
                    inp = input()
                    if inp == "yes":
                        screen = "shop"
                        shopagain = True
                    else:
                        print("Come again!")
                        screen = "play"
            else:
                print("I can't find them. Maybe try again?")
                    
if screen == "zoo":
    for row in range(len(myZoo)):
        for column in range(len(myZoo[0])):
            print("[" + myZoo[row][column], end = "]\t\t")
        print()
        print()

    print("Do you want to add anything?")
    inp = input()
    if inp == "yes":
        print("Here are your animals:")
        for i in range(len(available_animals)):
            print("ID " + str(i) + "    " + available_animals[i] + " (" + available_ages[i] + "-year old " + available_species[i] + ")")
        inp = int(input("Which one to put? Give me the ID. \n"))
        find = inp
        
        # Check if the selected species matches the available species
        selected_species = available_species[find]
        matching_indices = [i for i, species in enumerate(available_species) if species == selected_species]
        
        if matching_indices:
            print("Now for the coordinates. ")
            coordinate_x, coordinate_y = map(int, input().split())
            if coordinate_x <= 0:
                coordinate_x = 1
            if coordinate_y <= 0:
                coordinate_y = 1

            print("Loading...")
            if myZoo[coordinate_x-1][coordinate_y-1] == "n/a":
                myZoo[coordinate_y-1][coordinate_x-1] = available_animals[find]
                available_animals.pop(find)
                available_ages.pop(find)
                available_species.pop(find)
            else:
                print("Sorry, that's occupied.")
                screen = "homescreen"
                screen = "zoo"

            for row in range(len(myZoo)):
                for column in range(len(myZoo[0])):
                    print("[" + myZoo[row][column], end = "]\t\t")
                print()
                print()
            
            print("More to add?")
            inp = input()
            if inp == "yes":
                screen = "homescreen"
            else:
                print("Okay, you will be brought back to the shop!")
                screen = "shop"
        else:
            print("Sorry, there are no available animals of the same species.")
            print("You will be brought back to the shop!")
            screen = "shop"
        
    else:
        print("Okay, you will be brought back to the shop!")
        screen = "shop"
    if screen == "animal book":
        print("Welcome to the Animal Book!")
        print("To see all available animals, type 'continue'. To see your animals, type 'my animal book'.")
        inp = input()
        if inp == "continue":
            print("Here are all " + str(len(animal_list)) + " available species!\n")
            for i in range(len(animal_list)):
                if animal_list[i] in species:
                    print(animal_list[i] + " is either in your zoo or is available to put there.")
                if animal_list[i] not in species:
                    print(animal_list[i] + " is yet to be bought.")
        else:
            screen = "my animal book"
    if screen == "my animal book":
        print("Here are your personal animals")
        for i in range(len(animals)):
            print("ID " + str(i) + " " + animals[i] + ", " + ages[i] + "-year old " + species[i])
        print("Give an ID number and you will get data on the animal. To exit, type exit twice. ")
        inp = input()
        if inp == "exit":
            screen = "play"
        else:
            print("----------------------------------------------------------------------------------------")
            print(animals[int(inp)] + "  (" + ages[int(inp)] +")\n" + species[int(inp)])
            print("This specimen was acquired on " + time_acquired[int(inp)] + ".")
            if animals[int(inp)] in available_animals:
                print("This specimen is available to put in your zoo. ")
            else:
                print("It's probably in your zoo. ")
            print("----------------------------------------------------------------------------------------")
    if screen == "codes":
        print("WELCOME TO CODES")
        print("Enter a code to get your reward!")
        print("Type 'help' for help!")
        
        inp = input()
        if inp == "help":
            print("Welcome to the Codes Help Page!")
            print("For questions on how to use, type '1'. ")
            inp = input()
            break
        if inp == "exit":
            screen = "homescreen"
        inp = inp.upper()
        print(inp)
        if inp in codes:
            if inp == "HALBERT":
                print("The original guy. ")
                animals.append("Halbert")
                species.append("Mountain Goat")
                ages.append("12")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                print("You have acquired Halbert (12-year old Mountain Goat)!")
                
            elif inp == "ZILLA":
                print("He's just a gila monster.")
                animals.append("Zilla")
                species.append("Gila Monster")
                ages.append("5")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                print("You have acquired Zilla (12-year old Gila Monster)!")
                
            elif inp == "THANKS":
                print("You're welcome!")
                print("You recived 100 dollars. ")
                balance += 100

        else:
            print("Sorry, that is not a valid code. ")
    if screen == "exit":
        print("Goodbye!")
        quit()
