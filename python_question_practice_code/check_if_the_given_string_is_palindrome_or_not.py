# Write A Python function to check whether given string is palindrome or not.
'''
What is Palindrome?
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
For example, "madam" and "A man, a plan, a canal: Panama" are palindromes.
In Real Life:
1. Data Validation: Palindromic sequences can be used in data validation checks to ensure data integrity.
2. Genetics: In DNA sequences, palindromic regions can play a role in the
    formation of secondary structures and are important in molecular biology.
3. Computer Science: Palindromic algorithms are used in various applications, including text processing and searching algorithms.
4. Recreational Mathematics: Palindromes are often explored in puzzles and mathematical games.
5. Literature and Art: Palindromic structures are sometimes used in poetry and art to create symmetry and balance.
'''
def is_palindrome(s):
    # Normalize the string by removing spaces and converting to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]
# Example usage:
if __name__ == "__main__":
    test_string = "A man, a plan, a canal: Panama"
    if is_palindrome(test_string):
        print(f'"{test_string}" is a palindrome.')
    else:
        print(f'"{test_string}" is not a palindrome.')
    test_string = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(test_string):
        print(f'"{test_string}" is a palindrome.')
    else:
        print(f'"{test_string}" is not a palindrome.')
        
# The function works by first normalizing the input string (removing non-alphanumeric characters and converting to lowercase),
# then checking if the normalized string is the same as its reverse.
input_string = input("Enter a string to check if it's a palindrome: ")
# Normalize the string: remove non-alphanumeric characters and convert to lowercase
temp_string = ''.join(c.lower() for c in input_string if c.isalnum())
reversed_string = temp_string[::-1]
if temp_string == reversed_string:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
