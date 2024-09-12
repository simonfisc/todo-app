def foo(temperature_local):
    if temperature_local > 25:
        return "Hot"
    elif 15 < temperature_local < 25:
        return "Warm"
    else:
        return "Cold"


print(foo(15))