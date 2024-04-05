def reverse(text):
    """
    A recursive function that reverses a given string text

    Parameter
    ---------
    text: str
        text to be reversed
    
    Returns
    ---------
    reversed text
    """
    text = text.strip()
    if (len(text) <= 1):
        return text
    first = text[0]
    text = text[1:]
    return reverse(text) + first
    

def is_palindrome(text):
    """
    A recursive function that takes in an input string and checks whether it is a valid palindrome

    Parameter
    ---------
    text: str
        text that will be checked if it is valid

    Returns
    ---------
    True: bool or False: bool
    """
    text = text.lower().strip()
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])
        
        

