import bonus.d14be_modules
from bonus.d14be_modules import parse, convert

feet_inches = input("Enter feet and inches: ")

parsed = bonus.d14be_modules.parse(feet_inches)
result = bonus.d14be_modules.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet(s) and {parsed['inches']} inche(s) is equal to {result}m")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")