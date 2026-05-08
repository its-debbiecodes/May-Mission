

print("Enter your details to access your account".title().center(100))
while True:
    attempts = 3
    correct_username = "debbie_brown"
    correct_password = "Gusguslee@23"
    logged_in = False

    while attempts > 0:
        user_name =(input("\nEnter your username: "))
        password =(input("Enter your password: "))
        attempts -= 1

        if user_name == correct_username and password == correct_password:
            print("login successful ✅")
            logged_in = True
            break

        if attempts <= 0:
            print("access denied ❌ \nNumber of attempts exceeded")

        else:
            print("access denied ❌ \nwrong username or password")
            print(f"\nYou have {attempts} attempts left")
            continue

    if logged_in:
        break

    try_again = input("\nDo you want to try again? (y/n): ")
    if try_again != "y" and try_again != "yes":
        print("\nHope to see you again")
        break


