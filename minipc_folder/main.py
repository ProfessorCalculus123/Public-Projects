import os
import calculators
import games
import youtube
import chatbot
import security



def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear_console()
    while True:
        clear_console()
        print("______________________")
        print("MINI PC - MAIN MENU")
        print("1. Grade Calculators")
        print("2. Games")
        print("3. Youtube Analytics")
        print("4. Chat bot")
        print("5. Cyber Security Tools")
        print("6. Exit")
        print("_____________________")
        
        option = input("Enter option: ")
        
        if option == "1":
            clear_console()
            calculators.run()
        elif option == "2":
            clear_console()
            games.run()
            clear_console()
        elif option == "3":
            clear_console()
            youtube.run()
            clear_console()
        elif option == "4":
            clear_console()
            chatbot.run()
            clear_console()
        elif option == "5":
            clear_console()
            security.run()
            clear_console()
        elif option == "6":
            exit()

if __name__ == "__main__":
    menu()