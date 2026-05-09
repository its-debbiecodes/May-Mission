import time

print("Countdown Timer".center(50).title())
while True:
    try:
        seconds= int(input("\nHow many seconds would you like to wait? "))

        if seconds <= 0:
            print("\nEnter a valid number")
            continue

        while seconds > 0:
            print(seconds)
            seconds -= 1
            time.sleep(1)

        if seconds == 0:
            print("\nTimer Ends")

    except ValueError:
        print("\nPlease enter a valid number")

    play_again = input("\nWould you like to play again? (y/n) ".lower())
    if play_again != "y" and play_again != "yes":
        break




