print("=" * 40)
print("  MATHEMATICAL CALCULATOR  ")
print("=" * 40)

status = "ON"
while status == "ON":
    print("Choose an operation")
    print("+   Addition")
    print("-   Subtraction")
    print("*   Multiplication")
    print("/   Division")
    print("\\   Floor Division")
    print("%   Modulus")
    print("^   Power")
    print("C   Clear Screen")
    print("OFF Turn Off Calculator")

    choice = input("\nEnter your choice: ").upper()

    if choice == "OFF":
        print("Calculator is OFF.")
        status = "OFF"
    elif choice == "C":
        print("\n" * 30)
        print("Screen Cleared.")
    elif choice == "+" or choice == "-" or choice == "*" or choice == "/" or choice == "\\" or choice == "%" or choice == "^":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == "+":
            print("Answer =", num1 + num2)
        elif choice == "-":
            print("Answer =", num1 - num2)
        elif choice == "*":
            print("Answer =", num1 * num2)
        elif choice == "/":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print("Answer =", num1 / num2)
        elif choice == "\\":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print("Answer =", num1 // num2)
        elif choice == "%":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print("Answer =", num1 % num2)
        elif choice == "^":
            print("Answer =", num1 ** num2)
    else:
        print("Invalid choice. Please try again.")