# Write a code in Python thus Hoes is a Merge Sort algorithm implemented.?
'''
What is Merge Sort?
Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts each half, and then merges the sorted halves back together. It is known for its efficiency and stability.
In Real Life:
1. Large Data Sorting: Merge Sort is often used in external sorting algorithms for large datasets that do not fit into memory, as it can efficiently handle large amounts of data.  
2. Stable Sorting: Merge Sort maintains the relative order of equal elements, making it suitable for scenarios where stability is required, such as sorting records in a database.
3. Parallel Processing: Merge Sort can be easily parallelized, allowing for faster sorting on multi-core processors.
4. Linked Lists: Merge Sort is particularly effective for sorting linked lists, as it does not require random access to elements.
5. Functional Programming: Merge Sort is commonly used in functional programming languages due to its recursive nature and immutability.
'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]        # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)        # Sorting the first half
        merge_sort(R)        # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
# Example usage:
if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(sample_array)
    print("Sorted array is:", sorted_array)

    user_input = input("Enter numbers separated by spaces to sort: ")
    user_array = list(map(int, user_input.split()))
    sorted_user_array = merge_sort(user_array)
    print("Sorted array is:", sorted_user_array)
# The function works by recursively dividing the array into halves until single-element arrays are reached, then merging those arrays back together in sorted order.
# Edge cases such as empty arrays and arrays with one element are handled naturally by the algorithm.
user_input = input("Enter numbers separated by spaces to sort: ")
user_array = list(map(int, user_input.split()))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
sorted_user_array = merge_sort(user_array)
print("Sorted array is:", sorted_user_array)

