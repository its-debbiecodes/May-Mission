
print("WELCOME TO Age Calculator".title().center(50,"*"))
while True:
    try:
        birth_year= int(input("\nWhat is your birth year? "))
        current_year= int(input("What is the current year? "))
        if birth_year>current_year or birth_year<1900:
            print("\nHmmm.. that doesn't look right. Please try again.")
            continue

        age = current_year - birth_year
        print(f"\nYou are {age} years old")
        break

    except ValueError:
        print("\nPlease enter a valid year")
        continue