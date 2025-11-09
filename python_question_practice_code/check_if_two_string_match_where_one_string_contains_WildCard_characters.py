# Write a Python Function to check if two strings match where one string contains WildCard characters.
'''
What is WildCard Matching?
WildCard matching is a technique used to compare two strings where one string may contain special characters known as wildcards. The most common wildcards are:
1. '?' - Matches any single character.
2. '*' - Matches any sequence of characters (including the empty sequence).
In Real Life:
1. File Searching: Wildcards are commonly used in file systems to search for files with specific patterns (e.g., *.txt to find all text files).
2. Database Queries: SQL uses wildcards in queries to filter results based on patterns (e.g., LIKE 'A%' to find names starting with 'A').
3. Command Line Interfaces: Many command line tools use wildcards to specify groups of files or directories.
4. Text Processing: Wildcards are used in text editors and programming languages for pattern matching and string manipulation.
5. Network Security: Wildcards are used in firewall rules and access control lists to define patterns for allowed or blocked traffic.
'''
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[m][n]
# Example usage:
if __name__ == "__main__":
    string = "adceb"
    pattern = "*a*b"
    if is_match(string, pattern):
        print(f'The string "{string}" matches the pattern "{pattern}".')
    else:
        print(f'The string "{string}" does not match the pattern "{pattern}".')
    
    string = input("Enter the string: ")
    pattern = input("Enter the pattern (with wildcards ? and *): ")
    if is_match(string, pattern):
        print(f'The string "{string}" matches the pattern "{pattern}".')
    else:
        print(f'The string "{string}" does not match the pattern "{pattern}".')

        
# The function works by using dynamic programming to build a 2D table that keeps track of matches between substrings of the input string and the pattern.
# It initializes the table based on the presence of '*' in the pattern and iteratively fills it based on character matches and wildcard rules.
# Edge cases such as empty strings and patterns consisting solely of '*' are handled in the initialization step.
s = input("Enter the string: ")
p = input("Enter the pattern (with wildcards ? and *): ")
m, n = len(s), len(p)
dp = [[False] * (n + 1) for _ in range(m + 1)]
dp[0][0] = True
for j in range(1, n + 1):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 1]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if p[j - 1] == s[i - 1] or p[j - 1] == '?':
            dp[i][j] = dp[i - 1][j - 1]
        elif p[j - 1] == '*':
            dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
if dp[m][n]:
    print(f'The string "{s}" matches the pattern "{p}".')
else:
    print(f'The string "{s}" does not match the pattern "{p}".')

