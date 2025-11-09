# Write a Ptyhon funtion to generate Fibonacci series up to n terms.
'''
What is Fibonacci series?
The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones,
usually starting with 0 and 1. The series goes like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.

In Real Life:
1. Nature: The arrangement of leaves on a stem, the branching of trees, the arrangement of a pine cone, and the pattern of various fruits and vegetables often follow the Fibonacci sequence.
2. Computer Algorithms: Fibonacci numbers are used in algorithms such as Fibonacci search technique and in data structures like Fibonacci heaps.
3. Financial Markets: Some traders use Fibonacci retracement levels to predict potential support and resistance levels in financial markets.
4. Art and Architecture: The Fibonacci sequence is often associated with the golden ratio, which has been used in art and architecture to create aesthetically pleasing compositions.
{Golden Ratio=F(n+1)​/F(n), where F(n) is the nth Fibonacci number. As n approaches infinity, this ratio approaches approximately 1.6180339887...}
5. Music: Some musical compositions and rhythms are based on Fibonacci numbers.
'''
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
# Example usage:
if __name__ == "__main__":   
    terms = 10
    print(f"Fibonacci series up to {terms} terms: {fibonacci_series(terms)}")
    terms = int(input("Enter the number of terms for Fibonacci series: "))
    print(f"Fibonacci series up to {terms} terms: {fibonacci_series(terms)}")
# The function works by initializing the first two Fibonacci numbers (0 and 1) and iteratively calculating the next numbers in the series by summing the last two numbers.
# The generated numbers are stored in a list which is returned at the end.
