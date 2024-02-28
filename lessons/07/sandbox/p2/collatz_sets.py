def collatz_conjecture(n):
    sequence = set()
    
    while n != 1:
        if n in sequence:
            # Detected a cycle, exit to avoid infinite loop
            break        
        sequence.add(n)        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.add(n)
    return sequence

def main():
    try:
        starting_number = int(input("Enter a positive integer to start the Collatz sequence: "))        
        if starting_number <= 0:
            raise ValueError("Please enter a positive integer.")        
        collatz_sequence = collatz_conjecture(starting_number)
        print(f"Collatz sequence starting from {starting_number}:")
        print(collatz_sequence)
        print(f"Length of the sequence: {len(collatz_sequence)}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
