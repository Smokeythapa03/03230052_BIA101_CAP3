################################
# https://github.com/Smokeythapa03/03230052_BIA101_CAP3
# LEELA THAPA
# BBI 'A'
# 03230052
################################

# REFERENCES
# https://docs.python.org/3/tutorial/inputoutput.html
# https://www.w3schools.com/python/python_file_open.asp
################################

# SOLUTION
# Your Solution Score:  485428
################################

def read_input(file_path):
    """
    Reads the input file and returns a list of lines.
    :param file_path: Path to the input file
    :return: List of lines from the file
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def extract_number(line):
    """
    Extracts the first and last digits from a given line and forms a two-digit number.
    :param line: A single line from the input file
    :return: A two-digit number formed by concatenating the first and last digits
    """
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char

    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0

def print_solution(file_path):
    """
    Reads the input file, calculates the total sum of the two-digit numbers formed from each line,
    and prints the solution.
    :param file_path: Path to the input file
    """
    lines = read_input(file_path)
    total_sum = 0

    for line in lines:
        number = extract_number(line)
        total_sum += number

    print(f"The total sum from the given input file {file_path} is {total_sum}")

input_file_path = '052.txt'  

print_solution(input_file_path)
