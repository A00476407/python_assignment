# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:19:20 2023

@author: kaman
"""

def stack(our_list, operation, new_element=0):
    """
    Stack

    Parameters
    ----------
    our_list : existing list such as [1,2,3].
    operation: 'add' or 'remove'
    new_element: element to be added or removed, such as 4

    Returns
    -------
    list: Updated list

    """

    if (operation == 'add'):
        new_list.insert(0, new_element)
    elif (operation == 'remove'):
        new_list.pop(0)
    return new_list

def queue(our_list, operation, new_element=0):
    """
    Queue

    Parameters
    ----------
    our_list : existing list such as [1,2,3].
    operation: 'add' or 'remove'
    new_element: element to be added or removed, such as 4

    Returns
    -------
    list: Updated list

    """

    if (operation == 'add'):
        new_list.append(new_element)
    elif (operation == 'remove'):
        new_list.pop(0)
    return new_list

new_list = [1,2,3,4]
print("Adding new element to the stack")
new_list = stack(new_list, 'add', 0)
print(new_list)
print("Adding remove an element from stack")
new_list = stack(new_list, 'remove')
print(new_list)
print("Adding new element to the queue")
new_list = queue(new_list, 'add', 5)
print(new_list)
print("Adding remove an element from queue")
new_list = queue(new_list, 'remove')
print(new_list)