with open('my_file.txt') as my_file:
    get_data = my_file.read()

# Context Manager as Class:

class open_file():
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with open_file('file_name.txt', 'w') as f:
    f.write('Context_Manager class is working')

print(f.closed)

# try to handle the error:
class open_file():
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Error has been handled")
        self.file.close()
        return True

# Context Manager as Generator:
# Creating a context manager as a function,
from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    f = open(file_name, mode)

    try:
        yield f
    except Exception:
        print("Error has been handled")
    finally:
        f.close()

with open_file('file_name.txt', 'w') as f:
    f.write('Context_Manager class is working')


















