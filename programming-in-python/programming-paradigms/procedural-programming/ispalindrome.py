def isPalindrome(str):
    """
    Function that checks if a word is a palindrome or not.

    Args:
        str: the word to be compared.

    Returns:
        bool: result after comparing if the word is a palindrome.
    """
    startIndex = 0
    endIndex = len(str) - 1

    while startIndex < endIndex:
        if str[startIndex] != str[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1

    return True

# Testing the function
print(isPalindrome('casa'))  # Expected output: False
print(isPalindrome('alola')) # Expected output: True