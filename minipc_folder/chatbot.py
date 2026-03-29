
import main
import random
import os
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def chat_bot():
    clear_console()
    
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
def run():
    chat_bot()
if __name__ == "__main__":
    run()