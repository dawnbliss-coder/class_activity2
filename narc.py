def is_narc(n): #1
    """Check if a number is narc."""
    num_str = str(n) #1
    num_digits = len(num_str) #1
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) #1
    
    return sum_of_powers == n

def print_narcis_numbers(start, end) : #2
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): #1
        if is_narc(num): #2
            print(num)

print_narcis_numbers(1000, 5000) #1