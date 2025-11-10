# Write a code for heap sort algorithm in Python.
'''
What is Heap Sort?
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements. It works by first building a max heap from the input data, and then repeatedly extracting the maximum element from the heap and rebuilding the heap until all elements are sorted.
In Real Life:
1. Priority Queues: Heap Sort is often used in implementing priority queues, where elements with higher priority are served before those with lower priority.
2. Efficient Sorting: Heap Sort is useful for sorting large datasets due to its O(n log n) time complexity, making it efficient for various applications.
3. Memory Management: Heap Sort is an in-place sorting algorithm, which means it requires only a constant amount of additional memory, making it suitable for memory-constrained environments.
4. Real-Time Systems: Heap Sort can be used in real-time systems where predictable performance is crucial, as it has a guaranteed time complexity.
5. Graph Algorithms: Heap Sort is utilized in graph algorithms like Dijkstra's and Prim's algorithms for efficiently managing and sorting vertices based on their weights or distances.
'''
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2    # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr
# Example usage:
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6, 7]
    sorted_array = heap_sort(sample_array)
    print("Sorted array is:", sorted_array)

    user_input = input("Enter numbers separated by spaces to sort: ")
    user_array = list(map(int, user_input.split()))
    sorted_user_array = heap_sort(user_array)
    print("Sorted array is:", sorted_user_array)
# The function works by first building a max heap from the input array and then repeatedly extracting the maximum element and rebuilding the heap until the array is sorted.
# Edge cases such as empty arrays and arrays with one element are handled naturally by the algorithm.
user_input = input("Enter numbers separated by spaces to sort: ")
user_array = list(map(int, user_input.split()))
n = len(user_array)
for i in range(n // 2 - 1, -1, -1):
    heapify(user_array, n, i)
for i in range(n-1, 0, -1):
    user_array[i], user_array[0] = user_array[0], user_array[i]
    heapify(user_array, i, 0)   
print("Sorted array is:", user_array)
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
