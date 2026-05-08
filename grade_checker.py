print("Grade Checker".upper().center(100))
while True:
    try:
        score= int(input("\nWhat is your score? "))

        if score < 0 or score > 100:
            print("\nPlease enter a valid number")
            continue

        if score < 59:
            grade = "F"
            print("\nYour Grade is", grade)

        elif score <= 69:
            grade = "D"
            print("\nYour Grade is", grade)

        elif score <= 79:
            grade = "C"
            print("\nYour Grade is", grade)

        elif score <= 89:
            grade = "B"
            print("\nYour Grade is", grade)

        elif score <= 100:
            grade= "A"
            print("\nYour Grade is", grade)

    except ValueError:
        print("\nPlease enter a valid number")


    check_again = input("\nWould you like to check again? (y/n) ".lower())
    if check_again == "y" or check_again == "yes":
        continue
    elif check_again == "n" or check_again == "no":
        break