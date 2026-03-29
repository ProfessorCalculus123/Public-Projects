import main
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    

def grad_calculators():
    clear_console()
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