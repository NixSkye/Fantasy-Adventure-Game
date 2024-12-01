import time

def introduction():
    print("Welcome to the Fantasy Adventure Game!")
    print("You are a young hero on a quest to save the kingdom.")
    print("Your journey begins in a small village...")
    time.sleep(2)
    village()

def village():
    print("\nYou find yourself in a small village.")
    print("You can choose one of the following paths:")
    print("1. Venture into the enchanted forest.")
    print("2. Explore the mysterious cave.")
    print("3. Rest at the village inn.")
    print("4. Quit the game.")
    choice = input("What will you do? (1/2/3/4): ")

    if choice == "1":
        enchanted_forest()
    elif choice == "2":
        mysterious_cave()
    elif choice == "3":
        village_inn()
    elif choice == "4":
        quit_game()
    else:
        print("Invalid choice. Please select a valid option.")
        village()

def enchanted_forest():
    print("\nYou enter the enchanted forest, surrounded by mystical trees and creatures.")
    print("As you venture deeper, you come across a magical clearing with a sparkling pond.")
    print("What do you do?")
    print("1. Approach the sparkling pond.")
    print("2. Continue exploring the forest.")
    print("3. Return to the village.")
    choice = input("Your choice (1/2/3): ")

    if choice == "1":
        print("You approach the pond and feel a surge of energy.")
        print("You gain new strength and continue your journey.")
        time.sleep(2)
        village()
    elif choice == "2":
        print("You continue exploring the forest, uncovering its secrets.")
        print("suddenly you heard something")
        lyra()
        # Add more game content here
    elif choice == "3":
        print("You decide to return to the village.")
        time.sleep(2)
        village()
    else:
        print("Invalid choice. Please select a valid option.")
        enchanted_forest()

def mysterious_cave():
    print("\nYou enter the mysterious cave, and it's dark and damp inside.")
    print("You hear faint whispers echoing in the cave.")
    print("What do you do?")
    print("1. Investigate the whispers.")
    print("2. Leave the cave.")
    choice = input("Your choice (1/2): ")

    if choice == "1":
        print("You approach the whispers and.....")
        eldric()
    elif choice == "2":
        print("You decide to leave the cave.")
        time.sleep(2)
        village()
    else:
        print("Invalid choice. Please select a valid option.")
        mysterious_cave()

def village_inn():
    print("\nYou rest at the village inn and regain your strength.")
    print("The innkeeper shares tales of the kingdom's history and challenges.")
    print("You are now better prepared for your quest.")
    time.sleep(2)
    village()
def eldric():
    print('''Hey there!
It seems like I am not alone here!
Do you want to know a secret?''')
    c= input('''1. Yes
2. No
Your choice (1/2):''')
    if c== "1":
        print("Eldric the Mysterious:There is a hidden treasure in this cave. If you found it first, then you can have it all to yourself but if I found it, you won't get a single penny. Do you accept the challange?")
        c1= input('''1. Yes
2. No
Your choice (1/2): ''')
        if c1== "1":
            print('''Eldric the Mysterious: Thats the spirit
You tried hard and found the treasure box
Eldric the Mysterious: You WON!! You are really something traveller.''')
            print('Thank you')
            print("You take the treasure with you on your journey.")
            time.sleep(5)
            village_inn()
    elif c=="2":
        print("Eldric the Mysterious: as you wish Traveller")
    else:
        print("Invalid choice. Please select a valid option.")
        eldric()
        
def lyra():
    print("hey mate!")
    print('''Lyra the Enchantress: Greetings, brave traveler. I sense you seek a path through these enchanted woodlands. But beware, for the forest is filled with secrets and dangers. How may I assist you on your journey?''')
    choice = input('''1.Tell me about the forest's secrets.
2.Can you guide me safely through the forest?
3.I'll go on my own. Thanks.
Your choice (1/2/3): ''')

    if choice == "1":
        print("Lyra the Enchantress: Gladly traveller. ____________________")
        # Add more game content here
    elif choice =="2":
        print("Lyra the Enchantress: Sure traveller. Where do you want to go next?")
        print("1. Mysterious Cave")
        print("1. village inn")
        c = input("Your choice (1/2): ")
        if c== "1":
            mysterious_cave()
        elif c== "2":
            village_inn()
        else:
            print("Invalid choice. Please select a valid option.")
            lyra()
    elif choice == "3":
        time.sleep(2)
        print("Lyra the Enchantress: Happy Journey traveller!")
        village()
    else:
        print("Invalid choice. Please select a valid option.")
        mysterious_cave()
def quit_game():
    print("\nThank you for playing the Fantasy Adventure Game!")
    exit()

if __name__ == "__main__":
    introduction()
