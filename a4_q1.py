"""
   Pythpn-121 2023W

   Name: Haani Syed
   Date: 2023-03-15
"""
from functions import char_prime, primeify, is_anagram #imports functions to be called in lines below.
def main():
    '''

    -------------------------------------------------------
    A4 Question 1's Main function with user friendly statements and calls to functions based on user input:
    Entry of 1 means def char_prime(my_char) is called, an uppercase alphabet is entered by user and respective prime returned.
    Entry of 2 means def primeify(my_string) is called, an uppercase string is entered by user and the corresponding product of prime numbers returned.
    Entry of 3 means def is_anagram(string1, string2) is called, two uppercase strings entered by user and the return is True if they're anagrams and False if not.
    -------------------------------------------------------
    Parameters:
        None directly for def main function. However there are many parameters for each of the respective functions called in this main function.
    Returns:
         No direct return. However 3 command based functions are called which have returns.
    -------------------------------------------------------
    '''
    print('Enter an UPPERCASE alphabet for my_char below ')#user friendly statement
    my_char = input('Enter an UPPERCASE Alphabet: ')
    print('The corresponding prime number for the entered alphabet is: ', char_prime(my_char)) #user friendly statement
    print('Enter a word/string in all uppercase ')
    my_string = input('Enter an UPPERCASE string: ')
    print('The corresponding product of primes for the entered string is: ', primeify(my_string))#user friendly statement
    print('Enter two UPPERCASE strings (String1, String2) to determine whether they are anagrams or not ')#user friendly statement
    string1 = input('Enter an UPPERCASE string/word for String1: ') #user uppercase string1 input.
    if not string1.isupper(): #Error check. If user enters non-uppercase. Error statement will be printed.
         print('Error. The string inputted was NOT all UPPERCASE') #Error statement.
    string2 = input('Enter a UPPERCASE string/word for String2: ') #user uppercase string2 input.
    if not string2.isupper(): #Error check. If user enters non-uppercase. Error statement will be printed.
            print('Error. The string inputted was NOT all UPPERCASE')
    print('The statement that the two entered UPPERCASE strings are anagrams is: ',is_anagram(string1, string2),'.')
        # above print statement will inform user whether it is True or False that the 2 entered uppercase strings are anagrams.

main() #call to main to let Q1 run

