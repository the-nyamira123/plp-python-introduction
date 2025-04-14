#!/usr/bin/python3
"""
Reads a file, modifies its content, and writes to a new file.NYAMIRA AUTHOR.
Includes error handling for missing or unreadable files.
"""

def modify_file(input_filename, output_filename):
    """
    Reads content from input_filename,
    converts it to uppercase,
    and writes it to output_filename.
    """
    try:
        # Try opening the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Example modification: to uppercase

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print("✅ File was successfully modified and saved.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except IOError:
        print("❌ Error: Unable to read or write to the file.")

