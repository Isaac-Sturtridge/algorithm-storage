import re

def is_palindrome(s1):
    s1 = re.sub('\W', '', s1)
    if s1.lower() == s1[::-1].lower():
        return True
    return False

s1 = 'a man a plan a canal. Panama'
print(is_palindrome(s1))
