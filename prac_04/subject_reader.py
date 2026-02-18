"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    # print(data)
    display_subject_details(data)

def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    new_data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        data = [parts[0], parts[1], int(parts[2])]
        # print(data)  # See if that worked
        new_data.append(data)
        # print("----------")
    input_file.close()
    return new_data

def display_subject_details(data):
    """Display all subject details"""
    name_width = max(len(pair[1]) for pair in data)
    student_width = max(len(str(pair[2])) for pair in data)
    for index in data:
        print(f"{index[0]} is taught by {index[1]:<{name_width}} has {index[2]:>{student_width}} students.")


main()