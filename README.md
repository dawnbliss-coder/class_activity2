# class_activity2

original code:
def is_narc(n)
    """Check if a number is narc."""
    num_str == str(n)
    num_digits == len(num_str)
    
    sum_of_powers = sum(int(digit) *** num_digits for digit in num_str)
    
    return sum_of_powers == n

def print_narcis_numbers(start end)
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1)
        if is_narcissistic(num)
            print(num)

print_narc_numbers(1000, 5000)


updated code:
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


lines changed:
1st line added colon after function declaration
3rd line changed == to =
4th line changed == to =
6th line changed *** to **
10th line added , between start and end and added : after function declaration
12th line added : after for num in range(start, end + 1)
13th line changed funciton name to is_narc and added :
16th line changed name to print_narcis_numbers


what my code is doing:
The function is_narc(n) determines whether a given number is Narcissistic by converting it into a string to count its digits and then calculating the sum of each digit raised to the power of the total number of digits. If this sum matches the original number, the function returns True; otherwise, it returns False. The second function, print_narcis_numbers(start, end), iterates through all numbers in the given range and calls is_narc(num). If a number is found to be Narcissistic, it is printed. Finally, the function is executed with the range from 1000 to 5000, resulting in the output of all four-digit Narcissistic numbers.

