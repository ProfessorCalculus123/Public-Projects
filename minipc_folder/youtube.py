
import os
import random
import time       
import threading
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def YT_Analytics():
    def YT_Title_Gen():
        global exit_choice, app
        app = 7
        while True:
            print("Youtube Title Generator")
            enter_keyword = input("Enter a keyword: ")
            if enter_keyword.lower() == 'q': break 
            hows = input("Do you want titles beginning with How? (y/n): ")

            enter_number = input("How many titles do you want: ")
            if enter_number.lower() == 'q': break 
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
            if audience.lower() == 'q': break 
            if not audience.isdigit():
                clear_console()
                print("RESULT", audience, " IS NOT VALID, PLEASE START AGAIN")
                continue
            audience = int(audience)
            
            competition = input("Enter Competition: ")
            if competition.lower() == 'q': break 
            if not competition.isdigit() or not (0 <= int(competition) <= 100):
                clear_console()
                print("RESULT", competition, " IS NOT VALID, PLEASE START AGAIN")
                continue
            competition = int(competition)
            
            vidiq = input("Enter VidIQ Score: ")
            if vidiq.lower() == 'q': break 
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
            if subscribers.lower() == 'q': break 
            if not subscribers.isdigit() or int(subscribers) < 0:
                clear_console()
                print("RESULT", subscribers, " IS NOT VALID, PLEASE START AGAIN")
                continue
            subscribers = int(subscribers)

            views = input("View Count:")
            if views.lower() == 'q': break 
            if not views.isdigit() or int(views) < 0:
                clear_console()
                print("RESULT", views, " IS NOT VALID, PLEASE START AGAIN")
                continue
            views = int(views)
            
            likes = input("Like Count:")
            if likes.lower() == 'q': break 
            if not likes.isdigit() or int(likes) < 0:
                clear_console()
                print("RESULT", likes, " IS NOT VALID, PLEASE START AGAIN")
                continue
            likes = int(likes)
            
            engagement = input("Engagement as % :")
            if engagement.lower() == 'q': break 
            if not engagement.isdigit() or int(engagement) < 0:
                clear_console()
                print("RESULT", engagement, " IS NOT VALID, PLEASE START AGAIN")
                continue
            engagement = int(engagement)
            
            comment = input("Comment Count:")
            if comment.lower() == 'q': break 
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
def run():
    YT_Analytics()
if __name__ == "__main__":
    run()