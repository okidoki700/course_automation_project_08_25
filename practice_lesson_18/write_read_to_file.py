def write_to_file(filename, content):
    """
        Write content to a file.

        Args:
            filename (str): The name of the file to write to
            content (str): The content to write to the file

        File Modes:
            'r'  - Read mode (default). Opens file for reading, error if file doesn't exist.
            'w'  - Write mode. Creates new file or overwrites existing file.
            'a'  - Append mode. Adds content to end of file without overwriting.
            'x'  - Exclusive creation. Creates new file, error if file exists.
            'r+' - Read and write. File must exist.
            'w+' - Write and read. Overwrites existing file.
            'a+' - Append and read. Creates file if it doesn't exist.
            'rb' - Read in binary mode.
            'wb' - Write in binary mode.
            'ab' - Append in binary mode.

        Note: This function uses 'a' (append) mode, which adds content to the end
              of the file without overwriting existing content.
        """
    file = open(filename, 'a') # Open the file in write mode
    file.write(content)
    file.close()


def read_from_file(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content



for i in range(3):
    write_to_file("example1.txt", f"This is a new line {i+1}\n")

print(read_from_file("example1.txt"))

# write_to_file("example1.txt", "\nHave a great day!\n")

# # Output: Hello, World!