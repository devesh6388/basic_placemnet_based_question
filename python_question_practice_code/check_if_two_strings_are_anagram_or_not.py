# Write a python function to check whether two strings are anagram or not.
'''
What is Anagram?
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
For example, the word "listen" is an anagram of "silent".
In Real Life:
1. Cryptography: Anagrams can be used in simple encryption techniques where messages are disguised by rearranging letters.
2. Puzzles and Games: Anagrams are commonly used in word games and puzzles to challenge players' vocabulary and problem-solving skills.
3. Linguistics: Studying anagrams can help linguists understand language patterns and letter frequency.
4. Marketing and Branding: Companies sometimes use anagrams to create catchy brand names or slogans that are memorable and engaging.
5. Literature: Authors may use anagrams as a literary device to add depth to characters or themes in their works.
'''
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for accurate comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2) 
# Example usage:
if __name__ == "__main__":
    string1 = "Listen"
    string2 = "Silent"
    if are_anagrams(string1, string2):
        print(f'"{string1}" and "{string2}" are anagrams.')
    else:
        print(f'"{string1}" and "{string2}" are not anagrams.')
    
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    if are_anagrams(string1, string2):
        print(f'"{string1}" and "{string2}" are anagrams.')
    else:
        print(f'"{string1}" and "{string2}" are not anagrams.')

# The function works by first normalizing the input strings (removing spaces and converting to lowercase),
# then sorting the characters in both strings and comparing the sorted results.
# If the sorted character lists are identical, the strings are anagrams; otherwise, they are not.
# Edge cases such as different lengths or presence of spaces and capitalization are handled by the normalization step.
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
temp_str1 = str1.replace(" ", "").lower()
temp_str2 = str2.replace(" ", "").lower()
if len(temp_str1) != len(temp_str2):
    print(f'"{str1}" and "{str2}" are not anagrams.')
else:
    sorted_str1 = sorted(temp_str1)
    sorted_str2 = sorted(temp_str2)
    if sorted_str1 == sorted_str2:
        print(f'"{str1}" and "{str2}" are anagrams.')
    else:
        print(f'"{str1}" and "{str2}" are not anagrams.')

