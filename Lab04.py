#Author: Ellie Reece
#Date: 4/4/2022
#Description: Lab 04 - Files and Lists

import random
def is_palindrome(s):
    """
    is_palindrome tests if the input string is a palindrome (word spelled the same
    forward and backwards)
    : param : str - string determining if a palindrome
    : return : True - parameter is a palindrome
               False - parameter is not a palindrome
    """
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

is_palindrome("racecar")
#Challenge 1
def challenge1():
    #Open File for Reading
    infile = open("dictionary.txt", "r")
    #Read All Lines of the Input File into a List
    word_list = infile.read().splitlines()
    print(word_list)
    word = random.choice(word_list)
    if is_palindrome(word) == True:
        print(str)
        
challenge1()


