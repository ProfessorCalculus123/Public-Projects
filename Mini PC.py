exit_choice = ""
app = 0
import os
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    return 
 

def chat_bot():
    import random 
    chatmode = True

    def greeting():
        greetings = random.choice([
            "Hello there!", 
            "Hey! How's it going?", 
            "Hiya!", 
            "Greetings, human!", 
            "Yo! What's up?", 
            "Good day to you!", 
            "Howdy partner!", 
            "Hi! What's on your mind today?", 
            "Hey there! Need something?", 
            "Hello! Ready to chat?"
        ])
        print(greetings)
        return main()

    def calculator():
        num1 = int(input("bot: What is the first number? "))
        function = input("bot: What is the function? ")
        num2 = int(input("bot: What is the second number? "))

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
            result = num1 / num2
            print("bot: the answer is ", result)
        else:
            print("bot: sorry I can't help with that, can you please try again?")
            return calculator()

        return main()

    def jokes():
        jokes = random.choice([
            "Why don't skeletons fight each other? They don't have the guts.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I used to play piano by ear, but now I use my hands.",
            "What do you call fake spaghetti? An impasta.",
            "Why don’t eggs tell jokes? Because they’d crack each other up.",
            "What’s orange and sounds like a parrot? A carrot.",
            "Why couldn’t the bicycle stand up by itself? It was two-tired.",
            "I’m reading a book on anti-gravity. It’s impossible to put down.",
            "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "I tried to catch some fog earlier. I mist.",
            "What do you call cheese that isn't yours? Nacho cheese!"
        ])
        print("bot: ", jokes)
        return main()

    def transaltions():
        global chat_you
        human_greetings = [
            "hi", "hello", "hey", "hiya", "howdy", "g'day", "what's up", "yo", "sup", 
            "heya", "good morning", "good afternoon", "good evening", "hi there", 
            "hello there", "hey there", "how's it going", "how are you", "what's going on", 
            "what's happening", "hiya there", "greetings", "morning", "evening", "afternoon"
        ]
        calculator_requests = [
            "Can I use a calculator?", "Do you have a calculator?", "Is it okay if I use a calculator?", 
            "Can I grab the calculator?", "Mind if I use the calculator?", "Could you pass me the calculator?", 
            "Can I calculate this real quick?", "Do you have a moment to use the calculator?", 
            "I need to use a calculator, is that fine?", "Would you mind if I used the calculator?", 
            "Could I borrow the calculator?", "Can I use the calculator for a second?", 
            "I need to do some math, can I use the calculator?", "Is it alright if I use the calculator now?", 
            "Can I use your calculator?", "Let's calculate something!", "Let's use the calculator for a quick calculation.", 
            "How about we calculate this together?", "Let's figure this out using the calculator.", 
            "Can we do some math with the calculator?", "Let's solve this using a calculator.", 
            "I need to calculate something, let's use the calculator.", "Let's do a quick calculation!", 
            "I think we need a calculator for this.", "I want to calculate something, can we use the calculator?",
            "can you help me with math", "can you calculate this", "let's do some math", 
            "can you calculate something for me", "please help me calculate", "I need help with math", 
            "can you solve this", "let's calculate something", "can you use a calculator for me", 
            "help me with a calculation", "do some math for me", "can you do math", "can you figure this out", 
            "can you solve a problem for me", "calculate", "math", "calculator"
        ]
        joke = [
            "tell me a joke", "can you tell me a joke?", "make me laugh", "say something funny", "I need a joke", 
            "tell a joke", "can you crack a joke?", "give me a joke", "got any jokes?", "how about a joke?", 
            "please tell me a joke", "tell me something funny", "make me laugh with a joke", "humor me with a joke"
        ]
        bye = [
            "Goodbye", "See you later", "Bye now", "Take care", "Catch you later", "See ya", "Until next time", 
            "Peace out", "Later", "Have a good one", "Farewell", "Adios", "Cya", "I'm out", "I'm done here", 
            "You can go now", "Shut up", "Leave me alone", "Stop talking", "Enough already", "I don’t need you anymore", 
            "Quit it", "Go away", "I'm sick of you", "You're annoying, goodbye", "Leave me be", "Stop responding", 
            "Fuck off", "bye", "later", "later loser"
        ]
        gratitude_phrases = [
            "Thank you", "Thanks a lot", "I appreciate it", "Thanks so much", "You're awesome, thanks", "I owe you one", 
            "I’m grateful", "Much appreciated", "Thanks for the help", "I can't thank you enough", "You're a lifesaver, thank you", 
            "Thanks for everything", "I appreciate your help", "You're the best, thanks", "Thank you so much", 
            "I really appreciate that", "I'm grateful for you", "Thanks a ton", "I couldn't have done it without you", 
            "You're amazing, thank you", "Big thanks", "thanks", "thankyou"
        ]
        
        if any(greet in chat_you.lower() for greet in human_greetings): 
            greeting()
        elif any(calculator in chat_you.lower() for calculator in calculator_requests):
            calculator()
        elif any(joke in chat_you.lower() for joke in joke):
            jokes()
        elif any(thanks in chat_you.lower() for thanks in gratitude_phrases ):
            print("bot: glad to help")
            return main() 
        elif any(bye in chat_you.lower() for bye in bye):
            print("bot: bye")
            clear_console()
            return menu()
        
        else:
            print("sorry I don't understand, can you please try again?")

    def main():
        global chat_you
        while chatmode:
            chat_you = input("You:")
            transaltions()

    main()







def grad_calculators():
    def weighted_calc():
        global exit_choice, app
        app = 1
        print("Weighted_Calculator")
        amount = int(input("How many assignments: "))
        index = 0 
        weight_dec_100 = 0
        final_grade = 0
        while index < amount:
            weight = int(input("enter assignment weighting %: "))
            grade = int(input("enter assignment grade: "))
            weight_dec = weight / 100 
            scaled_grade = weight_dec * grade
            final_grade += scaled_grade
            weight_dec_100 += weight_dec
            index += 1
        if round(weight_dec_100, 2) != 1.00:
            print("RESULT INVALID PLEASE START AGAIN") 
            print(final_grade)
            print(weight_dec_100)
        else:
            print(final_grade)
        exit_choice = input("Start Again: ")
        if exit_choice.lower() == "y" or exit_choice.lower() == "yes" or exit_choice.lower() == "":
            weighted_calc()
        elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
            clear_console()
            return grad_calculators()
        

    def grade_goal():
        global exit_choice, app
        app = 2
        print("Grade Goal Calculator")
        grade = int(input("Enter current Grade: "))
        goal = int(input("Enter your goal grade: "))
        weight = int(input("Enter Weight Of Final Assignment: "))
        weight_dec = (weight / 100)
        current_contribution = (1 - weight_dec) * grade 
        required_final_grade = (goal - current_contribution) / weight_dec
        required_final_grade = str(required_final_grade)
        goal = str(goal)
        print("You need to achieve " + required_final_grade + " to achieve a final grade of " + goal)
        exit_choice = input("Start Again: ")
        if exit_choice.lower() == "y" or exit_choice.lower() == "yes" or exit_choice.lower() == "":
            grade_goal()
        elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
            clear_console()
            return grad_calculators()

    def gpa_calculator():
        global exit_choice, app
        app = 3
        print("GPA Calculator")
        amount = int(input("How many subjects are you calculating for: "))
        index = 0
        subject1 = []
        gpa1 = []
        result1 = []
        grade1 = []
        while index < amount:
            subject = input("enter subject name: ")
            grade = int(input("enter subject grade: "))
            if grade < 50:
                gpa = 0
                result = ("Fail")
            elif grade >= 50 and grade < 60:
                gpa = 1
                result = ("Pass")
            elif grade >= 60 and grade < 70:
                gpa = 2
                result = ("Credit")
            elif grade >= 70 and grade < 80:
                gpa = 3
                result = ("Distinction")
            elif grade >= 80 and grade <= 100:
                gpa = 4
                result = ("High Distinction")
            gpa_str = str(gpa)
            grade_str = str(grade)
            gpa1.append(gpa_str)  # Use .append() to add items to the list
            subject1.append(subject)
            result1.append(result)
            grade1.append(grade_str)
            index += 1

        index = 0
        print("########Results##########")
        calc_gpa = 0
        while index < amount:
            print(subject1[index] + ":" + " " + grade1[index] + " " + result1[index])
            calc_gpa += int(gpa1[index])
            index += 1

        final_gpa = calc_gpa / amount
        final_gpa_str = str(final_gpa)

        if final_gpa < 1:
            final_result = "Fail"
        elif final_gpa >= 1 and final_gpa < 2:
            final_result = "Pass"
        elif final_gpa >= 2 and final_gpa < 3:
            final_result = "Credit"
        elif final_gpa >= 3 and final_gpa < 4:
            final_result = "Distinction"
        elif final_gpa >= 4 and final_gpa <= 5:
            final_result = "High Distinction"

        print("________________")
        print("Gpa: " + final_gpa_str)
        print("Result: " + final_result)
        exit_choice = input("Start Again: ")

        if exit_choice.lower() == "y" or exit_choice.lower() == "yes" or exit_choice.lower() == "":
            gpa_calculator()
        elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
            clear_console()
            return grad_calculators()

    def gpa_goal():
        global exit_choice, app
        app = 4
        print("GPA Goal Calculator")
        current_gpa = float(input("Enter Current GPA: "))
        goal_gpa = float(input("Enter Goal GPA: "))
        time_goal = int(input("How many semesters do you have to reach your goal: "))
        adjusted_time = 1 + time_goal
        result_needed = (goal_gpa * adjusted_time - current_gpa) 
        result_final = round(result_needed / time_goal, 2)
        goal_gpa1 = str(goal_gpa)
        time_goal1 = str(time_goal)
        if result_final > 4:
            print("You can't achieve a GPA of " + goal_gpa1 + " within " + time_goal1 + " semesters")
        else:
            result_final1 = str(result_final)
            print("You need a GPA of " + result_final1 + " on average for the next " + time_goal1 + " semesters to achieve a GPA of " + goal_gpa1)
        exit_choice = input("Start Again: ")
        if exit_choice.lower() == "y" or exit_choice.lower() == "yes" or exit_choice.lower() == "":
            gpa_goal()
        elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
            clear_console()
            return grad_calculators()

    print("1. Weighted Calculator")
    print("2. Grade Goal Calculator")
    print("3. GPA Calculator")
    print("4. GPA Goal Calculator")
    print("5. Exit")
    option = int(input("Choose an Option (1-5)"))
    clear_console()
    print("")
    (input("Press Enter To continue"))
    print("")
    if option == 1:
        weighted_calc()
    if option == 2:
        grade_goal()
    if option == 3:
        gpa_calculator()
    if option == 4:
        gpa_goal()
    if option == 5:
        clear_console()
        return menu()
    
def games():    
                    def coin_flip():
                        global exit_choice, app
                        app = 5
                        print("Coin Flip")
                        input("Press Enter To Flip Coin ")
                        import random
                        coin = ["Heads", "Tails"] 
                        result = random.choice(coin)
                        print("_________")
                        print(result)
                        print("_________")
                        exit_choice = input("Start Again: ")

                        if exit_choice.lower() == "y" or exit_choice.lower() == "yes" or exit_choice.lower() == "":
                            coin_flip()
                        elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
                            return games()

                    def RPS():
                        global exit_choice, app
                        app = 6
                        print("Rock Paper Scissors")
                        print("1. Rock")
                        print("2. Paper") 
                        print("3. Scissors")

                        player = int(input("Select ROCK PAPER SCISSORS using (1-3): "))
                        clear_console()

                        if player == 1:
                            hand = "Rock"
                        elif player == 2:
                            hand = "Paper"
                        elif player == 3:
                            hand = "Scissors"

                        import random
                        npc = ["Rock", "Paper", "Scissors"] 
                        result = random.choice(npc)

                        if hand == result:
                            print("Draw")
                        elif hand == "Rock" and result == "Scissors" or \
                            hand == "Scissors" and result == "Paper" or \
                            hand == "Paper" and result == "Rock":
                            print("You win")
                        else:
                            print("You lose")

                        print("_________")
                        print("PC choose " + result)
                        print("_________")
                        exit_choice = input("Start Again: ")
                        if exit_choice.lower() == "y" or exit_choice.lower() == "yes" or exit_choice.lower() == "":
                            RPS()
                        elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
                            clear_console()
                            return games()

                    def RLGL():
                        import os
                      

                        def clear_console():
                          os.system("cls" if os.name == "nt" else "clear")
                          return
                     
                     
                        def Classic():
                            import random
                            import time
                            import os

                            def new():
                                global start_time, distance
                                start_time = time.time()
                                distance = 50
                                return

                            def time_check():
                                global start_time
                                currant_time = time.time()
                                time_passed = currant_time - start_time
                                print(round(120 - time_passed), " sec left")
                                if time_passed > 120:
                                    game_over()
                                return

                            def clear_console():
                                os.system("cls" if os.name == "nt" else "clear")
                                return

                            def red_light_time():
                                global distance
                                print("greenlight")
                                timer = random.randint(2, 7)
                                starttimer = time.time()
                                timepassed = 0
                                while int(timepassed) < timer:
                                    time_check()
                                    currant_time = time.time()
                                    timepassed = currant_time - starttimer
                                    move = input("")
                                    if move == "w":
                                        clear_console()
                                        distance -= 0.5
                                        distance_check()
                                        print(distance, "m")
                                return

                            def green_light_time():
                                print("redlight")
                                starttimer = time.time()
                                timepassed = 0
                                while int(timepassed) < 3:
                                    currant_time = time.time()
                                    timepassed = currant_time - starttimer
                                    if timepassed < 3:
                                        move = input("")
                                    if move == "w":
                                        game_over()
                                return

                            def distance_check():
                                if distance == 0:
                                    print("_____________")
                                    print("YOU WIN")
                                    print("1.Retry")
                                    print("2.Exit")
                                    print("_____________")
                                    game_state = int(input("Choose an option 1-2"))
                                    if game_state == 1:
                                        clear_console()
                                        return main_game()
                                    if game_state == 2:
                                        clear_console()
                                        return RLGL()

                            def game_over():
                                global distance
                                print("_____________")
                                print("GAME OVER")
                                print(distance, "m remaining")
                                print("1.Retry")
                                print("2.Exit")
                                print("_____________")
                                game_state = int(input("Choose an option 1-2"))
                                if game_state == 1:
                                    clear_console()
                                    return main_game()
                                if game_state == 2:
                                    clear_console()
                                    return RLGL()

                            def main_game():
                                input("Press Enter to Start")
                                new()
                                game = True

                                while game:
                                    red_light_time()
                                    clear_console()
                                    distance_check()
                                    time_check()
                                    clear_console()
                                    green_light_time()
                                    clear_console()
                                    time_check()
                                    clear_console()

                            main_game()

                        def Unlimited():
                            import random
                            import time
                            import os

                            def new():
                                global start_time, distance
                                start_time = time.time()
                                distance = 0
                                return

                            def clear_console():
                                os.system("cls" if os.name == "nt" else "clear")
                                return

                            def red_light_time():
                                global distance
                                print("greenlight")
                                timer = random.randint(1, 15)
                                starttimer = time.time()
                                timepassed = 0
                                while int(timepassed) < timer:
                                    currant_time = time.time()
                                    timepassed = currant_time - starttimer
                                    move = input("")
                                    if move == "w":
                                        clear_console()
                                        distance += 0.5
                                        print(distance, "m")
                                return

                            def green_light_time():
                                print("redlight")
                                starttimer = time.time()
                                timepassed = 0
                                while int(timepassed) < 3:
                                    currant_time = time.time()
                                    timepassed = currant_time - starttimer
                                    if timepassed < 3:
                                        move = input("")
                                    if move == "w":
                                        game_over()
                                return

                            def game_over():
                                global distance
                                print("_____________")
                                print("GAME OVER")
                                print("you travaled ", distance, "m")
                                print("1.Retry")
                                print("2.Exit")
                                print("_____________")
                                game_state = int(input("Choose an option 1-2"))
                                if game_state == 1:
                                    clear_console()
                                    return main_game()
                                if game_state == 2:
                                    clear_console()
                                    RLGL()

                            def main_game():
                                input("Press Enter to Start")
                                new()
                                game = True

                                while game:
                                    red_light_time()
                                    clear_console()
                                    green_light_time()
                                    clear_console()

                            main_game()

                        def Mystery():
                            import random
                            import time
                            import os

                            def new():
                                global start_time, distance
                                start_time = time.time()
                                distance = 50
                                return

                            def time_check():
                                global start_time
                                currant_time = time.time()
                                time_passed = currant_time - start_time
                                if time_passed > 100:
                                    game_over()
                                return

                            def clear_console():
                                os.system("cls" if os.name == "nt" else "clear")
                                return

                            def red_light_time():
                                global distance
                                print("greenlight")
                                timer = random.randint(2, 7)
                                starttimer = time.time()
                                timepassed = 0
                                while int(timepassed) < timer:
                                    time_check()
                                    currant_time = time.time()
                                    timepassed = currant_time - starttimer
                                    move = input("")
                                    if move == "w":
                                        clear_console()
                                        distance -= 0.5
                                        distance_check()
                                        print(distance, "m")
                                return

                            def green_light_time():
                                print("redlight")
                                starttimer = time.time()
                                timepassed = 0
                                while int(timepassed) < 3:
                                    currant_time = time.time()
                                    timepassed = currant_time - starttimer
                                    if timepassed < 3:
                                        move = input("")
                                    if move == "w":
                                        game_over()
                                return

                            def distance_check():
                                if distance == 0:
                                    print("_____________")
                                    print("YOU WIN")
                                    print("1.Retry")
                                    print("2.Exit")
                                    print("_____________")
                                    game_state = int(input("Choose an option 1-2"))
                                    if game_state == 1:
                                        clear_console()
                                        return main_game()
                                    if game_state == 2:
                                        clear_console()
                                        RLGL()

                            def game_over():
                                global distance
                                print("_____________")
                                print("GAME OVER")
                                print(distance, "m remaining")
                                print("1.Retry")
                                print("2.Exit")
                                print("_____________")
                                game_state = int(input("Choose an option 1-2"))
                                if game_state == 1:
                                    clear_console()
                                    return main_game()
                                if game_state == 2:
                                    clear_console()
                                    return RLGL()

                            def main_game():
                                input("Press Enter to Start")
                                new()
                                game = True

                                while game:
                                    red_light_time()
                                    clear_console()
                                    distance_check()
                                    time_check()
                                    clear_console()
                                    green_light_time()
                                    clear_console()
                                    time_check()
                                    clear_console()

                            main_game()

                        def Practice():
                            import random
                            import time
                            import os

                            def new():
                                global start_time, distance
                                distance = 50
                                clear_console()
                                return

                            def clear_console():
                                os.system("cls" if os.name == "nt" else "clear")
                                return

                            def red_light_time():
                                global distance
                                print("greenlight")
                                timer = random.randint(2, 7)
                                starttimer = time.time()
                                timepassed = 0
                                while int(timepassed) < timer:
                                    currant_time = time.time()
                                    timepassed = currant_time - starttimer
                                    move = input("")
                                    if move == "w":
                                        clear_console()
                                        distance -= 0.5
                                        distance_check()
                                        print(distance, "m")
                                return

                            def green_light_time():
                                print("redlight")
                                starttimer = time.time()
                                timepassed = 0
                                while int(timepassed) < 3:
                                    currant_time = time.time()
                                    timepassed = currant_time - starttimer
                                    if timepassed < 3:
                                        move = input("")
                                    if move == "w":
                                        game_over()
                                return

                            def distance_check():
                                if distance == 0:
                                    print("_____________")
                                    print("YOU WIN")
                                    print("1.Retry")
                                    print("2.Exit")
                                    print("_____________")
                                    game_state = int(input("Choose an option 1-2"))
                                    if game_state == 1:
                                        clear_console()
                                        return main_game()
                                    if game_state == 2:
                                        clear_console()
                                        return RLGL()

                            def game_over():
                                global distance
                                print("_____________")
                                print("GAME OVER")
                                print(distance, "m remaining")
                                print("1.Retry")
                                print("2.Exit")
                                print("_____________")
                                game_state = int(input("Choose an option 1-2"))
                                if game_state == 1:
                                    clear_console()
                                    return main_game()
                                if game_state == 2:
                                    clear_console()
                                    return RLGL()

                            def main_game():
                                input("Press Enter to Start")
                                new()
                                game = True

                                while game:
                                    red_light_time()
                                    clear_console()
                                    distance_check()
                                    clear_console()
                                    green_light_time()
                                    clear_console()

                            main_game()
                        def modes():
                          print("__________RLGL__________")
                          print("home:")
                          print("1. Classic")
                          print("2. Unlimited")
                          print("3. Mystery")
                          print("4. Practice")
                          print("5.Exit")
                          print("__________RLGL__________")
                          gamemode = int(input("Choose a game mode 1-4:"))
                          if gamemode == 1:
                             clear_console()
                             Classic()
                          elif gamemode == 2:
                            clear_console()
                            Unlimited()
                          elif gamemode == 3:
                            clear_console()
                            Mystery()
                          elif gamemode == 4:
                            clear_console()
                            Practice()
                          elif gamemode == 5:
                           clear_console()
                           return RLGL() 
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
                            print("4. Practice: Same as Classic, but untimed.\n")

                            print("I hope you enjoy the game!")
                            input("press enter to exit")
                            clear_console()
                            RLGL()

                             
                        print("__________RLGL__________")
                        print("Menu:")
                        print("1. Play Game")
                        print("2. Rules")
                        print("3. Exit")
                        print("__________RLGL__________")
                        gamemode = int(input("Choose a game mode 1-4:"))
                        if gamemode == 1:
                            clear_console()
                            modes()
                        elif gamemode == 2:
                            clear_console()
                            rules()
                        elif gamemode == 3:
                         clear_console()
                         return games() 
                            
                         
                    



                   #  finish here REILIT



                    print("1. Coin Flipper")
                    print("2. RPS")
                    print("3. Red Light | Green Light")
                    print("4. Exit")
                    option = int(input("Choose Option (1-3)"))
                    clear_console()
                    print("")
                    (input("Press Enter To continue"))
                    clear_console()
                    print("")
                    if option == 1:
                            clear_console()
                            coin_flip()
                    if option == 2:
                            clear_console()
                            RPS() 
                    if option == 3:
                        clear_console()
                        RLGL()
                    if option == 4:
                        clear_console()
                        return menu()

def YT_Analytics():

 def YT_Title_Gen():
    import random
    global exit_choice, app
    print("Youtube Title Generator")
    app = 7
    enter_keyword = input("Enter a keyword: ")
    hows = input("Do you want titles beginning with How? (y/n): ")
    enter_number = input("How many titles do you want: ")
    num = int(enter_number)
    index = 0

    while index < num:
        keyword = random.choice([
            "Comprehensive", "Easy", "Step-by-Step", "Essential", 
            "Beginner-Friendly", "Detailed", "Efficient", 
            "Advanced", "Quick", "Foolproof", "Simple",
            "Easy", "Quick", "Effortless", "Basic", 
            "Straightforward", "Beginner-friendly", "Fast", 
            "No-fuss", "Instant", "Clear", "Simple-to-follow", 
            "Smooth", "Hassle-free", "Ultimate", "Powerful", 
            "Unbeatable", "Stunning", "Incredible", "Amazing", 
            "Revolutionary", "Epic", "Jaw-dropping", "Unstoppable", 
            "Unique", "Innovative", "Groundbreaking", "One-of-a-kind", 
            "Original", "Exclusive", "Fresh", "Master", 
            "Pro-level", "Expert", "Advanced", "Top-tier", 
            "Unmatched", "Unrivaled", "Legendary", "Impossible", 
            "Challenging", "Surprising", "Insane", "Hidden"
        ])

        if hows == "y":
            title = 'How to make A ' + keyword + " " + enter_keyword + ' in Minecraft'
        else:
            title = 'You need this ' + keyword + " " + enter_keyword + ' in Minecraft'

        print(title)
        index += 1
    exit_choice=input("Start Again: ")
    if  exit_choice.lower() == "y" or exit_choice.lower() == "yes" or  exit_choice.lower() == "":
       YT_Title_Gen()
    elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
        clear_console()
        return YT_Analytics()



 def Trend_Calculator():
    global exit_choice, app
    app = 8
    print("YT Trend Calculator")
    audience = int(input("Enter topic popularity: "))
    competition = int(input("Enter Competition: "))
    vidiq = int(input("Enter VidIQ Score: "))

    # Determine the score based on audience
    score = 0  # Initialize 'score' with a default value
    if audience >= 400000:
        score = 100
    elif audience >= 350000:
        score = 95
    elif audience >= 300000:
        score = 90
    elif audience >= 250000:
        score = 85
    elif audience >= 200000:
        score = 80
    elif audience >= 150000:
        score = 75
    elif audience >= 100000:
        score = 70
    elif audience >= 75000:
        score = 65
    elif audience >= 50000:
        score = 60
    elif audience >= 25000:
        score = 55
    elif audience == 20000:
        score = 50
    elif audience >= 10000:
        score = 45
    elif audience >= 7500:
        score = 40
    elif audience >= 5000:
        score = 35
    elif audience >= 2500:
        score = 30

    # Calculate scores
    comp_score = 100 - competition
    bonus = comp_score * 0.1
    if bonus > 10:
        bonus = 10
    comp_score_final = comp_score + bonus
    raw_score = (comp_score_final + score) / 2

    final_score = (raw_score + vidiq) / 2
    if vidiq > raw_score:
        accuracy = round(final_score / vidiq * 100)  # This should be positive (raw_score is higher)
    else:
        accuracy = round(vidiq / final_score * 100)  # This should also be positive (vidiq is higher)

    # Print results
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
    if exit_choice.lower() == "y" or exit_choice.lower() == "yes" or exit_choice.lower() == "":
        Trend_Calculator()
    elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
        clear_console()
        return YT_Analytics()


 def YT_Grade():
    global exit_choice, app
    app = 9
    subscribers = int(input("Subscriber Count:"))
    views = int(input("View Count:"))
    likes = int(input("Like Count:"))
    engagement = int(input("Engagement as % :"))
    comment = int(input("Comment Count:"))

    # Grading System for views
    a_plus_views = 2 * subscribers
    a_views = 1.5 * subscribers
    b_plus_views = 1 * subscribers
    b_views = 0.5 * subscribers
    c_plus_views = 0.3 * subscribers
    c_views = 0.15 * subscribers
    d_plus_views = 0.05 * subscribers
    d_views = 0.01 * subscribers


    if views >= a_plus_views: 
        views_grade = "A+"
        views_grade_num = 1
    elif views < a_plus_views and views >= a_views:
        views_grade = "A"
        views_grade_num = 2
    elif views < a_views and views >= b_plus_views:
        views_grade = "B+"
        views_grade_num = 3
    elif views < b_plus_views and views >= b_views:
        views_grade = "B"
        views_grade_num = 4
    elif views < b_views and views >= c_plus_views:
        views_grade = "C+"
        views_grade_num = 5 
    elif views < c_plus_views and views >= c_views:
        views_grade = "C"
        views_grade_num = 6
    elif views < c_views and views >= d_plus_views:
        views_grade = "D+"
        views_grade_num = 7 
    elif views < d_plus_views and views >= d_views:
        views_grade = "D"
        views_grade_num = 8 
    else: 
        views_grade = "F"  
        views_grade_num = 9 
        #views bonus  
    if views_grade_num == 1:
       bonus_views = 0.25 
    elif views_grade_num == 2:
        bonus_views = 0.225
    elif views_grade_num == 3:
        bonus_views = 0.2
    elif views_grade_num == 4:
        bonus_views = 0.175
    elif views_grade_num == 5:
        bonus_views = 0.15
    else:
     bonus_views = 0 




    # Grading system for likes
    a_plus_likes = views * 0.06
    a_likes = views * 0.04
    b_plus_likes = views * 0.03
    b_likes = views * 0.02
    c_plus_likes = views * 0.015
    c_likes = views * 0.01
    d_plus_likes = views * 0.005
    d_likes = views * 0.001

    if likes >= a_plus_likes: 
        likes_grade = "A+"
        likes_grade_num = 1
    elif likes < a_plus_likes and likes >= a_likes:
        likes_grade = "A"
        likes_grade_num = 2
    elif likes < a_likes and likes >= b_plus_likes:
        likes_grade = "B+"
        likes_grade_num = 3
    elif likes < b_plus_likes and likes >= b_likes:
        likes_grade = "B"
        likes_grade_num = 4
    elif likes < b_likes and likes >= c_plus_likes:
        likes_grade = "C+"
        likes_grade_num = 5 
    elif likes < c_plus_likes and likes >= c_likes:
        likes_grade = "C"
        likes_grade_num = 6
    elif likes < c_likes and likes >= d_plus_likes:
        likes_grade = "D+"
        likes_grade_num = 7 
    elif likes < d_plus_likes and likes >= d_likes:
        likes_grade = "D"
        likes_grade_num = 8 
    else: 
        likes_grade = "F"  
        likes_grade_num = 9 

    if likes_grade_num == 1:
       bonus_likes = 0.125 
    elif likes_grade_num == 2:
        bonus_likes = 0.1
    elif likes_grade_num == 3:
        bonus_likes = 0.075
    elif likes_grade_num == 4:
        bonus_likes = 0.050
    elif likes_grade_num == 5:
        bonus_likes = 0.025
    else:
     bonus_likes= 0 

    # Grading system for engagement
    a_plus_eng = 90
    a_eng = 80
    b_plus_eng = 70
    b_eng = 60 
    c_plus_eng = 50
    c_eng = 40
    d_plus_eng = 30 
    d_eng = 20

    if engagement >= a_plus_eng: 
        eng_grade = "A+"
        eng_grade_num = 1
    elif engagement < a_plus_eng and engagement >= a_eng:
        eng_grade = "A"
        eng_grade_num = 2
    elif engagement < a_eng and engagement >= b_plus_eng:
        eng_grade = "B+"
        eng_grade_num = 3
    elif engagement < b_plus_eng and engagement >= b_eng:
        eng_grade = "B"
        eng_grade_num = 4
    elif engagement < b_eng and engagement >= c_plus_eng:
        eng_grade = "C+"
        eng_grade_num = 5 
    elif engagement < c_plus_eng and engagement >= c_eng:
        eng_grade = "C"
        eng_grade_num = 6
    elif engagement < c_eng and engagement >= d_plus_eng:
        eng_grade = "D+"
        eng_grade_num = 7 
    elif engagement < d_plus_eng and engagement >= d_eng:
        eng_grade = "D"
        eng_grade_num = 8 
    else: 
        eng_grade = "F"  
        eng_grade_num = 9

    if eng_grade_num == 1:
       bonus_eng = 0.2
    elif eng_grade_num == 2:
       bonus_eng = 0.175
    elif eng_grade_num == 3:
       bonus_eng = 0.15
    elif eng_grade_num == 4:
       bonus_eng = 0.125
    elif  eng_grade_num == 5:
       bonus_eng = 0.1

    else:
        bonus_eng = 0   

    # Grading system for comments
    a_plus_com = views * 0.04
    a_com = views * 0.03
    b_plus_com = views * 0.025
    b_com = views * 0.02
    c_plus_com = views * 0.015
    c_com = views * 0.01
    d_plus_com = views * 0.007
    d_com = views * 0.003

    if comment >= a_plus_com: 
        com_grade = "A+"
        com_grade_num = 1
    elif comment < a_plus_com and comment >= a_com:
        com_grade = "A"
        com_grade_num = 2
    elif comment < a_com and comment >= b_plus_com:
        com_grade = "B+"
        com_grade_num = 3
    elif comment < b_plus_com and comment >= b_com:
        com_grade = "B"
        com_grade_num = 4
    elif comment < b_com and comment >= c_plus_com:
        com_grade = "C+"
        com_grade_num = 5 
    elif comment < c_plus_com and comment >= c_com:
        com_grade = "C"
        com_grade_num = 6
    elif comment < c_com and comment >= d_plus_com:
        com_grade = "D+"
        com_grade_num = 7 
    elif comment < d_plus_com and comment >= d_com:
        com_grade = "D"
        com_grade_num = 8 
    else: 
        com_grade = "F"  
        com_grade_num = 9 

    if com_grade_num == 1:
     bonus_com = 0.1
    elif com_grade_num == 2:
         bonus_com = 0.075
    elif com_grade_num == 3:
         bonus_com = 0.05
    elif com_grade_num == 4:
         bonus_com = 0.025 
    elif com_grade_num == 5:
         bonus_com = 0.01
    else:
      bonus_com = 0  

    bonus = bonus_views + bonus_com + bonus_eng + bonus_likes


    # Final Grade Calculation
    total_grade_num = ((views_grade_num + likes_grade_num + eng_grade_num + com_grade_num) / 4)
    if bonus > 3:
        bonus = 3
    Scaled_Grade_num = total_grade_num - bonus
    bonus = str(bonus)


    if total_grade_num <= 1.5: 
        grade = "A+"
    elif total_grade_num <= 2.5:
        grade = "A"
    elif total_grade_num <= 3.5:
        grade = "B+"
    elif total_grade_num <= 4.5:
        grade = "B"
    elif total_grade_num <= 5.5:
        grade = "C+"
    elif total_grade_num <= 6.5:
        grade = "C"
    elif total_grade_num <= 7.5:
        grade = "D+"
    elif total_grade_num <= 8.5:
        grade = "D"
    else: 
        grade = "F" 

    if Scaled_Grade_num<= 1.5: 
         scale_grade = "A+"
    elif Scaled_Grade_num <= 2.5:
        scale_grade = "A"
    elif Scaled_Grade_num <= 3.5:
       scale_grade = "B+"
    elif Scaled_Grade_num <= 4.5:
       scale_grade = "B"
    elif Scaled_Grade_num <= 5.5:
       scale_grade = "C+"
    elif Scaled_Grade_num <= 6.5:
        scale_grade = "C"
    elif Scaled_Grade_num <= 7.5:
       scale_grade = "D+"
    elif Scaled_Grade_num <= 8.5:
        scale_grade = "D"
    else: 
        scale_grade = "F" 

    print("##########################")
    print("Final Results:") 
    print("Views Grade: " + views_grade)
    print("Likes Grade: " + likes_grade)
    print("Engagement Grade: " + eng_grade)
    print("Comments Grade: " + com_grade)

    print ("Bonus:" +  bonus)
    print("---------")
    print ("Final Grade:" + grade )
    print("Scaled Grade: " + scale_grade)
    print("##########################")
    exit_choice = input("Start Again: ")
    if  exit_choice.lower() == "y" or exit_choice.lower() == "yes" or  exit_choice.lower() == "":
       YT_Grade()
    elif exit_choice.lower() == "n" or exit_choice.lower() == "no":
        return YT_Analytics()
 print ("1.Title Generator")
 print ("2.Keyword Search")
 print ("3.YT Video Grade Calculator")
 print ("4.Exit")

 option = int(input("Choose An Option (1-4)"))
 clear_console()
 print("")
 (input("Press Enter To continue"))
 print("")
 if option == 1:
     YT_Title_Gen()
 if option == 2:
     Trend_Calculator()
 if option == 3:
     YT_Grade()
 if option == 4:
     clear_console()
     return menu()





def menu():
 clear_console()
 print("###########################")
 print ("Menu")
 print("1.Grade Calculators")
 print("2.Games")
 print("3.Youtube Analytics")
 print("4. Chat bot")
 print("5.Exit")
 print ("___________")
 option = int(input("enter option: "))
 print("")
 (input("Press Enter To continue"))
 clear_console()
 print("")
 if option == 1:
     grad_calculators()
 elif option == 2:
     games()
 elif option == 3:
    YT_Analytics()
 elif option == 4:
     clear_console()
     chat_bot()
 elif option == 5:
  clear_console()
  exit()

 input ("Press Enter To Continue")
 clear_console()
 print ("")


menu()