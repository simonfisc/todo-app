try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = float(value / total_value * 100)
    print(f"That is {percentage}%")
except ZeroDivisionError:
    print("Your total value cannot be zero.")
except:
    print("You need to enter a number. Run the program again.")