#!/usr/bin/python3
"""
Test file for List Operations Module
"""

from list_operations import (
    create_list, append_elements, insert_element, extend_list, 
    remove_last_element, sort_list, find_index
)

def print_list(lst):
    """Print the current state of the list."""
    print("List:", lst)

if __name__ == "__main__":
    my_list = create_list()
    my_list = append_elements(my_list, [10, 20, 30, 40])
    my_list = insert_element(my_list, 1, 15)
    my_list = extend_list(my_list, [50, 60, 70])
    my_list = remove_last_element(my_list)
    my_list = sort_list(my_list)
    index_30 = find_index(my_list, 30)
    
    print("Index of 30:", index_30)  # Expected output: Index of 30: 3
    print_list(my_list)  # Expected output: [10, 15, 20, 30, 40, 50, 60]

