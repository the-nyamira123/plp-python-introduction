#!/usr/bin/python3
"""
Test file for file read & write with error handling
"""

from file_rw import modify_file

if __name__ == "__main__":
    input_file = input("Enter the name of the file to read: ")
    output_file = input("Enter the name of the new file to write to: ")

    modify_file(input_file, output_file)
