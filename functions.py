"""
   CISC-121 2023W

   Name: Haani Syed
   Student Number: 20331181
   Email: 21ahs7@queensu.ca
   Date: 2023-03-15

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""
"""
-------------------------------------------------------
MAIN CODE FOR QUESTION 1
-------------------------------------------------------
"""
def char_prime(my_char):
    '''

    -------------------------------------------------------
    Converts an uppercase letter to a unique prime number Based on the conversion matching A-Z to prime numbers:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
    -------------------------------------------------------
    Parameters:
     my_char - a char in ABCDEFGHIJKLMNOPQRSTUVWXYZ (char)
    Returns:
         prime_int = a prime number unique to the letter
    -------------------------------------------------------
    '''
    #below dictionary with mapping: key - char, value - prime as required and mentioned in footnote of A4
    prime_numbers_mapping = {'A':2, 'B':3, 'C':5, 'D':7, 'E':11, 'F':13, 'G':17, 'H':19, 'I':23, 'J':29, 'K':31, 'L':37, 'M':41, 'N':43, 'O':47, 'P':53, 'Q':59, 'R':61, 'S':67, 'T':71, 'U':73, 'V':79, 'W':83, 'X':89, 'Y':97, 'Z':101}
    prime_int = prime_numbers_mapping[my_char] #prime_int var assigned for value of prime_numbers_mapping at 'my_char' entered by user.
    return prime_int #returns respective prime number
#print(char_prime('C'))
#the line above is a test print proving that the function functions

def primeify(my_string):
    '''

    -------------------------------------------------------
    RECURSIVELY gives the product of primes corresponding to the letters 4 in the string
    -------------------------------------------------------
    Parameters:
    my_string: - any UPPERCASE string (str)
    Returns:
        The product of all primes for each letter.
    -------------------------------------------------------
    '''
    if len(my_string) == 0: #base case: when len(my_string) == 0 equals zero
        return 1 #recursive process repeated for each char in string until base case reached. Would then return 1.
    else: #recursive case: when len(my_string) != 0 doesn't equal zero
        character = my_string[0] #extracts 1st char from string entered and assigns to var character
        char_prime_variable = char_prime(character) #char_prime_variable assigned to function call of char_prime with parameter character
        prime_product = char_prime_variable * primeify(my_string[1:]) #multiplies char_prime(character)'s variable with primeify(all other chars in string)

    return prime_product #returns product of primes (int)
#print(primeify('NANA'))
#the line above is a test print proving that the function functions

def is_anagram(string1, string2):
    '''

    -------------------------------------------------------
    Determines if two strings are anagrams (also known as exact same word) of each other
    -------------------------------------------------------
    Parameters:
    string1: any UPPERCASE string (str)
    string2: any UPPERCASE string (str)
    Returns:
         value #whether or not they are anagrams (Boolean)
    -------------------------------------------------------
    '''
    if primeify(string1) != primeify(string2): #if they (the 2 strings) are not anagrams will return False
        return False #return statement
    else: #will return True if they (the 2 strings) are anagrams
        return True #return statement
#print(is_anagram('FISH', 'DOG'))
#the line above is a test print proving that the function functions


"""
-------------------------------------------------------
MAIN CODE FOR QUESTION 2
-------------------------------------------------------
"""

def string_to_list_of_primes(my_string):
    '''

    -------------------------------------------------------
    takes a string as input and converts into a list of prime numbers.
    -------------------------------------------------------
    Parameters:
     my_string: any UPPERCASE string (str).
    Returns:
         value #list of primes.
    -------------------------------------------------------
    '''
    list_of_primes = [] #list of primes to be returned
    for char in my_string: #for each character in the string entered
        list_of_primes.append(char_prime(char)) #to list of primes add the prime equivalent for each respective char in string entered.
    return list_of_primes #returns list of prime numbers.
#string1_list = string_to_list_of_primes('BANANA') #example of what a user can enter for string1
#string2_list = string_to_list_of_primes('ABC') #example of what a user can enter for string2
#combined_primes_list = string1_list + string2_list #combines string1 and string2 into 1 list.
#print(combined_primes_list)
#the line above is a test print proving that the function functions

def recursive_radix_sort(arr, exponent):
    '''

    -------------------------------------------------------
    sets up the recursion - base case and recursive case which is to be used in the main radix sort.
    Base Case: when exponent equals to zero.
    Recursive Case: when exponent is not equal to zero.
    Also creates 10 distinct lists to let algorithm make sure buckets segment component of radix_sort is being completed.
    -------------------------------------------------------
    Parameters:
    arr: any UPPERCASE string (str)
    exponent: any exponent value
    Returns:
        Value #List. This function doesn't return the final sorted array, rather it is called within the main radix sort and fulfills a certain purpose there.
    -------------------------------------------------------
    '''
    if exponent == 0: #base case: is when exponent equals zero.
        return arr
    buckets_aka_lists = [[] for i in range(10)] #creating 10 distinct lists lets algorithm make sure buckets component of radix sort is being completed.
    for number in arr: #recursive case: is when exponent is not equal to zero.
        digit = (number // exponent) % 10
        buckets_aka_lists[digit].append(number) #distributes numbers into respective buckets based on 'specific digit'.
    arr=[] #list to be returned.
    for bucket in buckets_aka_lists: #loops over each bucket (aka list) in list of buckets (buckets_aka_lists)
        arr = arr + bucket #adds bucket to arr for each loop iteration
    return arr #returns array of primes. The purpose of this function is to set up recursion as this function is called later in main radix_sort function.
#print(recursive_radix_sort(combined_primes_list, 4))
#the line above is a test print proving that the function functions

def max_number_for_radix(arr): #linear search for max number used in radix sort function
    '''

    -------------------------------------------------------
    Linear Search finds the max number in the entered array and this function is used in the main radix sort function.
    -------------------------------------------------------
    Parameters:
    arr: any UPPERCASE string (str)
    Returns:
         biggest/maximum number found in the associated list of primes for the string entered.
    -------------------------------------------------------
    '''
    max_number = arr[0] #1st index of arr
    for number in arr: #for int in list
        if number > max_number: #if int greater than arr[0]
            max_number = number #sets them equal
    return max_number #retuns max number from the array of prime numbers for the respective associated string entered.
#print(max_number_for_radix(string2_list))
#the line above is a test print proving that the function functions

def radix_sort(arr): #ascending order sort
    '''

    -------------------------------------------------------
    Using the strings we had entered from Q1 (string1 and string2 that may or may not be anagrams),
    we noticed that we have both a string or a list of primes. We'll now sort this string,
    by applying a new sort to the list of primes (ascending order).
    Main Radix Sort: Radix sort is a recursive sorting algorithm that segments the lists into “buckets.” Can be
    done in a variety of capacities, but the most common is through position within an integer.
    -------------------------------------------------------
    Parameters:
     arr: any UPPERCASE string (str) unsorted when inputted into program.
    Returns:
         the associated list in sorted form in ascending order for the associated UPPERCASE string entered.
    -------------------------------------------------------
    '''
    max_number_var = max_number_for_radix(arr) #setting linear search (max) to max_number_var variable to use in radix sort.
    exponent = 1
    while max_number_var // exponent > 0: #while condition
        arr = recursive_radix_sort(arr, exponent) #arr variable assigned value of recursive_radix_sort function
        exponent *= 10
    return arr #returns final sorted array of primes in ascending order for the respective string once entered by user.
#print(radix_sort(string2_list))
#the line above is a test print proving that the function functions