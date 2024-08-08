def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE

    try:
        # Open and read the entire file
        with open(file_name, "r") as file:
            data = file.read()
            #print(data)  # Print the contents of the file
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")
        return None
    
    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE

    try:
        with open(file_name, "r") as file:
            # Create a list to store the stripped lines
            lines = []
            for line in file:
                stripped_line = line.strip()  # Remove leading and trailing whitespace
                lines.append(stripped_line)   # Add the stripped line to the list
            return lines
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")
        return None
    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    lines = file_contents.splitlines()
    if lines:
        first_line = lines[0]
        with open(output_filename, 'w') as file:
            file.write(first_line)
        return file
    
    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE

    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    even_lines = [lines[i] for i in range(1, len(lines), 2)]
    return even_lines

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    reversed_lines = lines[::-1]
    
    print(reversed_lines)
    return reversed_lines


    raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("../programming-in-python/programacion-basica/errors-exceptions-filehandling/ejercicio/sampletext.txt")

    print(read_file_into_list("../programming-in-python/programacion-basica/errors-exceptions-filehandling/ejercicio/sampletext.txt"))
    
    write_first_line_to_file(file_contents, "../programming-in-python/programacion-basica/errors-exceptions-filehandling/ejercicio/online.txt")
    print(read_even_numbered_lines("../programming-in-python/programacion-basica/errors-exceptions-filehandling/ejercicio/sampletext.txt"))
    print(read_file_in_reverse("../programming-in-python/programacion-basica/errors-exceptions-filehandling/ejercicio/sampletext.txt"))

if __name__ == "__main__":
    main()