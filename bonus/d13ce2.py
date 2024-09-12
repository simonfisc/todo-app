def get_nr_items(text: str):
    text = text.split(',')
    print(text)
    nr_items = len(text)
    print(nr_items)
    return nr_items


get_nr_items("john,lise, teresa")