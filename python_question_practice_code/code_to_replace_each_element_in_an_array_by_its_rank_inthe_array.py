# Write a code to replace each element in an array by its rank in the array.
'''
What is Rank Replacement in an Array?
Rank replacement in an array involves replacing each element with its rank when the array is sorted. The rank of an element is determined by its position in the sorted version of the array, with the smallest element having a rank of 1, the second smallest a rank of 2, and so on.
In Real Life:
1. Data Normalization: Rank replacement can be used in data preprocessing to normalize data for statistical analysis or machine learning.
2. Competitive Ranking: In sports or competitive scenarios, rank replacement can help in determining the standings of participants based on their scores.
3. Grading Systems: Educational institutions can use rank replacement to assign grades based on students' performance relative to their peers.
4. Performance Evaluation: In corporate settings, rank replacement can be used to evaluate employee performance by ranking them based on key performance indicators.
5. Survey Analysis: In survey data analysis, rank replacement can help in understanding the relative importance of different factors based on respondents' ratings.
'''
def replace_with_ranks(arr):
    sorted_unique = sorted(set(arr))
    rank_dict = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
    ranked_array = [rank_dict[value] for value in arr]
    return ranked_array
# Example usage:
if __name__ == "__main__":
    sample_array = [40, 10, 20, 30]
    ranked_array = replace_with_ranks(sample_array)
    print("Original array:", sample_array)
    print("Ranked array:", ranked_array)

    user_input = input("Enter numbers separated by spaces: ")
    user_array = list(map(int, user_input.split()))
    ranked_user_array = replace_with_ranks(user_array)
    print("Ranked array:", ranked_user_array)
# The function works by first creating a sorted list of unique elements to determine their ranks, then mapping each original element to its corresponding rank.
user_input = input("Enter numbers separated by spaces: ")
user_array = list(map(int, user_input.split()))
sorted_unique = sorted(set(user_array))
rank_dict = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
ranked_array = [rank_dict[value] for value in user_array]
print("Ranked array:", ranked_array)
print("Ranked array:", ranked_array)
