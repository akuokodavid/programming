#!/usr/bin/python3
# Author - King-David

def islower(c):
    """Function that checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
