# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.

import os

def print_directory_contents(path='/pictures'):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")

# Call the function to print the contents of the current directory
print_directory_contents()

# Problem-04 is Completed