# Write code to check if two strings match where one string contains wildcard characters.

'''
What are Wildcard Characters?
Wildcard characters are special symbols used in string matching that can represent one or more characters. The most common wildcard characters are:
1. Asterisk (*): Represents zero or more characters.
2. Question Mark (?): Represents exactly one character.
In Real Life:
1. File Searching: Wildcards are commonly used in file systems to search for files with specific patterns (e.g., *.txt to find all text files).
2. Database Queries: Wildcards are used in SQL queries to filter results based on patterns (e.g., WHERE name LIKE 'J%n' to find names starting with 'J' and ending with 'n').
3. Command Line Interfaces: Wildcards are used in command line operations to specify groups of files or directories.
4. Text Editors: Many text editors support wildcard searches to find and replace text patterns.
5. Programming: Wildcards are used in various programming languages for pattern matching and string manipulation.
'''
def is_match(s, pattern):
    s_len = len(s)
    p_len = len(pattern)

    # Create a DP table to store results of subproblems
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    dp[0][0] = True  # Empty pattern matches empty string

    # Handle patterns with '*' at the beginning
    for j in range(1, p_len + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or s[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[s_len][p_len]
# Example usage:
if __name__ == "__main__":
    string = "adceb"
    pattern = "*a*b"
    match = is_match(string, pattern)
    print(f"Does the string '{string}' match the pattern '{pattern}'? {match}")

    string = input("Enter the string: ")
    pattern = input("Enter the pattern (with wildcards * and ?): ")
    match = is_match(string, pattern)
    print(f"Does the string '{string}' match the pattern '{pattern}'? {match}")

# The function uses dynamic programming to build a table that keeps track of matches between substrings of the input string and the pattern.
# Edge cases such as empty strings and patterns with only wildcards are handled appropriately.
string = input("Enter the string: ")
pattern = input("Enter the pattern (with wildcards * and ?): ")
def is_match(s, pattern):
    s_len = len(s)
    p_len = len(pattern)

    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    dp[0][0] = True

    for j in range(1, p_len + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or s[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[s_len][p_len]
match = is_match(string, pattern)
print(f"Does the string '{string}' match the pattern '{pattern}'? {match}")
