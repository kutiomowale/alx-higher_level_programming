#!/usr/bin/python3
"""Search and update
Function definition for append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Search and update

    A function that inserts a line of text to a file,
    after each line containing a specific string

    File permission or file doesn't exist exceptions are not managed

    Args:
        filename (str): The name of the file
        search_string (str): Insert criteria
        new_string (str): Text to insert
    """
    # Open the file in read mode
    with open(filename, "r", encoding="utf-8") as f:
        # Get a list of all lines
        list_of_lines = list(f)
    # Close the file

    # Loop through the indexes of the list of lines
    for i in range(len(list_of_lines)):
        # Change lines containing search_string to line + new_string
        if search_string in list_of_lines[i]:
            list_of_lines[i] += new_string

    # Open the file in write mode
    with open(filename, "w", encoding="utf-8") as f:
        # Write each new line to the file
        for line in list_of_lines:
            f.write(line)
    # Close the file
