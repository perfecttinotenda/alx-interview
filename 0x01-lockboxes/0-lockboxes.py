#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered from 0 to n - 1, and they might have keys to other boxes.
Task: Write a method to find out if you can open all the boxes.
"""


def canUnlockAll(boxes):
    """
    This function checks if you can open all the boxes using keys inside them.
    It looks through the boxes, and if a key matches the box number, it opens the box.
    """
    """ Check if the input is a list """
    if type(boxes) is not list:
        return False

    elif len(boxes) == 0:
        return False

    """ Loop through each key (starting from the second box) """
    for key in range(1, len(boxes) - 1):
        """ Assume the box is not opened initially """
        box_checked = False

        """ Loop through all the boxes """
        for box_idx in range(len(boxes)):
            """ Check if the key matches the box number and is not in the same box """
            box_checked = key in boxes[box_idx] and key != box_idx

            """ If the box is opened, stop checking other boxes """
            if box_checked:
                break

        """ If the box is not opened, return False """
        if not box_checked:
            return box_checked

    """ If all boxes can be opened, return True """
    return True
