def get_todos(filepath_local="files/todos.txt"):
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath_local, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath_local="files/todos.txt"):
    """ Write a to-do item list in the text file."""
    with open(filepath_local, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())