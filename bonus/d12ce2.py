password = "AbCdEfGhI"
def strength(password):
    result = {}

    if len(password) < 8:
        result["length"] = False
    else:
        result["length"] = True

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True
    result["digit"] = digit
    result["uppercase"] = uppercase

    if all(result.values()):
        # Return "strong password" if all attributes are True
        return "Strong Password"
    else:
        return "Weak Password"


print(strength(password))