def isPalindrome(word):
    if word.lower()[::-1]==word.lower():
        return True
    else:
        return False

