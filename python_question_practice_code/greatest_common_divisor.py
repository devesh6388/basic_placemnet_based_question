# Write a Python Function or code to find the Greatest Common Divisor (GCD) of two numbers.
"""
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both numbers without leaving a remainder.

Why GCD is important?
In Real Life:
1. Simplifying Fractions: GCD is used to reduce fractions to their simplest form by dividing both the numerator and denominator by their GCD.
2. Cryptography: GCD calculations are essential in algorithms like RSA for key generation and encryption
3. Computer Science: GCD is used in algorithms for tasks such as finding least common multiples, simplifying ratios, and in various optimization problems.
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
# Example usage:
if __name__ == "__main__":
    num1 = 56
    num2 = 98
    print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")