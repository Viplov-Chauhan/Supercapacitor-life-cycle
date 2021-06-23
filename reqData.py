""" Opening the csv file and creating a new csv file with only required data """
import os
import csv


def get_file_path(filename):
    # CSV file to be pasted in the same folder as the main file
    dir_path = os.getcwd()
    # Path to the life cycle csv file
    file_path = os.path.join(dir_path, filename)
    return file_path


def reading_file(filename):
    file_path = get_file_path(filename)
    # Opening the original csv file
    file = open(file_path)
    # Reader object
    read_file = csv.reader(file)
    # Creating list of the read file
    file_list = list(read_file)
    # Closing file
    file.close()
    return file_list


def new_file(original_filename, new_filename):
    file_lines = reading_file(original_filename)

    # Marking empty lines
    index = -1
    indices = []
    for lines in file_lines:
        index += 1
        if not lines:
            indices.append(index)

    # Creating new file with the desired data
    lifecycle = get_file_path(new_filename)
    new = open(lifecycle, 'a')
    # Joining the elements of header by ',' to create csv file's first row
    new.write(','.join(file_lines[19]) + '\n')
    # Appending the data lines
    for lines in range(21, 171553, 1):
        line = ','.join(file_lines[lines])
        new.write(line + '\n')

    new.close()
    return lifecycle
