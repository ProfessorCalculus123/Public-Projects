# Welcome to the MINI PC - I created the MINI PC as an efficient method to store my programming scripts
# I Dante Rosini under the MIT Licence permit all personal use of this code including modifying and distributing.
# However, I do not consent to this code being sold in its current form or similar.
# I request acknowledgement in code under the copyright act
# I hope you enjoy
import os
import random
import time       
import threading

exit_choice = ""
app = 0


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    return


def chat_bot():
    print("_____________MINIGPT_____________")

    def greeting():
        greetings = random.choice(
            [
                "Hello there!",
                "Hey! How's it going?",
                "Hiya!",
                "Greetings, human!",
                "Yo! What's up?",
                "Good day to you!",
                "Howdy partner!",
                "Hi! What's on your mind today?",
                "Hey there! Need something?",
                "Hello! Ready to chat?",
            ]
        )
        print(greetings)

    def calculator():
        while True:
            try:
                num1 = int(input("bot: What is the first number? "))
                function = input("bot: What is the function? ")
                num2 = int(input("bot: What is the second number? "))
            except ValueError:
                print("bot: sorry I can't help with that, can you please try again?")
                continue

            if function == "+":
                result = num1 + num2
                print("bot: the answer is ", result)
            elif function == "-":
                result = num1 - num2
                print("bot: the answer is ", result)
            elif function.lower() == "x" or function == "*":
                result = num1 * num2
                print("bot: the answer is ", result)
            elif function == "/":
                if num2 == 0:
                    print("bot: sorry I can't divide by zero, can you please try again?")
                    continue
                result = num1 / num2
                print("bot: the answer is ", result)
            else:
                print("bot: sorry I can't help with that, can you please try again?")
                continue
            break

    def jokes():
        joke_list = random.choice(
            [
                "Why don't skeletons fight each other? They don't have the guts.",
                "I told my wife she was drawing her eyebrows too high. She looked surprised.",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "I used to play piano by ear, but now I use my hands.",
                "What do you call fake spaghetti? An impasta.",
                "Why don't eggs tell jokes? Because they'd crack each other up.",
                "What's orange and sounds like a parrot? A carrot.",
                "Why couldn't the bicycle stand up by itself? It was two-tired.",
                "I'm reading a book on anti-gravity. It's impossible to put down.",
                "I told my computer I needed a break, and now it won't stop sending me Kit-Kats.",
                "Why did the tomato turn red? Because it saw the salad dressing!",
                "I tried to catch some fog earlier. I mist.",
                "What do you call cheese that isn't yours? Nacho cheese!",
            ]
        )
        print("bot: ", joke_list)

    def translations(chat_you):
        human_greetings = [
            "hi", "hello", "hey", "hiya", "howdy", "g'day", "what's up", "yo", "sup",
            "heya", "good morning", "good afternoon", "good evening", "hi there",
            "hello there", "hey there", "how's it going", "how are you",
            "what's going on", "what's happening", "hiya there", "greetings",
            "morning", "evening", "afternoon",
        ]
        calculator_requests = [
            "Can I use a calculator?", "Do you have a calculator?",
            "Is it okay if I use a calculator?", "Can I grab the calculator?",
            "Mind if I use the calculator?", "Could you pass me the calculator?",
            "Can I calculate this real quick?", "Do you have a moment to use the calculator?",
            "I need to use a calculator, is that fine?", "Would you mind if I used the calculator?",
            "Could I borrow the calculator?", "Can I use the calculator for a second?",
            "I need to do some math, can I use the calculator?",
            "Is it alright if I use the calculator now?", "Can I use your calculator?",
            "Let's calculate something!", "Let's use the calculator for a quick calculation.",
            "How about we calculate this together?", "Let's figure this out using the calculator.",
            "Can we do some math with the calculator?", "Let's solve this using a calculator.",
            "I need to calculate something, let's use the calculator.",
            "Let's do a quick calculation!", "I think we need a calculator for this.",
            "I want to calculate something, can we use the calculator?",
            "can you help me with math", "can you calculate this", "let's do some math",
            "can you calculate something for me", "please help me calculate",
            "I need help with math", "can you solve this", "let's calculate something",
            "can you use a calculator for me", "help me with a calculation",
            "do some math for me", "can you do math", "can you figure this out",
            "can you solve a problem for me", "calculate", "math", "calculator",
        ]
        joke_requests = [
            "tell me a joke", "can you tell me a joke?", "make me laugh",
            "say something funny", "I need a joke", "tell a joke",
            "can you crack a joke?", "give me a joke", "got any jokes?",
            "how about a joke?", "please tell me a joke", "tell me something funny",
            "make me laugh with a joke", "humor me with a joke",
        ]
        bye_phrases = [
            "Goodbye", "See you later", "Bye now", "Take care", "Catch you later",
            "See ya", "Until next time", "Peace out", "Later", "Have a good one",
            "Farewell", "Adios", "Cya", "I'm out", "I'm done here", "You can go now",
            "Shut up", "Leave me alone", "Stop talking", "Enough already",
            "I don't need you anymore", "Quit it", "Go away", "I'm sick of you",
            "You're annoying, goodbye", "Leave me be", "Stop responding",
            "fuck off", "bye", "later", "later loser", "exit", "end"
        ]
        gratitude_phrases = [
            "Thank you", "Thanks a lot", "I appreciate it", "Thanks so much",
            "You're awesome, thanks", "I owe you one", "I'm grateful",
            "Much appreciated", "Thanks for the help", "I can't thank you enough",
            "You're a lifesaver, thank you", "Thanks for everything",
            "I appreciate your help", "You're the best, thanks", "Thank you so much",
            "I really appreciate that", "I'm grateful for you", "Thanks a ton",
            "I couldn't have done it without you", "You're amazing, thank you",
            "Big thanks", "thanks", "thankyou",
        ]

        if any(greet in chat_you.lower() for greet in human_greetings):
            greeting()
        elif any(calc in chat_you.lower() for calc in calculator_requests):
            calculator()
        elif any(joke in chat_you.lower() for joke in joke_requests):
            jokes()
        elif any(thanks in chat_you.lower() for thanks in gratitude_phrases):
            print("bot: glad to help")
        elif any(bye in chat_you.lower() for bye in bye_phrases):
            print("bot: bye")
            clear_console()
            return False
        else:
            print("sorry I don't understand, can you please try again?")
        return True

    while True:
        chat_you = input("You:")
        if not translations(chat_you):
            break


def grad_calculators():
    def weighted_calc():
        global exit_choice, app
        app = 1
        while True:
            print("Weighted_Calculator")
            amount = input("How many assignments: ")
            if not amount.isdigit() or not (1 <= int(amount) <= 100):
                clear_console()
                print("RESULT", amount, " IS NOT VALID, PLEASE START AGAIN")
                continue
            
            amount = int(amount)
            weight_dec_100 = 0
            final_grade = 0
            restart = False
            
            for _ in range(amount):
                weight = input("enter assignment weighting %: ")
                if not weight.isdigit() or not (1 <= int(weight) <= 100):
                    clear_console()
                    print("RESULT", weight, " IS NOT VALID, PLEASE START AGAIN")
                    restart = True
                    break
                weight = int(weight)
                
                grade = input("enter assignment grade: ")
                if not grade.isdigit() or not (1 <= int(grade) <= 100):
                    clear_console()
                    print("RESULT", grade, " IS NOT VALID, PLEASE START AGAIN")
                    restart = True
                    break
                grade = int(grade)
                
                weight_dec = weight / 100
                scaled_grade = weight_dec * grade
                final_grade += scaled_grade
                weight_dec_100 += weight_dec
            
            if restart:
                continue

            print(final_grade)
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    def grade_goal():
        global exit_choice, app
        app = 2
        while True:
            print("Grade Goal Calculator")
            grade = input("Enter current Grade: ")
            if not grade.isdigit() or not (1 <= int(grade) <= 100):
                clear_console()
                print("RESULT", grade, " IS NOT VALID, PLEASE START AGAIN")
                continue
            grade = int(grade)
            
            goal = input("Enter your goal grade: ")
            if not goal.isdigit() or not (1 <= int(goal) <= 100):
                clear_console()
                print("RESULT", goal, " IS NOT VALID, PLEASE START AGAIN")
                continue
            goal = int(goal)
            
            weight = input("Enter Weight Of Final Assignment: ")
            if not weight.isdigit() or not (1 <= int(weight) <= 100):
                clear_console()
                print("RESULT", weight, " IS NOT VALID, PLEASE START AGAIN")
                continue
            weight = int(weight)
            
            weight_dec = weight / 100
            current_contribution = (1 - weight_dec) * grade
            required_final_grade = (goal - current_contribution) / weight_dec
            
            print("You need to achieve " + str(required_final_grade) + " to achieve a final grade of " + str(goal))
            
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    def gpa_calculator():
        global exit_choice, app
        app = 3
        while True:
            print("GPA Calculator")
            amount = input("How many subjects are you calculating for: ")
            if not amount.isdigit():
                clear_console()
                print("RESULT", amount, " IS NOT VALID, PLEASE START AGAIN")
                continue
            amount = int(amount)
            
            subject1 = []
            gpa1 = []
            result1 = []
            grade1 = []
            restart = False
            
            for _ in range(amount):
                subject = input("enter subject name: ")
                if subject.strip() == "":
                    clear_console()
                    print("RESULT", subject, " IS NOT VALID, PLEASE START AGAIN")
                    restart = True
                    break
                    
                grade = input("enter subject grade: ")
                if not grade.isdigit() or not (1 <= int(grade) <= 100):
                    clear_console()
                    print("RESULT", grade, " IS NOT VALID, PLEASE START AGAIN")
                    restart = True
                    break
                grade = int(grade)

                if grade < 50:
                    gpa = 0
                    result = "Fail"
                elif grade >= 50 and grade < 60:
                    gpa = 1
                    result = "Pass"
                elif grade >= 60 and grade < 70:
                    gpa = 2
                    result = "Credit"
                elif grade >= 70 and grade < 80:
                    gpa = 3
                    result = "Distinction"
                elif grade >= 80 and grade <= 100:
                    gpa = 4
                    result = "High Distinction"
                    
                gpa1.append(str(gpa))
                subject1.append(subject)
                result1.append(result)
                grade1.append(str(grade))
            
            if restart:
                continue

            print("########Results##########")
            calc_gpa = 0
            for index in range(amount):
                print(subject1[index] + ":" + " " + grade1[index] + " " + result1[index])
                calc_gpa += int(gpa1[index])

            final_gpa = calc_gpa / amount if amount > 0 else 0
            final_gpa_str = str(final_gpa)

            if final_gpa < 1:
                final_result = "Fail"
            elif final_gpa >= 1 and final_gpa < 2:
                final_result = "Pass"
            elif final_gpa >= 2 and final_gpa < 3:
                final_result = "Credit"
            elif final_gpa >= 3 and final_gpa < 4:
                final_result = "Distinction"
            else:
                final_result = "High Distinction"

            print("________________")
            print("Gpa: " + final_gpa_str)
            print("Result: " + final_result)
            
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    def gpa_goal():
        global exit_choice, app
        app = 4
        while True:
            print("GPA Goal Calculator")
            current_gpa = input("Enter Current GPA: ")
            try:
                current_gpa = float(current_gpa)
                if not (0 <= current_gpa <= 4):
                    clear_console()
                    print("RESULT", current_gpa, " IS NOT VALID, PLEASE START AGAIN")
                    continue
            except ValueError:
                clear_console()
                print("RESULT", current_gpa, " IS NOT VALID, PLEASE START AGAIN")
                continue
            
            goal_gpa = input("Enter Goal GPA: ")
            try:
                goal_gpa = float(goal_gpa)
                if not (0 <= goal_gpa <= 4):
                    clear_console()
                    print("RESULT", goal_gpa, " IS NOT VALID, PLEASE START AGAIN")
                    continue
            except ValueError:
                clear_console()
                print("RESULT", goal_gpa, " IS NOT VALID, PLEASE START AGAIN")
                continue
            
            time_goal = input("How many semesters do you have to reach your goal: ")
            try:
                time_goal = int(time_goal)
            except ValueError:
                clear_console()
                print("RESULT", time_goal, " IS NOT VALID, PLEASE START AGAIN")
                continue

            adjusted_time = 1 + time_goal
            result_needed = goal_gpa * adjusted_time - current_gpa
            if time_goal > 0:
                result_final = round(result_needed / time_goal, 2)
            else:
                result_final = result_needed

            if result_final > 4:
                print("You can't achieve a GPA of " + str(goal_gpa) + " within " + str(time_goal) + " semesters")
            else:
                print("You need a GPA of " + str(result_final) + " on average for the next " + str(time_goal) + " semesters to achieve a GPA of " + str(goal_gpa))
                
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    while True:
        print("______________________________")
        print("Grade Calculators")
        print("1. Weighted Calculator")
        print("2. Grade Goal Calculator")
        print("3. GPA Calculator")
        print("4. GPA Goal Calculator")
        print("5. Exit")
        print("______________________________")
        try:
            option = int(input("Choose an Option (1-5): "))
        except ValueError:
            clear_console()
            print("INVALID INPUT, PLEASE START AGAIN")
            continue
        
        clear_console()
        print("\n")
        
        if option == 1:
            weighted_calc()
        elif option == 2:
            grade_goal()
        elif option == 3:
            gpa_calculator()
        elif option == 4:
            gpa_goal()
        elif option == 5:
            clear_console()
            break
        else:
            clear_console()
            print("RESULT", option, " IS NOT VALID, PLEASE START AGAIN")


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


def YT_Analytics():
    def YT_Title_Gen():
        global exit_choice, app
        app = 7
        while True:
            print("Youtube Title Generator")
            enter_keyword = input("Enter a keyword: ")
            hows = input("Do you want titles beginning with How? (y/n): ")

            enter_number = input("How many titles do you want: ")
            if not enter_number.isdigit():
                clear_console()
                print("RESULT", enter_number, " IS NOT VALID, PLEASE START AGAIN")
                continue
            num = int(enter_number)

            for _ in range(num):
                keyword = random.choice(
                    [
                        "Comprehensive", "Easy", "Step-by-Step", "Essential",
                        "Beginner-Friendly", "Detailed", "Efficient", "Advanced",
                        "Quick", "Foolproof", "Simple", "Effortless", "Basic",
                        "Straightforward", "Beginner-friendly", "Fast", "No-fuss",
                        "Instant", "Clear", "Simple-to-follow", "Smooth", "Hassle-free",
                        "Ultimate", "Powerful", "Unbeatable", "Stunning", "Incredible",
                        "Amazing", "Revolutionary", "Epic", "Jaw-dropping", "Unstoppable",
                        "Unique", "Innovative", "Groundbreaking", "One-of-a-kind",
                        "Original", "Exclusive", "Fresh", "Master", "Pro-level",
                        "Expert", "Top-tier", "Unmatched", "Unrivaled", "Legendary",
                        "Impossible", "Challenging", "Surprising", "Insane", "Hidden",
                    ]
                )

                if hows == "y":
                    title = "How to make A " + keyword + " " + enter_keyword + " in Minecraft"
                else:
                    title = "You need this " + keyword + " " + enter_keyword + " in Minecraft"
                print(title)
                
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    def Trend_Calculator():
        global exit_choice, app
        app = 8
        while True:
            print("YT Trend Calculator")
            audience = input("Enter topic popularity: ")
            if not audience.isdigit():
                clear_console()
                print("RESULT", audience, " IS NOT VALID, PLEASE START AGAIN")
                continue
            audience = int(audience)
            
            competition = input("Enter Competition: ")
            if not competition.isdigit() or not (0 <= int(competition) <= 100):
                clear_console()
                print("RESULT", competition, " IS NOT VALID, PLEASE START AGAIN")
                continue
            competition = int(competition)
            
            vidiq = input("Enter VidIQ Score: ")
            if not vidiq.isdigit() or not (0 <= int(vidiq) <= 100):
                clear_console()
                print("RESULT", vidiq, " IS NOT VALID, PLEASE START AGAIN")
                continue
            vidiq = int(vidiq)

            score = 0
            if audience >= 400000: score = 100
            elif audience >= 350000: score = 95
            elif audience >= 300000: score = 90
            elif audience >= 250000: score = 85
            elif audience >= 200000: score = 80
            elif audience >= 150000: score = 75
            elif audience >= 100000: score = 70
            elif audience >= 75000: score = 65
            elif audience >= 50000: score = 60
            elif audience >= 25000: score = 55
            elif audience >= 20000: score = 50
            elif audience >= 10000: score = 45
            elif audience >= 7500: score = 40
            elif audience >= 5000: score = 35
            elif audience >= 2500: score = 30

            comp_score = 100 - competition
            bonus = comp_score * 0.1
            if bonus > 10: bonus = 10
            comp_score_final = comp_score + bonus
            raw_score = (comp_score_final + score) / 2

            final_score = (raw_score + vidiq) / 2
            
            if final_score == 0 and vidiq == 0:
                accuracy = 100
            elif vidiq > raw_score:
                accuracy = round(final_score / vidiq * 100) if vidiq else 0
            else:
                accuracy = round(vidiq / final_score * 100) if final_score else 0

            print("\n################################")
            print("Keyword Inspector Results: ")
            print("Competition Score: " + str(comp_score))
            print("Search Volume: " + str(score))
            print("Raw Score: " + str(raw_score))
            print("VidIQ Score: " + str(vidiq))
            print("Final Score: " + str(final_score))
            print("Accuracy: " + str(accuracy) + "%")
            print("\n_______________________________________")
            
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    def YT_Grade():
        global exit_choice, app
        app = 9
        while True:
            subscribers = input("Subscriber Count:")
            if not subscribers.isdigit() or int(subscribers) < 0:
                clear_console()
                print("RESULT", subscribers, " IS NOT VALID, PLEASE START AGAIN")
                continue
            subscribers = int(subscribers)

            views = input("View Count:")
            if not views.isdigit() or int(views) < 0:
                clear_console()
                print("RESULT", views, " IS NOT VALID, PLEASE START AGAIN")
                continue
            views = int(views)
            
            likes = input("Like Count:")
            if not likes.isdigit() or int(likes) < 0:
                clear_console()
                print("RESULT", likes, " IS NOT VALID, PLEASE START AGAIN")
                continue
            likes = int(likes)
            
            engagement = input("Engagement as % :")
            if not engagement.isdigit() or int(engagement) < 0:
                clear_console()
                print("RESULT", engagement, " IS NOT VALID, PLEASE START AGAIN")
                continue
            engagement = int(engagement)
            
            comment = input("Comment Count:")
            if not comment.isdigit() or int(comment) < 0:
                clear_console()
                print("RESULT", comment, " IS NOT VALID, PLEASE START AGAIN")
                continue
            comment = int(comment)

            a_plus_views = 2 * subscribers
            a_views = 1.5 * subscribers
            b_plus_views = 1 * subscribers
            b_views = 0.5 * subscribers
            c_plus_views = 0.3 * subscribers
            c_views = 0.15 * subscribers
            d_plus_views = 0.05 * subscribers
            d_views = 0.01 * subscribers

            if views >= a_plus_views: views_grade, views_grade_num = "A+", 1
            elif views >= a_views: views_grade, views_grade_num = "A", 2
            elif views >= b_plus_views: views_grade, views_grade_num = "B+", 3
            elif views >= b_views: views_grade, views_grade_num = "B", 4
            elif views >= c_plus_views: views_grade, views_grade_num = "C+", 5
            elif views >= c_views: views_grade, views_grade_num = "C", 6
            elif views >= d_plus_views: views_grade, views_grade_num = "D+", 7
            elif views >= d_views: views_grade, views_grade_num = "D", 8
            else: views_grade, views_grade_num = "F", 9

            if views_grade_num == 1: bonus_views = 0.25
            elif views_grade_num == 2: bonus_views = 0.225
            elif views_grade_num == 3: bonus_views = 0.2
            elif views_grade_num == 4: bonus_views = 0.175
            elif views_grade_num == 5: bonus_views = 0.15
            else: bonus_views = 0

            a_plus_likes = views * 0.06
            a_likes = views * 0.04
            b_plus_likes = views * 0.03
            b_likes = views * 0.02
            c_plus_likes = views * 0.015
            c_likes = views * 0.01
            d_plus_likes = views * 0.005
            d_likes = views * 0.001

            if likes >= a_plus_likes: likes_grade, likes_grade_num = "A+", 1
            elif likes >= a_likes: likes_grade, likes_grade_num = "A", 2
            elif likes >= b_plus_likes: likes_grade, likes_grade_num = "B+", 3
            elif likes >= b_likes: likes_grade, likes_grade_num = "B", 4
            elif likes >= c_plus_likes: likes_grade, likes_grade_num = "C+", 5
            elif likes >= c_likes: likes_grade, likes_grade_num = "C", 6
            elif likes >= d_plus_likes: likes_grade, likes_grade_num = "D+", 7
            elif likes >= d_likes: likes_grade, likes_grade_num = "D", 8
            else: likes_grade, likes_grade_num = "F", 9

            if likes_grade_num == 1: bonus_likes = 0.125
            elif likes_grade_num == 2: bonus_likes = 0.1
            elif likes_grade_num == 3: bonus_likes = 0.075
            elif likes_grade_num == 4: bonus_likes = 0.050
            elif likes_grade_num == 5: bonus_likes = 0.025
            else: bonus_likes = 0

            a_plus_eng = 90
            a_eng = 80
            b_plus_eng = 70
            b_eng = 60
            c_plus_eng = 50
            c_eng = 40
            d_plus_eng = 30
            d_eng = 20

            if engagement >= a_plus_eng: eng_grade, eng_grade_num = "A+", 1
            elif engagement >= a_eng: eng_grade, eng_grade_num = "A", 2
            elif engagement >= b_plus_eng: eng_grade, eng_grade_num = "B+", 3
            elif engagement >= b_eng: eng_grade, eng_grade_num = "B", 4
            elif engagement >= c_plus_eng: eng_grade, eng_grade_num = "C+", 5
            elif engagement >= c_eng: eng_grade, eng_grade_num = "C", 6
            elif engagement >= d_plus_eng: eng_grade, eng_grade_num = "D+", 7
            elif engagement >= d_eng: eng_grade, eng_grade_num = "D", 8
            else: eng_grade, eng_grade_num = "F", 9

            if eng_grade_num == 1: bonus_eng = 0.2
            elif eng_grade_num == 2: bonus_eng = 0.175
            elif eng_grade_num == 3: bonus_eng = 0.15
            elif eng_grade_num == 4: bonus_eng = 0.125
            elif eng_grade_num == 5: bonus_eng = 0.1
            else: bonus_eng = 0

            a_plus_com = views * 0.04
            a_com = views * 0.03
            b_plus_com = views * 0.025
            b_com = views * 0.02
            c_plus_com = views * 0.015
            c_com = views * 0.01
            d_plus_com = views * 0.007
            d_com = views * 0.003

            if comment >= a_plus_com: com_grade, com_grade_num = "A+", 1
            elif comment >= a_com: com_grade, com_grade_num = "A", 2
            elif comment >= b_plus_com: com_grade, com_grade_num = "B+", 3
            elif comment >= b_com: com_grade, com_grade_num = "B", 4
            elif comment >= c_plus_com: com_grade, com_grade_num = "C+", 5
            elif comment >= c_com: com_grade, com_grade_num = "C", 6
            elif comment >= d_plus_com: com_grade, com_grade_num = "D+", 7
            elif comment >= d_com: com_grade, com_grade_num = "D", 8
            else: com_grade, com_grade_num = "F", 9

            if com_grade_num == 1: bonus_com = 0.1
            elif com_grade_num == 2: bonus_com = 0.075
            elif com_grade_num == 3: bonus_com = 0.05
            elif com_grade_num == 4: bonus_com = 0.025
            elif com_grade_num == 5: bonus_com = 0.01
            else: bonus_com = 0

            bonus = bonus_views + bonus_com + bonus_eng + bonus_likes

            total_grade_num = (views_grade_num + likes_grade_num + eng_grade_num + com_grade_num) / 4
            if bonus > 3: bonus = 3
            Scaled_Grade_num = total_grade_num - bonus
            bonus_str = str(bonus)

            if total_grade_num <= 1.5: grade = "A+"
            elif total_grade_num <= 2.5: grade = "A"
            elif total_grade_num <= 3.5: grade = "B+"
            elif total_grade_num <= 4.5: grade = "B"
            elif total_grade_num <= 5.5: grade = "C+"
            elif total_grade_num <= 6.5: grade = "C"
            elif total_grade_num <= 7.5: grade = "D+"
            elif total_grade_num <= 8.5: grade = "D"
            else: grade = "F"

            if Scaled_Grade_num <= 1.5: scale_grade = "A+"
            elif Scaled_Grade_num <= 2.5: scale_grade = "A"
            elif Scaled_Grade_num <= 3.5: scale_grade = "B+"
            elif Scaled_Grade_num <= 4.5: scale_grade = "B"
            elif Scaled_Grade_num <= 5.5: scale_grade = "C+"
            elif Scaled_Grade_num <= 6.5: scale_grade = "C"
            elif Scaled_Grade_num <= 7.5: scale_grade = "D+"
            elif Scaled_Grade_num <= 8.5: scale_grade = "D"
            else: scale_grade = "F"

            print("##########################")
            print("Final Results:")
            print("Views Grade: " + views_grade)
            print("Likes Grade: " + likes_grade)
            print("Engagement Grade: " + eng_grade)
            print("Comments Grade: " + com_grade)

            print("Bonus:" + bonus_str)
            print("---------")
            print("Final Grade:" + grade)
            print("Scaled Grade: " + scale_grade)
            print("##########################")
            
            exit_choice = input("Start Again: ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    while True:
        print("______________________________")
        print("YT Analytics:")
        print("1.Title Generator")
        print("2.Keyword Search")
        print("3.YT Video Grade Calculator")
        print("4.Exit")
        print("______________________________")
        option = input("Choose An Option (1-4): ")
        clear_console()
        print("\n\n")
        try:
            option_int = int(option)
        except ValueError:
            clear_console()
            continue
        
        if option_int == 1:
            clear_console()
            YT_Title_Gen()
        elif option_int == 2:
            clear_console()
            Trend_Calculator()
        elif option_int == 3:
            clear_console()
            YT_Grade()
        elif option_int == 4:
            clear_console()
            break
        else:
            clear_console()
            
def cybersec():
    def Net_Analyser():
        try:
            from scapy.all import sniff, IP, TCP, UDP
        except ImportError:
            print("\n[!] Error: The 'scapy' module is not installed in the current Python environment.")
            print("[!] It looks like you might have multiple Python versions.")
            print("[!] Try running the script using:")
            print("    python3 mini_pc.py")
            print("[!] Or install it explicitly for this environment by running:")
            print("    python3 -m pip install scapy")
            input("\nPress Enter to return to the previous menu...")
            return

        from datetime import datetime           
        import socket
        import threading   
        SERVICE_MAP = {
            53: "DNS",
            80: "HTTP (WEB)",
            443: "HTTPS (SECURE WEB)",
            22: "SSH(Remote Access)",
            21: "FTP"
        }

        global exit_choice, app
        app = 10

        while True:
            def enhanced_scanner(target):
                try:
                    hostname = socket.gethostbyaddr(target)[0]
                except socket.herror:
                    hostname = "Unknown Name"
                print(f"\n---Scanning {target}--{hostname}---")
        
                for port in SERVICE_MAP.keys():
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
            
                    if s.connect_ex((target, port)) == 0:
                        service = SERVICE_MAP.get(port, "Unknown Service")    
                        print(f"[+] {port:<5}) |  {service:<15} | OPEN")
                    s.close()

            hostname = socket.gethostname()
            MY_IP = socket.gethostbyname(hostname)
            TARGET_IP = input("Enter IP address or press enter: ")

            if TARGET_IP == "":
                TARGET_IP = MY_IP

            DNS_CACHE = {}
            HOST_CACHE = {}
            
            stop_event = threading.Event()

            def packet_callback(packet):
                if stop_event.is_set():
                    return
                direction = "UNKNOWN"
                resolved_name = "UNKNOWN"
                if packet.haslayer(IP):
                    src_ip = packet[IP].src 
                    dst_ip = packet[IP].dst
            
                    if src_ip == TARGET_IP or dst_ip == TARGET_IP:
                        portinfo = "NONE" 
                        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                        src_port = "N/A"
                        dst_port = "N/A"
                        proto = "Other"
                        
                        if packet.haslayer(TCP): 
                            proto = "TCP    "
                            src_port = packet[TCP].sport
                            dst_port = packet[TCP].dport
                        elif packet.haslayer(UDP): 
                            proto = "UDP    "
                            src_port = packet[UDP].sport
                            dst_port = packet[UDP].dport
                        else:
                            proto = "OTHER  "
                            
                        if dst_ip == MY_IP:
                            direction = "INBOUND"
                        elif src_ip == MY_IP:
                            direction = "OUTBOUND"
                            
                        service_name = SERVICE_MAP.get(dst_port, SERVICE_MAP.get(src_port, "UNKNOWN"))
                        portinfo = (f"{service_name}") if service_name != "UNKNOWN" else ""
                        
                        for ip in [src_ip, dst_ip]:
                            if ip not in HOST_CACHE:
                                try:
                                    name = socket.gethostbyaddr(ip)[0]
                                    HOST_CACHE[ip] = name 
                                except socket.herror:
                                    HOST_CACHE[ip] = ""
            
                        if src_ip == TARGET_IP:
                            resolved_name = HOST_CACHE.get(dst_ip, dst_ip)
                        else: 
                            resolved_name = HOST_CACHE.get(src_ip, src_ip) 
            
                        print(f"[{timestamp}] {proto:5} | {src_ip}:{src_port} -> {dst_ip}:{dst_port} | {len(packet)} bytes |  {portinfo} | {direction} | {resolved_name}")

            def stop_filter_fn(packet):
                return stop_event.is_set()

            sniff_thread = threading.Thread(
                target=sniff,
                kwargs={
                    'filter': f"host {TARGET_IP}",
                    "prn": packet_callback,
                    "store": 0,
                    "stop_filter": stop_filter_fn
                },
                daemon=True
            )
            sniff_thread.start()

            print(f"--- Monitoring live traffic for {TARGET_IP}---")
            print("____________")
            enhanced_scanner(TARGET_IP)
            print("____________")

            try:
                print("Press Enter to stop the monitor.")
                input("")
            except KeyboardInterrupt:
                pass
                
            stop_event.set()
            print("\n Session Ending...")

            exit_choice = input("Start Again (y/n): ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    while True:
        print("______________________________")
        print("Cyber Security Tools:")
        print("1.Network Analyser")
        print("2.Exit")
        print("______________________________")
        option = input("Choose An Option (1-2): ")
        clear_console()
        print("\n\n")
        try:
            option_int = int(option)
        except ValueError:
            clear_console()
            continue
        
        if option_int == 1:
            clear_console()
            Net_Analyser()
        elif option_int == 2:
            clear_console()
            break
        else:
            clear_console()


def menu():
    while True:
        clear_console()
        print("______________________")
        print("Menu")
        print("1. Grade Calculators")
        print("2. Games")
        print("3. Youtube Analytics")
        print("4. Chat bot")
        print("5. Cyber Security Tools")
        print("6. Exit")
        print("_____________________")
        option = input("enter option: ")
        print("\n")
        clear_console()
        print("\n")
        try:
            option_int = int(option)
        except ValueError:
            continue
        
        if option_int == 1:
            grad_calculators()
        elif option_int == 2:
            games()
        elif option_int == 3:
            YT_Analytics()
        elif option_int == 4:
            clear_console()
            chat_bot()
        elif option_int == 5:
            clear_console()
            cybersec()
        elif option_int == 6:
            clear_console()
            exit()


menu()
# Welcome to the MINI PC - I created the MINI PC as an efficient method to store my programming scripts
# I Dante Rosini under the MIT Licence permit all personal use of this code including modifying and distributing.
# However, I do not consent to this code being sold in its current form or similar.
# I request acknowledgement in code under the copyright act
# I hope you enjoy DONT REMOVE ANYTHING