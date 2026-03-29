import os
import random
import time
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")




def games():
    def coin_flip():
        global exit_choice, app
        app = 5
        while True:
            print("Coin Flip")
            input("Press Enter To Flip Coin ")

            coin = ["Heads", "Tails"]
            result = random.choice(coin)
            print("_________")
            print(result)
            print("_________")
            
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    def RPS():
        global exit_choice, app
        app = 6
        while True:
            print("Rock Paper Scissors")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")

            try:
                player = int(input("Select ROCK PAPER SCISSORS using (1-3): "))
            except ValueError:
                clear_console()
                print("INVALID INPUT, PLEASE START AGAIN")
                continue
            
            clear_console()

            if player == 1:
                hand = "Rock"
            elif player == 2:
                hand = "Paper"
            elif player == 3:
                hand = "Scissors"
            else:
                print("RESULT", player, " IS NOT VALID, PLEASE START AGAIN")
                continue

            npc = ["Rock", "Paper", "Scissors"]
            result = random.choice(npc)

            if hand == result:
                print("Draw")
            elif (
                hand == "Rock" and result == "Scissors"
                or hand == "Scissors" and result == "Paper"
                or hand == "Paper" and result == "Rock"
            ):
                print("You win")
            else:
                print("You lose")

            print("_________")
            print("PC choose " + result)
            print("_________")
            
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    def RLGL():
        def Classic():
            while True:
                input("Press Enter to Start")
                start_time = time.time()
                distance = 50
                state = "continue"

                while state == "continue":
                    # Red light block
                    print("greenlight")
                    timer = random.randint(2, 7)
                    starttimer = time.time()
                    
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= timer:
                            break
                        
                        time_passed = current_time - start_time
                        print(round(120 - time_passed), " sec left")
                        if time_passed > 120:
                            state = "game_over"
                            break
                            
                        move = input("")
                        if move == "w":
                            clear_console()
                            distance -= 0.5
                            if distance <= 0:
                                state = "win"
                                break
                            print(distance, "m")
                    
                    if state != "continue": break
                    clear_console()

                    if distance <= 0:
                        state = "win"
                        break
                    
                    # Green light block
                    print("redlight")
                    starttimer = time.time()
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= 3:
                            break
                        move = input("")
                        if move == "w":
                            state = "game_over"
                            break
                            
                    if state != "continue": break
                    clear_console()

                clear_console()
                while True:
                    if state == "win":
                        print("_____________\nYOU WIN")
                    else:
                        print(f"_____________\nGAME OVER\n{distance}m remaining")
                        
                    print("1.Retry\n2.Exit\n_____________")
                    game_state = input("Choose an option 1-2: ")
                    if game_state in ['1', '2']: 
                        break
                    clear_console()
                    
                if game_state == '1':
                    clear_console()
                    continue
                else:
                    clear_console()
                    break

        def Unlimited():
            while True:
                input("Press Enter to Start")
                start_time = time.time()
                distance = 0
                state = "continue"

                while state == "continue":
                    print("greenlight")
                    timer = random.randint(1, 15)
                    starttimer = time.time()
                    
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= timer:
                            break
                            
                        move = input("")
                        if move == "w":
                            clear_console()
                            distance += 0.5
                            print(distance, "m")
                    
                    if state != "continue": break
                    clear_console()

                    print("redlight")
                    starttimer = time.time()
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= 3:
                            break
                        move = input("")
                        if move == "w":
                            state = "game_over"
                            break
                            
                    if state != "continue": break
                    clear_console()

                clear_console()
                while True:
                    print(f"_____________\nGAME OVER\n{distance}m traveled")
                    print("1.Retry\n2.Exit\n_____________")
                    game_state = input("Choose an option 1-2: ")
                    if game_state in ['1', '2']: 
                        break
                    clear_console()
                    
                if game_state == '1':
                    clear_console()
                    continue
                else:
                    clear_console()
                    break

        def Mystery():
            while True:
                input("Press Enter to Start")
                start_time = time.time()
                distance = 50
                state = "continue"

                while state == "continue":
                    print("greenlight")
                    timer = random.randint(2, 7)
                    starttimer = time.time()
                    
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= timer:
                            break
                        
                        time_passed = current_time - start_time
                        if time_passed > 100:
                            state = "game_over"
                            break
                            
                        move = input("")
                        if move == "w":
                            clear_console()
                            distance -= 0.5
                            if distance <= 0:
                                state = "win"
                                break
                            print(distance, "m")
                    
                    if state != "continue": break
                    clear_console()

                    if distance <= 0:
                        state = "win"
                        break
                    
                    print("redlight")
                    starttimer = time.time()
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= 3:
                            break
                        move = input("")
                        if move == "w":
                            state = "game_over"
                            break
                            
                    if state != "continue": break
                    clear_console()

                clear_console()
                while True:
                    if state == "win":
                        print("_____________\nYOU WIN")
                    else:
                        print(f"_____________\nGAME OVER\n{distance}m remaining")
                        
                    print("1.Retry\n2.Exit\n_____________")
                    game_state = input("Choose an option 1-2: ")
                    if game_state in ['1', '2']: 
                        break
                    clear_console()
                    
                if game_state == '1':
                    clear_console()
                    continue
                else:
                    clear_console()
                    break

        def Practice():
            while True:
                input("Press Enter to Start")
                distance = 5
                clear_console()
                state = "continue"

                while state == "continue":
                    print("greenlight")
                    timer = random.randint(2, 7)
                    starttimer = time.time()
                    
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= timer:
                            break
                            
                        move = input("")
                        if move == "w":
                            clear_console()
                            distance -= 0.5
                            if distance <= 0:
                                state = "win"
                                break
                            print(distance, "m")
                    
                    if state != "continue": break
                    clear_console()

                    if distance <= 0:
                        state = "win"
                        break
                    
                    print("redlight")
                    starttimer = time.time()
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= 3:
                            break
                        move = input("")
                        if move == "w":
                            state = "game_over"
                            break
                            
                    if state != "continue": break
                    clear_console()

                clear_console()
                while True:
                    if state == "win":
                        print("_____________\nYOU WIN")
                    else:
                        print(f"_____________\nGAME OVER\n{distance}m remaining")
                        
                    print("1.Retry\n2.Exit\n_____________")
                    game_state = input("Choose an option 1-2: ")
                    if game_state in ['1', '2']: 
                        break
                    clear_console()
                    
                if game_state == '1':
                    clear_console()
                    continue
                else:
                    clear_console()
                    break

        def Rage():
            while True:
                input("Press Enter to Start")
                start_time = time.time()
                distance = 100
                state = "continue"

                while state == "continue":
                    print("Not Redlight")
                    timer = random.randint(1, 3)
                    starttimer = time.time()
                    
                    while True:
                        current_time = time.time()
                        if current_time - starttimer >= timer:
                            break
                        
                        time_passed = current_time - start_time
                        print(round(240 - time_passed), " sec left")
                        if time_passed > 240:
                            state = "game_over"
                            break
                            
                        move = input("")
                        if move == "w":
                            clear_console()
                            distance -= 0.5
                            if distance <= 0:
                                state = "win"
                                break
                            print(distance, "m")
                    
                    if state != "continue": break
                    clear_console()

                    if distance <= 0:
                        state = "win"
                        break
                    
                    print("Not greenlight")
                    starttimer = time.time()
                    while True:
                        current_time = time.time()
                        if int(current_time - starttimer) >= 1.5:
                            break
                        move = input("")
                        if move == "w":
                            state = "game_over"
                            break
                            
                    if state != "continue": break
                    clear_console()

                clear_console()
                while True:
                    if state == "win":
                        print("_____________\nYOU WIN")
                    else:
                        print(f"_____________\nGAME OVER\n{distance}m remaining")
                        
                    print("1.Retry\n2.Exit\n_____________")
                    game_state = input("Choose an option 1-2: ")
                    if game_state in ['1', '2']: 
                        break
                    clear_console()
                    
                if game_state == '1':
                    clear_console()
                    continue
                else:
                    clear_console()
                    break

        def modes():
            while True:
                print("__________RLGL__________")
                print("GAME MODES:")
                print("1. Classic")
                print("2. Unlimited")
                print("3. Mystery")
                print("4. Practice")
                print("5. Blood Bath")
                print("6. Exit")
                print("__________RLGL__________")
                gamemode = input("Choose a game mode 1-6: ")
                try:
                    gamemode_int = int(gamemode)
                except ValueError:
                    clear_console()
                    continue
                
                if gamemode_int == 1:
                    clear_console()
                    Classic()
                elif gamemode_int == 2:
                    clear_console()
                    Unlimited()
                elif gamemode_int == 3:
                    clear_console()
                    Mystery()
                elif gamemode_int == 4:
                    clear_console()
                    Practice()
                elif gamemode_int == 5:
                    clear_console()
                    Rage()
                elif gamemode_int == 6:
                    clear_console()
                    break
                else:
                    clear_console()

        def rules():
            print("RULES")
            print("Welcome to Redlight Greenlight!")
            print("The game that tests your speed, reflexes, and more.\n")

            print("Controls:")
            print("Enter 'w' into the console and press 'Enter' to move forward.")
            print("If you move during a red light, you will lose.")
            print("Press 'Enter' to keep still during the red light phase.")
            print("If you don't, you will run out of time.\n")

            print("Game Modes:")
            print("1. Classic: You have 120 seconds to get to the other side without being caught during the red light phase.")
            print("2. Unlimited: See how far you can travel without getting caught.")
            print("3. Mystery: Same as Classic, but the timer is hidden.")
            print("4. Practice: Same as Classic, but untimed.")
            print("5. Bloodbath: Twice the length, twice the danger and twice the difficulty\n ")

            print("I hope you enjoy the game!")
            input("press enter to exit")
            clear_console()

        while True:
            print("__________RLGL__________")
            print("Menu:")
            print("1. Play Game")
            print("2. Rules")
            print("3. Exit")
            print("__________RLGL__________")
            gamemode = input("Choose a game mode 1-3: ")
            try:
                gamemode_int = int(gamemode)
            except ValueError:
                clear_console()
                continue
            
            if gamemode_int == 1:
                clear_console()
                modes()
            elif gamemode_int == 2:
                clear_console()
                rules()
            elif gamemode_int == 3:
                clear_console()
                break
            else:
                clear_console()

    while True:
        print("______________________________")
        print("Games")
        print("1. Coin Flipper")
        print("2. RPS")
        print("3. Red Light | Green Light")
        print("4. Exit")
        print("______________________________")
        option = input("Choose Option (1-4): ")
        clear_console()
        print("\n\n")
        try:
            option_int = int(option)
        except ValueError:
            clear_console()
            continue
        
        if option_int == 1:
            clear_console()
            coin_flip()
        elif option_int == 2:
            clear_console()
            RPS()
        elif option_int == 3:
            clear_console()
            RLGL()
        elif option_int == 4:
            clear_console()
            break
        else:
            clear_console()
