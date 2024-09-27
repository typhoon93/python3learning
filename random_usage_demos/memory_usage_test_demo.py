"""
Difference in memory usage for two methods of palindrome detection, for very long strings.

"""


# Using s == s[::-1] (O(n) space)
def is_palindrome_slice(s):
    return s == s[::-1]


# Using two-pointer technique (O(1) space)
def is_palindrome_pointers(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# Test string
s = "a" * 10 ** 7  # Very long string of 10 million 'a's

# Comparing space usage
import tracemalloc

# Test slicing method
tracemalloc.start()
is_palindrome_slice(s)
current, peak = tracemalloc.get_traced_memory()
print(f"Slicing method peak memory usage: {peak} KB = {peak / 10 ** 6} MB")
tracemalloc.stop()

# Test two-pointer method
tracemalloc.start()
is_palindrome_pointers(s)
current, peak = tracemalloc.get_traced_memory()
print(f"Two-pointer method peak memory usage: {peak} KB = {peak / 10 ** 6} MB")  # dividing here converts BYTEs to MB
tracemalloc.stop()

"""
tracemalloc monitors memory allocations made by Python code, specifically the memory allocated in the Python heap.
Tracemalloc only tracks memory allocations within the current Python process.
It does not monitor memory usage of other processes or the entire system.
"""
