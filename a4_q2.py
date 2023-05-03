"""
   CISC-121 2023W

   Name: Haani Syed
   Student Number: 20331181
   Email: 21ahs7@queensu.ca
   Date: 2023-03-15

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""
#imports important functions needed to be able to run the main radix sort function.
from functions import char_prime, string_to_list_of_primes, recursive_radix_sort, max_number_for_radix, radix_sort
def main():
    '''

    -------------------------------------------------------
    A4 Q2's main function
    Radix sort is a recursive sort that segments the lists into “buckets.”
    This can be done in a variety of capacities, but the most common is through position within an integer.
    The user is to enter a my_string input (UPPERCASE ONLY) for which the respective list of primes is then returned with a user friendly statement.
    The function which returned the associated list of primes (string_to_list_of_primes) is then set to variable arr as it is taken in as parameter in the main radix sort function
    which will output the sorted array in ascending order.
    -------------------------------------------------------
    Parameters:
        No direct parameters for the main function. However, there are parameters for each of the functions that were created to assist the main radix sort function (radix_sort).
        in fulfilling, it's purpose.

    Returns:
        No direct returns for the main function. However, string_to_list_of_primes is called and will return the respective list of primes unsorted.
        the main radix sort function (radix_sort) will return the sorted array in ascending order.
    -------------------------------------------------------
    '''
    my_string = input('Enter an UPPERCASE string: ') #user input uppercase string for string_to_list_of_primes function's conversion.
    print('The associated list of prime numbers for this UPPERCASE string/word is: ', string_to_list_of_primes(my_string)) #user friendly print statement
    arr = string_to_list_of_primes(my_string) #turns string_to_list_of_primes into a variable so it can be taken in as a parameter by the main radix sort function.
    print('The sorted version of that list of prime numbers sorted by Radix Sort in ascending order is: ', radix_sort(arr)) #user friendly print statement


main() #call to main to let Q2 run