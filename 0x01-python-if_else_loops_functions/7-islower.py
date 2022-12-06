# a function that checks for lowercase character
# without using str.upper() and str.isupper()
# Returns True if c is lowercase, Returns False otherwise

def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
