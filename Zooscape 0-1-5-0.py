import random
import os
from datetime import datetime
import shutil
from colorama import Fore, Style
import animal_name_gen
import pandas as pd
from IPython.display import display
from time import sleep

def print_colored_centered_text(text, color_hex, font_style=None, end='\n'):
    # Get the width of the terminal
    terminal_width, _ = shutil.get_terminal_size()
    padding = (terminal_width - len(text)) // 2
    
    # Check if color_hex is a valid hexadecimal color code
    try:
        color_code = f"\033[38;2;{int(color_hex[0:2], 16)};{int(color_hex[2:4], 16)};{int(color_hex[4:], 16)}m"
    except ValueError:
        print("")
        return
    
    style_code = getattr(Style, font_style, "")
    
    print(" " * padding + f"{color_code}{style_code}{text}{Style.RESET_ALL}", end=end)
    
    
# Example usage
#print_colored_centered_text("Hello, World!", "FF0000", "BRIGHT", end = " ")


RUNNING_GAME = True

animal_list = []
f = open("./animal_name.txt")

for line in f:
    animal_list.append(line.replace("\n",''))
f.close()

# Completion Codes
# Green: Ready for testing, minor change needed
# Yellow: Minor bugs to fix
# Orange: Major bugs to fix / Still programming
# Red: Very Major bugs to fix / In progress of programming the framework
# Black: Generates big problem / Not even started

codes = [
    "HALBERT",
    "ZILLA",
    "THANKS",
    "PROMOBABIRUSA"
    "MONKEYTESTPACK"
    "POLERBEAR"
    "ELLIGETOR"
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
# IDentification Code

coordinate_x = 0
coordinate_y = 0

animal_name_gen.generate_animal_name()

visitors = 0
vchild = 0
vadult = 0
vsenior = 0
vveteran = 0
vinfant = 0
#v = visitors that are ...
child_cost = 2.00
adult_cost = 5.00
senior_cost = 3.00
veteran_cost = 2.00
infant_cost = 0.50

caunter = 0

famalies = 0
def gen_anim():
    return animal_list[random.randint(0, len(animal_list)-1)]

def gen_shop():
    if inp != "order species":
        for namegen in range(random.randint(20, 300)):
            shop_animals.append(animal_name_gen.generate_animal_name())
            shop_ages.append(str(random.randint(1, 22)))
            shop_species.append(gen_anim())
            shop_cost.append(str(random.randint(10000, 2000000)))
    else:
        return None
    
while RUNNING_GAME:
    if screen == "homescreen":
        print_colored_centered_text("Zooscape 0.1.5.0", "90A02D", "BRIGHT")
        print()
        sleep(3)
        print_colored_centered_text("Press [Enter] to play!", "705414", "BRIGHT")
        inp = input()
        screen = "play"
    if screen == "play":
        print_colored_centered_text("Welcome to Zooscape!", "7CCF1D", "BRIGHT")
        sleep(2)
        if animals == []:
            print_colored_centered_text("You have no animals. Enter 'shop' to view animals on sale!", "7CCF1D", "BRIGHT")
            sleep(3)
        else:
            print_colored_centered_text("There are many things to do in the zoo. Here are some of them.", "7CCF1D", "BRIGHT")
            sleep(3)
            
        print_colored_centered_text("Type other commands to go to other pages!", "71BC1B", "BRIGHT")
        sleep(3)
        print_colored_centered_text("'shop' to view animals on sale,", "65A817", "BRIGHT")
        sleep(0.5)
        print_colored_centered_text("'zoo' will show your zoo,", "548D12", "BRIGHT")
        sleep(0.5)
        print_colored_centered_text("'codes' will let you enter codes,", "43700F", "BRIGHT")
        sleep(0.5)
        print_colored_centered_text("'animal book' shows your animal book directory,", "30510B", "BRIGHT")
        sleep(0.5)
        print_colored_centered_text("'genetic lab' lets you fuse animals together,", "50D1B5", "BRIGHT") #light bloo
        sleep(0.5)
        print_colored_centered_text("'cell shop' to view the cells you can buy,", "13ADB8", "BRIGHT") #azoor bloo
        sleep(0.5)
        print_colored_centered_text("'credits/licenses' shows all the credits of this game, as well as any licenses this game has,", "13ADB8", "BRIGHT") #azoor bloo
        sleep(0.5)
        print_colored_centered_text("and finally, 'exit' will exit your current game, as well as terminating the data. ", "000000", "BRIGHT")
        
        inp = input()
        if inp == "shop":
            screen = "shop"
                
        if inp == "animal book":
            screen = "animal book"
                
        if inp == "codes":
            screen = "codes"
                
        if inp == "cell shop":
            screen = "cellshop"
                
        if inp == "genetic lab":
            screen = "genetic lab"

        if inp == "zoo":
            screen = 'zoo'
            
        if inp == "credits/licenses":
            screen = 'credits'
                
        if inp == "exit":
            print_colored_centered_text("Goodbye! We hope to see you again!", "705414", "BRIGHT")
            RUNNING_GAME = False
                
    
    if screen == "shop":
        gen_shop()
        if shop_animals == []: # very impossible case. here just in case if you hecked me
            print_colored_centered_text("Sorry, we do not have any animals. Try again later.", "A0D832", "BRIGHT")
            sleep(3)
            # you probably hecked me. That ain't nice to us. 
            print()
            screen = "homescreen"
        else:
            if shopagain == False: # Just started shopping. 
                print_colored_centered_text("Welcome to the Animal Shop!", "D8B78A", "BRIGHT")
                sleep(2)
                print_colored_centered_text("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "D8B78A", "BRIGHT")
                sleep(0.5)
                print()
                print_colored_centered_text("You can do many things in shop. Here are the commands!", "05C15D", "BRIGHT")
                sleep(0.5)
                print_colored_centered_text("(buy item when asked) will get you an animal of your choice.", "17A359", "BRIGHT")
                sleep(0.5)
                print_colored_centered_text("'order species' will order them by species. ", "1A8E51", "BRIGHT")
                sleep(0.5)
                formatted_balance = str("{:,}".format(int(balance)))
                print("\n\n")
                you_have_balance = "You have $"+formatted_balance
                print_colored_centered_text(you_have_balance, "FFF13E", "BRIGHT")
                sleep(0.5)
                
            else:
                print()
                print()
            print_colored_centered_text("What would'tchu like? Gimme the ID, please.", "A0D832", "BRIGHT")
            sleep(4.5)
            shopdict = {'Name': shop_animals, 'Age': shop_ages, 'Species': shop_species, 'Cost': shop_cost}
            chart = pd.DataFrame(data=shopdict)
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            #chart_sorted = chart.sort_values(by='Species')
            #chart_sorted.reset_index(drop=True, inplace=True)
            #chart_sorted.index += 1
            display(chart)
            
            inp = input()
            if inp != "" or " ":
                if inp == "exit":
                    print_colored_centered_text("Have a nice day!", "A0D832", "BRIGHT")
                    sleep(2.5)
                    screen = "homescreen"
                if int(inp) >= 0 and int(inp) < len(shop_animals):
                    #else:
                    print_colored_centered_text("OK! I'll get it for ya.", "A0D832", "BRIGHT")
                    sleep(3.5)
                        
                    animals.append(shop_animals[int(inp)])
                    available_animals.append(shop_animals[int(inp)])
                        
                    ages.append(shop_ages[int(inp)])
                    available_ages.append(shop_ages[int(inp)])
                        
                    species.append(shop_species[int(inp)])
                    available_species.append(shop_species[int(inp)])

                        
                    balance -= int(shop_cost[int(inp)])
                        
                    idc += 1
                    print("ID " + str(idc) + ": " + (animals[idc]) + " (" + (ages[idc]) + ") is your very own " + (species[idc]) + "!")
                    formatted_balance = str("{:,}".format(int(balance)))
                    print("\n\n")
                    you_have_balance = "You have $"+formatted_balance
                    print_colored_centered_text(formatted_balance, "8AB173", "BRIGHT")
                    sleep(0.5)
                    
                    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                    time_acquired.append(date_time)
        
                    shop_animals = list(shop_animals)
                    shop_ages = list(shop_ages)
                    shop_species = list(shop_species)
        
                    shop_animals.pop(int(inp))
                    shop_ages.pop(int(inp))
                    shop_species.pop(int(inp))
                    shop_cost.pop(int(inp))
            
                    print_colored_centered_text("Anything else? (yes/no)", "A0D832", "BRIGHT")
                    sleep(4)
            
                    inp = input()
                    if inp == "yes":
                        screen = "shop"
                        shopagain = True
                            
                    else:
                        print_colored_centered_text("Come again!", "A0D832", "BRIGHT")
                        sleep(1.5)
                        screen = "play"
                            
                else:
                    #print("I can't find them. Maybe try again?")
                    print_colored_centered_text("I didn't quite catch that. Maybe try again?", "A0D832", "BRIGHT")
                    sleep(4.5)
                          
    if screen == "zoo":
        max_length = max(len(name) for row in myZoo for name in row)
        for row in range(len(myZoo)): #len myzoo is replacement for rows because this autism is no like jupyter
            for col in range(len(myZoo[0])):
                padding = max_length - len(myZoo[row][col])
                print("[{}]".format(myZoo[row][col]) + " " * padding, end=" ")
                sleep(0.5)
            print()
            sleep(0.5)
                
            print()
        
        print_colored_centered_text("Do you want to add anything? Type yes. If you want to look at the statistics of the visitors, type see visitors.", "E39F2B", "BRIGHT")

        
        inp = input()

        if inp == "see visitors":
            famalies = random.randint(10,1000)
            print(famalies)
            for i in range(famalies):
                caunter += random.randint(0,3)
            vchild = caunter
            caunter = 0
            
            vadult = random.randint(10,1000)+famalies*2
            vsenior = random.randint(0,20)
            vveteran = random.randint(10,100)
            for i in range(famalies):
                caunter += random.randint(0,3)
            vinfant = caunter
            caunter = 0
            
            visitors = vchild + vadult + vsenior + vveteran + vinfant
            print_colored_centered_text("You have " + str(visitors)+ ".", "FF5733", "BRIGHT")
            print_colored_centered_text(str(vchild)+" of them are children", "F4DE01", "BRIGHT")
            print_colored_centered_text(str(vadult)+" of them are adults", "09B6D2", "BRIGHT")
            print_colored_centered_text(str(vsenior)+" of them are seniors", "FF5733", "BRIGHT")
            print_colored_centered_text(str(vveteran)+" of them are veterans", "F4DE01", "BRIGHT")
            print_colored_centered_text(str(vinfant)+" of them are infants", "09B6D2", "BRIGHT")
            revenue = (vchild*child_cost) + (vadult*adult_cost) + (vsenior*senior_cost) + (vveteran*veteran_cost) + (vinfant*infant_cost)
            print_colored_centered_text("You have earned "+str(revenue), "FF5733", "BRIGHT")
            balance += revenue
            revenue = 0

            print_colored_centered_text("Do you want to change the cost of a ticket?", "75D22E", "BRIGHT")
            inp = input()
            if inp == "yes":
                print_colored_centered_text("Which do you want to change?", "B0D695", "BRIGHT")
                
                print_colored_centered_text("Infant Ticket", "99D969", "BRIGHT")
                print_colored_centered_text("Child Ticket", "86C15A", "BRIGHT")
                print_colored_centered_text("Adult Ticket", "71A34C", "BRIGHT")
                print_colored_centered_text("Senior Ticket", "5F8840", "BRIGHT")
                print_colored_centered_text("Veteran Ticket", "486C2E", "BRIGHT")

                inp = input()

                if inp == "infant":
                    print_colored_centered_text("Type the new cost of a ticket. ", "C8BC6C", "BRIGHT")
                    inp = int(input())
                    infant_cost = int(input())
                    print_colored_centered_text("An easy way to get money, but that's daylight robbery!", "C8B26C", "BRIGHT")
                if inp == "child":
                    print_colored_centered_text("Type the new cost of a ticket. ", "C8BC6C", "BRIGHT")
                    inp = int(input())
                    child_cost = int(input())
                    print_colored_centered_text("An easy way to get money, but that's daylight robbery!", "C8B26C", "BRIGHT")
                if inp == "adult":
                    print_colored_centered_text("Type the new cost of a ticket. ", "C8BC6C", "BRIGHT")
                    inp = int(input())
                    adult_cost = int(input())
                    print_colored_centered_text("An easy way to get money, but that's daylight robbery!", "C8B26C", "BRIGHT")
                if inp == "senior":
                    print_colored_centered_text("Type the new cost of a ticket. ", "C8BC6C", "BRIGHT")
                    inp = int(input())
                    senior_cost = int(input())
                    print_colored_centered_text("An easy way to get money, but that's daylight robbery!", "C8B26C", "BRIGHT")
                if inp == "veteran":
                    print_colored_centered_text("Type the new cost of a ticket. ", "C8BC6C", "BRIGHT")
                    inp = int(input())
                    veteran_cost = int(input())
                    print_colored_centered_text("An easy way to get money, but that's daylight robbery!", "C8B26C", "BRIGHT")
            else:
                print_colored_centered_text("I guess the cost is going to be the way it is right now...", "B6983B", "BRIGHT")
                
            
        if inp == "yes":
            print_colored_centered_text("Here are your animals:", "F3C575", "BRIGHT")
            sleep(2.5)
            
            for i in range(len(available_animals)):
                print("ID " + str(i) + "    " + available_animals[i] + " (" + available_ages[i] + "-year old " + available_species[i] + ")")
                sleep(0.07)
            inp = int(input("Which one to put? Give me the ID. \n"))
            sleep(4)
            
            find = inp
            print_colored_centered_text("Now for the coordinates. ", "E39F2B", "BRIGHT")
            
            coordinate_x, coordinate_y = map(int, input().split())
            if coordinate_x <= 0:
                coordinate_x = 1
                if coordinate_y <= 0:
                    coordinate_y = 1
            
            print_colored_centered_text("Loading...", "F3C575", "BRIGHT")
            sleep(random.randint(1,10))
            
            if myZoo[coordinate_x-1][coordinate_y-1] == "n/a":
                myZoo[coordinate_y-1][coordinate_x-1] = available_species[find]
                available_animals.pop(find)
                available_ages.pop(find)
                available_species.pop(find)
            else:
                print_colored_centered_text("Sorry, that's occupied.", "B9852B", "BRIGHT")
                sleep(3.5)
                
                screen = "homescreen"
                screen = "zoo"
            
            
            fmax_length = max(len(name) for row in myZoo for name in row)
            for row in range(len(myZoo)): #len myzoo is replacement for rows because this autism is no like jupyter
                for col in range(len(myZoo[0])):
                    padding = max_length - len(myZoo[row][col])
                    print("[{}]".format(myZoo[row][col]) + " " * padding, end=" ")
                    sleep(0.5)
                print()
                sleep(0.5)
                
            print()
            print_colored_centered_text("More to add?", "E39F2B", "BRIGHT")
            sleep(2)
            
            inp = input()
            if inp == "yes":
                screen == "homescreen"
                screen == "zoo"
            else:
                print_colored_centered_text("Okay, you will be brought back to the homescreen!", "E39F2B", "BRIGHT")
                sleep(2.5)
                screen = "play"
        else:
            print_colored_centered_text("Okay, you will be brought back to the homescreen!", "E39F2B", "BRIGHT")
            sleep(2.5)
            
            screen = "play"
    if screen == "animal book":
        print_colored_centered_text("Welcome to the Animal Book!", "2BB9B7", "BRIGHT")
        sleep(2.7)
        print_colored_centered_text("To see all available animals, type 'continue'. To see your animals, type 'my animal book'.", "3CDEDC", "BRIGHT")
        sleep(5)
        
        inp = input()
        if inp == "continue":
            print_colored_centered_text("Here are all " + str(len(animal_list)) + " available species!\n", "1A9897", "BRIGHT")
            sleep(4.5)
    
            for i in range(len(animal_list)-1):
                if animal_list[i] in species:
                    print_colored_centered_text(animal_list[i] + " Seen Before or Bought ---", "AEF926", "BRIGHT")
                    sleep(0.05)
                    
                else:
                    print_colored_centered_text(animal_list[i] + " Not Bought or Seen --- ", "F94D26", "BRIGHT")
                    sleep(0.05)

        else:
            screen = "my animal book"
    if screen == "my animal book":
        print_colored_centered_text("Here are your personal animals:", "1A9897", "BRIGHT")
        sleep(2.8)
        
        for i in range(len(animals)):
            print("ID " + str(i) + " " + animals[i] + ", " + ages[i] + "-year old " + species[i])
            sleep(0.081653)
        print_colored_centered_text("Give an ID number and you will get data on the animal. To exit, type exit. ", "2BB9B7", "BRIGHT")
        sleep(2)
        
        inp = input()
        if inp == "exit":
            screen = "play"
        else:
            print_colored_centered_text("----------------------------------------------------------------------------------------", "B4FA00", "BRIGHT")
            sleep(0.5)
            print_colored_centered_text(animals[int(inp)] + "  (" + ages[int(inp)] +")\n" + species[int(inp)], "A9E217", "BRIGHT")
            sleep(0.5)
            print_colored_centered_text("This specimen was acquired on " + time_acquired[int(inp)] + ".", "91C114", "BRIGHT")
            sleep(0.5)
            
            if animals[int(inp)] in available_animals:
                print_colored_centered_text("This specimen is available to put in your zoo. ", "70960E", "BRIGHT")
                sleep(0.5)
                
            else:
                print_colored_centered_text("It's probably in your zoo. ", "70960E", "BRIGHT")
                sleep(0.5)
                
            
            print_colored_centered_text("----------------------------------------------------------------------------------------", "B4FA00", "BRIGHT")
            sleep(0.5)
            
    if screen == "codes":
        print_colored_centered_text("Welcome to the codes page. Are you ready to hack the promotional content, the good free money, and the good little free items?", "328191", "BRIGHT")
        sleep(0.1)
        inp = input("// ")
        inp = inp.upper()
        if inp == "EXIT":
                screen = "play"
                
        if inp in codes:
                
            if inp == "HALBERT":
                print_colored_centered_text("The original guy. ", "EA5D0F", "BRIGHT")
                sleep(2)
                
                animals.append("Halbert")
                species.append("Mountain Goat")
                ages.append("12")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                
                print_colored_centered_text("You have acquired Halbert (12-year old Mountain Goat)!", "F59C6A", "BRIGHT")
                
                codes.remove("HALBERT")
                
            elif inp == "ZILLA":
                print_colored_centered_text("he's just a gila monster.", "464CC1", "BRIGHT")
                
                animals.append("Zilla")
                species.append("Gila Monster")
                ages.append("5")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                
                print_colored_centered_text("You have acquired Zilla (5-year old Gila Monster)!", "6A71F5", "BRIGHT")
                
                codes.remove("ZILLA")
                
            elif inp == "THANKS":
                
                print_colored_centered_text("You're welcome!", "FDC100", "BRIGHT")
                print_colored_centered_text("You recieved 100 dollars.", "FFE48B", "BRIGHT")
                
                balance += 100
                codes.remove("THANKS")
            
            elif inp == "PROMOBABIRUSA":
                print_colored_centered_text("Sunday the Babirusa is here to brighten your day!", "E44BE2", "BRIGHT")
                
                animals.append("Sunday")
                species.append("Sulawesian Babirusa")
                ages.append("7")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                
                print_colored_centered_text("You have acquired Sunday (7-year old Sulawesian Babirusa)!", "FEBDFD", "BRIGHT")
                
                codes.remove("PROMOBABIRUSA")
                
            elif inp == "MONKEYTESTPACK":
                print_colored_centered_text("Monkeys seem to enjoy pananas.", " F0F628 ", "BRIGHT")
                
                animals.append("Colubo")
                species.append("Colubus Monkey")
                ages.append("2")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                
                animals.append("Fraz")
                species.append("Blue-Eyed Black Lemur/East Javan Langur Hybrid")
                ages.append("16")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                
                animals.append("Elkhouri")
                species.append("Probiscus Monkey")
                ages.append("41261208")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                
                animals.append("Beppi")
                species.append("Purple? Uakari Monkey")
                ages.append("3")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                
                print_colored_centered_text("You have acquired The Monkey Test Pack (Monkeys with variable ages)!", "F6D128", "BRIGHT")
                
                codes.remove("MONKEYTESTPACK")

            elif inp == "LE OLDE TIMERS":
                print_colored_centered_text("It's the oldies. ", " FF0000 ", "BRIGHT")
                
                animals.append("Mr. Nibbles")
                species.append("Megalodon")
                ages.append("1")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)

                animals.append("Trexxy")
                species.append("Tyrannosaurus rex")
                ages.append("1")
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                time_acquired.append(date_time)
                
                print_colored_centered_text("You have acquired The Monkey Test Pack (Monkeys with variable ages)!", "F6D128", "BRIGHT")
                
                codes.remove("MONKEYTESTPACK")
                
        elif not inp == "EXIT":
            print_colored_centered_text("Sorry, that is not a valid code. ", "705414", "BRIGHT")
    if screen == "cellshop":
        pass
        # cellshop code
    
    if screen == "genetic lab":
        print_colored_centered_text("Hello, I see that you are interested in this scientific breakthrough of mine?", "D0F5ED", "BRIGHT")
        sleep(3)
        print_colored_centered_text("Certainly, I can let you use the Genetic Module of the Animal Phaser.", "B5EFE2", "BRIGHT")
        sleep(2)
        print_colored_centered_text("Well, just type in the first animal you want to use, and the list of your cells and the basic cells I provide will be listed out. \nJust take a step back and let the machine work its magic.", "98DFCF", "BRIGHT")
        sleep(1)
        for i in range(len(animals)):
            print_colored_centered_text("ID "+str(i)+": "+animals[i]+"("+ages[i]+"-year old "+species[i]+")","46C3A7", "BRIGHT")
            sleep(0.07)
        inp = input()
        if inp == 'exit':
            print_colored_centered_text("But don't you want to try out the new technology?", "98DFCF", "BRIGHT")
            sleep(3)
            print_colored_centered_text("aww shucks. I wanted some test subjects.", "98DFCF", "BRIGHT")
            sleep(2.7)
            screen = "play"
        inp = int(inp)
        geneticmod1_animal = animals[inp]
        geneticmod1_ages = ages[inp]
        geneticmod1_species = species[inp]
        i1 = inp
        print_colored_centered_text("Great! Now just input your second animal!", "98DFCF", "BRIGHT")
        inp = int(input())
        geneticmod2_animal = animals[inp]
        geneticmod2_ages = ages[inp]
        geneticmod2_species = species[inp]
        i2 = inp
        print_colored_centered_text("*rrrmmmm...*", "98DFCF", "BRIGHT")
        sleep(3)
        print_colored_centered_text("*ca-pam...*", "98DFCF", "BRIGHT")
        sleep(3)
        print_colored_centered_text("*klec...*", "98DFCF", "BRIGHT")
        sleep(3)
        print_colored_centered_text("*clack clack clack clack CLACK CLACK CLACKETY CLACKET clack... clac...clack*", "98DFCF", "BRIGHT")
        sleep(3)
        print_colored_centered_text("*v m m m m m*", "98DFCF", "BRIGHT")
        sleep(3)
        print_colored_centered_text("*rrrmmmm...*", "98DFCF", "BRIGHT")
        sleep(3)
        print_colored_centered_text("It's done!", "98DFCF", "BRIGHT")
        sleep(1.34)
        combined_name = (animal_list[animal_list.index(geneticmod1_species)])+'-'+(animal_list[animal_list.index(geneticmod2_species)])+' hybrid'
        print_colored_centered_text("You have created a "+combined_name+". Don't you feel happy?", "98DFCF", "BRIGHT")
        sleep(3)
        print_colored_centered_text("It's name is "+animals[i1]+"/"+animals[i2]+".","98DFCF","BRIGHT")
        newname_fusion = animals[i1]+"/"+animals[i2]
        averageAge = round((ages[i1]+ages[i2])/2)
        print_colored_centered_text("The monstrosity is "+str(averageAge)+" years old..","98DFCF","BRIGHT")
        animals.pop(animals.index(animals[i1]))
        animals.pop(animals.index(animals[i2]))
        ages.pop(ages.index(animals[i1]))
        ages.pop(ages.index(animals[i2]))
        species.pop(animals.index(animals[i1]))
        species.pop(animals.index(animals[i2]))

        animals.append(newname_fusion)
        ages.append(averageAge)
        species.append(combined_name)
        screen = "play"

    if screen == "credits":
        print_colored_centered_text("Zooscape", "81C415", "BRIGHT")
        print_colored_centered_text("Zooscape 0.1.5.0, Uguisu Ubuntu Version", "69A011", "BRIGHT")
        print_colored_centered_text("Lead Developer: pbthecoder (https://github.com/pbthecoder)", "9FC85E", "LIGHT")
        print_colored_centered_text("Licenses", "85C41F", "BRIGHT")
        print_colored_centered_text("Zooscape 0.1.5.0 © 2024 by pbthecoder is licensed under CC BY-NC-SA 4.0. You can see a copy of this here: (https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1)", "85C41F", "LIGHT")
        screen = "play"
