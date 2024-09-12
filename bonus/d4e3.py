ranking = ['John', 'Sen', 'Lisa']
name = input("input the person's name:")
matches = []
x = 0

for match in ranking:
    if name in match:
        print(x)
    else:
        x += 1