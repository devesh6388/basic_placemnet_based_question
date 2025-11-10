# Write a code for Bubble Sort algorithm in Python.

'''
What is Bubble Sort?
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the
list is repeated until the list is sorted.
In Real Life:
1. Educational Purposes: Bubble Sort is often used in educational settings to teach the concepts of sorting algorithms due to its simplicity.
2. Small Data Sets: For very small data sets, Bubble Sort can be efficient enough and easy to implement.
3. Nearly Sorted Data: Bubble Sort can perform well on nearly sorted data, as it can quickly identify that the list is already sorted.
4. Visual Demonstrations: Bubble Sort is frequently used in visualizations to demonstrate sorting algorithms because of its straightforward approach.
5. Simple Implementations: In scenarios where simplicity is prioritized over efficiency, Bubble Sort can be a suitable choice.
'''
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Example usage:
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(sample_array)
    print("Sorted array is:", sorted_array)

    user_input = input("Enter numbers separated by spaces to sort: ")
    user_array = list(map(int, user_input.split()))
    sorted_user_array = bubble_sort(user_array)
    print("Sorted array is:", sorted_user_array)
# The function works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order.
# Edge cases such as empty arrays and arrays with one element are handled naturally by the algorithm.
user_input = input("Enter numbers separated by spaces to sort: ")
user_array = list(map(int, user_input.split()))
n = len(user_array)
for i in range(n):
    for j in range(0, n-i-1):
        if user_array[j] > user_array[j+1]:
            user_array[j], user_array[j+1] = user_array[j+1], user_array[j]
print("Sorted array is:", user_array)

