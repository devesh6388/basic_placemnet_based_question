# Write Python function to calculate frequency of characters in a String.
'''
What is Character Frequency?
Character frequency refers to the number of times each character appears in a given string. It is a useful concept in various fields such as cryptography, data analysis, and natural language processing.
In Real Life:
1. Cryptography: Character frequency analysis is used in breaking ciphers by analyzing the frequency of letters in encrypted messages.
2. Text Analysis: Character frequency can help in understanding the characteristics of a text, such as identifying the language or author.
3. Data Compression: Algorithms like Huffman coding use character frequency to create efficient encoding schemes.
4. Natural Language Processing: Character frequency is used in various NLP tasks, including text classification and sentiment analysis.
5. Spell Checking: Character frequency can assist in developing algorithms for spell checking and autocorrect features.
'''
def calculate_character_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
# Example usage:
if __name__ == "__main__":
    input_string = "hello world"
    freq = calculate_character_frequency(input_string)
    print(f"Character frequency in '{input_string}': {freq}")
    
    input_string = input("Enter a string to calculate character frequency: ")
    freq = calculate_character_frequency(input_string)
    print(f"Character frequency in '{input_string}': {freq}")
# The function works by iterating through each character in the input string and maintaining a count of occurrences in a dictionary.
# Edge cases such as empty strings are handled by returning an empty dictionary.
input_string = input("Enter a string to calculate character frequency: ")
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(f"Character frequency in '{input_string}': {char_frequency}")
