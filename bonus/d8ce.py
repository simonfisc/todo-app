try:
    with open("files/docs.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("File not found")


