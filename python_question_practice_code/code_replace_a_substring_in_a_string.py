# Write a code in python for code replace a substring in a string.
'''
What is Substring Replacement?
Substring replacement is the process of finding a specific sequence of characters (substring) within a larger string and replacing it with another sequence of characters. This operation is commonly used in text processing, data cleaning, and formatting tasks.
In Real Life:
1. Text Editing: Substring replacement is frequently used in text editors to find and replace words or phrases in documents.
2. Data Cleaning: In data preprocessing, substring replacement helps in standardizing data by replacing inconsistent formats or correcting errors.
3. Programming: Many programming languages provide built-in functions for substring replacement, making it easier for developers to manipulate strings.
4. Web Development: Substring replacement is used in web development for tasks such as URL rewriting and dynamic content generation.    
5. Natural Language Processing: In NLP, substring replacement can be used for tasks like tokenization, stemming, and lemmatization to prepare text for analysis.
'''
def replace_substring(original_string, to_replace, replacement):
    return original_string.replace(to_replace, replacement)
# Example usage:
if __name__ == "__main__":
    original_string = "Hello, world! Welcome to the world of Python."
    to_replace = "world"
    replacement = "universe"
    modified_string = replace_substring(original_string, to_replace, replacement)
    print("Original String:", original_string)
    print("Modified String:", modified_string)

    original_string = input("Enter the original string: ")
    to_replace = input("Enter the substring to replace: ")
    replacement = input("Enter the replacement substring: ")
    modified_string = replace_substring(original_string, to_replace, replacement)
    print("Modified String:", modified_string)
# The function works by utilizing Python's built-in string method `replace()`, which efficiently handles the replacement of all occurrences of the specified substring.
# Edge cases such as empty strings and substrings not found in the original string are handled gracefully
original_string = input("Enter the original string: ")
to_replace = input("Enter the substring to replace: ")
replacement = input("Enter the replacement substring: ")
modified_string = original_string.replace(to_replace, replacement)
print("Modified String:", modified_string)

