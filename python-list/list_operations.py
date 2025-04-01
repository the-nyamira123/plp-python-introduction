#!/usr/bin/python3
"""
List Operations Module
"""

def create_list():
    """Create and return an empty list."""
    return []

def append_elements(lst, elements):
    """Append multiple elements to the list."""
    lst.extend(elements)
    return lst

def insert_element(lst, index, value):
    """Insert a value at a specific position in the list."""
    lst.insert(index, value)
    return lst

def extend_list(lst, new_elements):
    """Extend the list with another list."""
    lst.extend(new_elements)
    return lst

def remove_last_element(lst):
    """Remove the last element from the list."""
    if lst:
        lst.pop()
    return lst

def sort_list(lst):
    """Sort the list in ascending order."""
    lst.sort()
    return lst

def find_index(lst, value):
    """Find and return the index of a value in the list."""
    return lst.index(value) if value in lst else -1

if __name__ == "__main__":
    my_list = create_list()
    my_list = append_elements(my_list, [10, 20, 30, 40])
    my_list = insert_element(my_list, 1, 15)
    my_list = extend_list(my_list, [50, 60, 70])
    my_list = remove_last_element(my_list)
    my_list = sort_list(my_list)
    index_30 = find_index(my_list, 30)
    
    print("Index of 30:", index_30)
    print("Final list:", my_list)
