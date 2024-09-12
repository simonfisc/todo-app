feet_inches = input("Enter feet and inches: ")
def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feets = int(parts[0])
    inches = int(parts[1])
    return {"feet":feets, "inches": inches}

def convert(feets, inches):

    meters = (feets * 0.3048) + (inches * 0.0254)
    return meters

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet. and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")