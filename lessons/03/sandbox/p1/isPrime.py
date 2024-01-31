# Iterative program to check if a number is prime in Python

def is_prime(number: int) -> bool:
    """ Determine primality: return 0 and 1"""
    if number < 2:
        return False

    # Iterate from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        # If the number is divisible
        # by any value in the range, it's not prime
        if number % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True
# end of is_prime()

# Driver function of the program

def main()-> None:
    """ driver function"""
    # Example usage
    user_input = int(input("\t Enter a number: "))
    result = is_prime(user_input)

    if result:
        print(f"\t {user_input}: Prime number")
    else:
        print(f"\t {user_input}: Not a prime number")
# end of main()
        
# place at bottom of the file
main() # call the main() function
