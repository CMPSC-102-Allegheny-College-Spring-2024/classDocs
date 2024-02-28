def collatz_conjecture(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    # Get user input for the starting number
    starting_number = int(input("Enter a positive integer to start the Collatz sequence: "))
    if starting_number <= 0:
        print("Please enter a positive integer.")
        return

    # Generate and print the Collatz sequence
    result_sequence = collatz_conjecture(starting_number)
    print(f"The Collatz sequence starting with {starting_number}")
    print(f"{result_sequence}")
    print(f"Length of the sequence: {len(result_sequence)}")

if __name__ == "__main__":
    main()
