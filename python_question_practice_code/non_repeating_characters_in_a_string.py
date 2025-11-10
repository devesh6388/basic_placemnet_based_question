# Write a code in python to find non-repeating characters in a string.  
'''
What are Non-Repeating Characters?
Non-repeating characters in a string are those characters that appear only once in the entire string. They are unique and do not have any duplicates within the string.
In Real Life:
1. Data Cleaning: Identifying non-repeating characters can help in cleaning data by removing duplicates and retaining unique entries.
2. Cryptography: Non-repeating characters can be used in encryption algorithms to enhance security by ensuring uniqueness.
3. Text Analysis: In natural language processing, non-repeating characters can provide insights into the
    uniqueness of words or phrases in a text.
4. Usernames and IDs: When creating usernames or IDs, non-repeating characters can help in generating unique identifiers.
5. Puzzle Games: Many word games and puzzles utilize non-repeating characters to increase the challenge and complexity.
'''
def find_non_repeating_characters(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    non_repeating_chars = [char for char in s if frequency[char] == 1]
    return non_repeating_chars
# Example usage:
if __name__ == "__main__":
    input_string = "swiss"
    result = find_non_repeating_characters(input_string)
    print(f"Non-repeating characters in '{input_string}': {result}")
    
    input_string = input("Enter a string to find non-repeating characters: ")
    result = find_non_repeating_characters(input_string)
    print(f"Non-repeating characters in '{input_string}': {result}")
# The function works by first calculating the frequency of each character in the string using a dictionary,
# and then collecting those characters that have a frequency of one.
input_string = input("Enter a string to find non-repeating characters: ")
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
non_repeating_chars = [char for char in input_string if char_frequency[char] == 1]
print(f"Non-repeating characters in '{input_string}': {non_repeating_chars}")
