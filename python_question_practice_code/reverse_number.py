# Write a Python function that takes an integer as input and returns the integer with its digits reversed.
def reverse_number(n):
    # Convert the integer to string, reverse the string and convert back to integer
    reversed_n = int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])
    return reversed_n

n = 12345
print(reverse_number(n))  # Output: 54321
# Example usage:
if __name__ == "__main__":
    number = 12345
    print(f"Original number: {number}")
    print(f"Reversed number: {reverse_number(number)}")
    
    number = -6789
    print(f"Original number: {number}")
    print(f"Reversed number: {reverse_number(number)}")

#  Easiest approach:- Check whether the number is negative or positive. If negative, convert to positive, reverse the digits, and then convert back to negative.
# If positive, simply reverse the digits.
# This function handles both positive and negative integers.
# The function works by converting the integer to a string, reversing the string using slicing, and then converting it back to an integer.
# We can also handle edge cases like zero and single-digit numbers, which will remain unchanged when reversed.
# devide by zero error is not applicable here as we are not performing any division operation.
# Check for input type is not necessary as the function is designed to take an integer input only.

num = int(input("Enter an integer to reverse: "))
temp = num
new_rversed = 0
while temp != 0: # Here you can check if the value is not greater than zero so, temp > 0; 
    digit = temp % 10
    new_rversed = new_rversed * 10 + digit
    temp //= 10
print(f"The reversed number is: {new_rversed}")