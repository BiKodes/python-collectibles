# Change the name of each folder replacing ‘f’ with ‘folder’
# Printing the structure of the folders in a neat tree form.

folders = ['f1', ['f2_1', 'f2_2'], ['f3_1', ['f3_1_1', 'f3_1_2']]]

def print_folders(folders, level):
    for folder in folders:
        if not isinstance(folder, list):
            folder = folder.replace('f', 'folder ')
            print(f"|{level * '----'} {folder}")

        else:
            print_folders(folder, level + 1)

print_folders(folders, 0)


names = ["Adam", ["Bob", ["Chet", "Cat", ], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]

def count_leaf_items(item_list):
    """
        Recursively counts and returns the number of leaf items in a (potentially nested) list.
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count

count_leaf_items(names)
count_leaf_items([1, 2, 3, 4])
count_leaf_items([1, [2.1, 2.2], 3])
count_leaf_items([])
count_leaf_items(names)

# Adding some print() statements helps to demonstrate the sequence of recursive calls and return values:

def count_leaf_items(item_list):
    """
        Recursively counts and returns the number of leaf items in a (potentially nested) list.
    """
    print(f"List: {item_list}")
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += count_leaf_items(item)

        else:
            print(f"Counted leaf item \"{item}\"")
            count += 1

    print(f"-> Returning count {count}")
    return count

# Detect Palindromes:















