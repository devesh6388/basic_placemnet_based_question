# Write a python function of Perfect Number.
'''
What is Perfect Number?
A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding itself.
For example, 6 is a perfect number because its divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.
In Real Life:
1. Number Theory: Perfect numbers have been studied for their unique properties and relationships with prime numbers
2. Cryptography: Some cryptographic algorithms utilize properties of perfect numbers and related concepts in their design.
3. Computer Science: Algorithms for finding perfect numbers can be used to teach concepts of divisibility
and optimization.
4. Recreational Mathematics: Perfect numbers are often explored in puzzles and mathematical games.
5. Historical Significance: Perfect numbers have been known since ancient times and have been studied by mathematicians such as Euclid and Euler.
'''
def is_perfect_number(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
# Example usage:
if __name__ == "__main__":
    number = 28
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")
    
    number = int(input("Enter a positive integer to check if it's a perfect number: "))
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

# The function works by calculating the sum of all proper divisors of the given number and comparing it to the number itself.
# If they are equal, the number is perfect; otherwise, it is not.
# Edge cases like numbers less than or equal to 1 are handled by returning False, as perfect numbers are positive integers greater than 1.
# The function uses a generator expression to efficiently compute the sum of divisors.
num = int(input("Enter a positive integer to check if it's a perfect number: "))
temp = num
sum_of_divisors = 0
for i in range(1, temp):
    if temp % i == 0:
        sum_of_divisors += i
if sum_of_divisors == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    
