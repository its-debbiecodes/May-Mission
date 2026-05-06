print("HANDY CURRENCY CONVERTER".center(100))
while True:
    try:
        amount = int(input("\nHow much would you like to exchange? "))
        source_currency = input(f"\nWhat currency would you like to convert from? \n (USD), (GBP), (EUR) ").upper()
        target_currency = input("\nWhat currency would you like to convert to? \n (USD), (GBP), (EUR) ").upper()

        if source_currency not in ["USD", "GBP", "EUR"]:
            print("\nPlease enter a valid currency")
            continue

        elif target_currency not in ["USD", "GBP", "EUR"]:
            print("\nPlease enter a valid currency")
            continue

        if source_currency == "USD" and target_currency == "GBP":
            converted_amount = amount * 0.74
            print(f"\nThe converted amount is: {converted_amount}")

        elif source_currency == "USD" and target_currency == "EUR":
            converted_amount = amount * 0.85
            print(f"\nThe converted amount is: {converted_amount}")

        elif source_currency == "GBP" and target_currency == "USD":
            converted_amount = amount * 1.36
            print(f"\nThe converted amount is: {converted_amount}")

        elif source_currency == "GBP" and target_currency == "EUR":
            converted_amount = amount * 1.16
            print(f"\nThe converted amount is: {converted_amount}")

        elif source_currency == "EUR" and target_currency == "USD":
            converted_amount = amount * 1.18
            print(f"\nThe converted amount is: {converted_amount}")

        elif source_currency == "EUR" and target_currency == "GBP":
            converted_amount = amount * 0.86
            print(f"\nThe converted amount is: {converted_amount}")

    except ValueError:
        print("\nPlease enter a valid amount")
        continue


    again=input("\nWould you like to convert again? (y/n) ").upper()
    if again == "Y":
        continue
    else:
        print("THANK YOU FOR USING HANDY CURRENCY CONVERTER!")
        break
