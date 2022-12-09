import string

def is_palindrome(i_string=None):
    if not i_string is None:
        i_string = i_string.lower()
        for s in string.punctuation:
            i_string = i_string.replace(s, "").replace(" ", "")

        if i_string == i_string[::-1]:
            return True
        else:
            return False

print(is_palindrome())
print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))