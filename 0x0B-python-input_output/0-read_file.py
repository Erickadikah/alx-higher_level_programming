#!/usr/bin/python3
#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""


def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout.
    Args:
        - filename: name of the file
    """
<<<<<<< HEAD
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
=======

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
>>>>>>> 0c70077b17684da736eaf2f70339886b11b66dd2
