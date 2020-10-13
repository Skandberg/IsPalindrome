def isPalindrome(word):
    word=word.lower().strip(' ')
    if word[::-1]== word:
        return True
    else:
        return False

