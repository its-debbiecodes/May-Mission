
def add (a:float, b:float) -> float:
    return a+b
def sub (a:float, b:float) -> float:
    return a-b
def mul (a:float, b:float) -> float:
    return a*b
def div (a:float, b:float) ->float:
    return a/b

def valid_number(prompt:str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nPlease enter a number.\n")

def main():
    print(f"\n\033[45m Welcome to the Basic Calculator!\033[0m".center(50))
    operations={"+" : add,
                "-" : sub,
                "*" : mul,
                "/" : div,
                }
    while True:
        num_1 =valid_number("\nEnter your first number: ")
        num_2 = valid_number("\nEnter your second number: ")
        op_symbol= input("\nEnter your operator choice (\n+,\n-,\n*,\n/) : ").lower()
        cal_function = operations.get(op_symbol)

        if cal_function:
            try:
                result = cal_function(num_1, num_2)
                print(f"\nresult: {num_1}{op_symbol}{num_2}= {result}\n")

            except ZeroDivisionError as e:
                print(f"\n{e}:Number cannot be divided by 0\n")

        else:
            print("\nPlease enter a valid operator (+,-,*,/)!\n")

        try_again = input("\nWould you like to try again? (y/n) ").lower()
        if try_again != "y" and try_again != "yes":
            break

if __name__ == "__main__":
    main()


