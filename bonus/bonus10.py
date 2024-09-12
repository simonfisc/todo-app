password = input("Enter new password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)
    print("Password must be at least 8 characters long.")

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

upper = False
for i in password:
    if i.isupper():
        upper = True
result.append(upper)

print(result)