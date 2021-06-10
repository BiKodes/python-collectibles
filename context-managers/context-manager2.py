# context manager for file handling:

class MyFileHandler():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        # Originally, context object is None
        self.context_object = None

    # The context manager executes this first
    # Save the object state
    def __enter__(self):
        print("Entered the context!")
        self.context_object = open(self.filename, self.mode)

        return self.context_object

    # The context manager finally executes this before exiting
    # Information about any Exceptions encountered will go to
    # the arguments (type, value, traceback)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context....")
        print(f"Type: {exc_type}, Value: {exc_val}, Traceback: {exc_tb}")

        # Close the file
        self.context_manager.close()
        # Finally, restore the context object to it's old state (None)
        self.context_object = None

# We're simply reading the file using our context manager
with MyFileHandler('input.txt', 'r') as file_handle:
    for line in file_handle:
        print(line)












