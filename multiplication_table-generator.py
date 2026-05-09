
print("Welcome to the multiplication table generator!".title().center(100))
while True:
    try:
        number = int(input("\nWhat number would you like to generate a multiplication table of? "))
        i= 1
        if number <= 0 or number > 100:
            print("\nEnter a number greater than 0 and less than 101!")
            continue

        while i <= 12:
            result = number * i
            print(f"{number} x {i} = {result}")
            i += 1

    except ValueError:
        print("\n That's not a valid number!")

    play_again = input("\nWould you like to play again? (y/n) ").lower()
    if play_again != "y" and play_again != "yes":
        break