# Author: Aiishwin Muraliy
# Date: April 10, 2021
# Subject: Palindrome Checker
# Description: This function checks if a word is a palindrome or not

def palindrome(x: str) -> bool:
    if x == x[::-1]:
        return True
    else:
        return False
