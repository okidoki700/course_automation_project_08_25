# practice_lesson_18/shopping_list.py
from write_read_to_file import write_to_file, read_from_file

def add_item_to_shopping_list(item):
    write_to_file("shopping_list.txt", item + "\n")

def get_shopping_list():
    return read_from_file("shopping_list.txt")

if __name__ == "__main__":
    add_item_to_shopping_list("Apples")
    add_item_to_shopping_list("Bananas")
    add_item_to_shopping_list("Carrots")
    print("Shopping List:")
    print(get_shopping_list())