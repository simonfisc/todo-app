filenames = ["../files/a.txt", "../files/b.txt", "../files/c.txt"]

for filename in filenames:
    file = open(filename, "r")
    content = file.read()
    print(f"{content}")
    file.close()