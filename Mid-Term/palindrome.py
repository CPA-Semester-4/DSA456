def is_palindrome(word, st = 0, end = None):
    if end == None:
        end = len(word) - 1

    if st >= end:
        return True
    else:
        if word[st] != word[end]:
            return False
        else:
            return is_palindrome(word, st+1, end-1)


print(is_palindrome("naman"))
print(is_palindrome("hello"))