def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feets = int(parts[0])
    inches = int(parts[1])
    return {"feet":feets, "inches": inches}


def convert(feets, inches):

    meters = (feets * 0.3048) + (inches * 0.0254)
    return meters
