try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width != length:
        area = width * length
        print(area)
    else:
        exit("This is not a rectangle")
except ValueError:
    print("Please enter a valid number.")
