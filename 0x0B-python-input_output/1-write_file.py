#!/usr/bin/python3
"""writing a text file
   Return:
         number of characters written.
"""

def write_file(filename="", text=""):
    """Write a string to UTF8 tesxt file.

    Args:
        filename (str): the name of the file to write.
        text (str): the text to write to the  file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding='utf') as f:
        return f.write(text)
