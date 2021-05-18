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