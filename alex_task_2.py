"""
#(Task 2) Check if a string is a palindrome?

Add constraints for performance, like handling very long strings with early exit conditions using slicing and two-pointer techniques in O(n) time complexity.
"""

"""
Answer:
I have created two functions, since we do not have specific details on the input data.
    - is_palindrome_1 presumes that we will get strings with only alphanumeric values, e.g. s = "aba", s = "abc"
    - is_palindrome_2 takes into account that we may have alphanumeric values, aka - these are more traditional sentences
Both functions were written by me.
Inside both functions, after the code I have also added some comments / thoughts.
1. On a potential list slicing solution
2. A slightly optimized version that I have discovered after speaking with ChatGPT. 
Other:
 - I have done a similar task but for linked lists here: data-structures-and-algorithms/03-Linked Lists/Problems/easy-palindrome-linked-list.py
 - I have created a comparison on MEMORY used with slicing vs pointer method, to show the impact for a very big string: random_usage_demos/memory_usage_test_demo.py

"""

def is_palindrome_1(s):
    """
    This presumes that we will not have non-alphanumeric (spaces, commas etc) data in the input string.
    My original solution:
    Space Complexity = O(1)
    Time Complexity = O(n)
    Two pointer technique
    """
    i = 0
    j = len(s) - 1
    mid = j // 2
    while i <= mid and j >= mid:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True
    # a list slicing solution would be, but this would increase Space Complexity to O(n):
    # return s == s[::-1]
    # a slightly better gpt solution is this, avoiding unnecessary calculations
    # i = 0
    # j = len(s) - 1
    # while i < j:
    #     if s[i] != s[j]:
    #         return False
    #     i += 1
    #     j -= 1
    # return True


def is_palindrome_2(s):
    """
    If it is a regular sentence, that may have have spaces, and other non alphanumeric chars
    My original solution:
    Space Complexity = O(1)
    Time Complexity = O(n)
    Two pointer technique
    """
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i].isalnum() and s[j].isalnum():
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        else:
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1
    return True

    ## comments above is my original solution.
    ## a slicing technique cannot be used here directly;
    ## we would need to sanitize the string, skipping not alpha numeric chars, and save it to a list -> then use the slicing.
    ## a slightly better code from gpt:
    #  i = 0
    # j = len(s) - 1
    # while i <= j:
    #     while i < j and not s[i].isalnum():
    #         i += 1
    #     while i < j and not s[j].isalnum():
    #         j -= 1
    #     if s[i].lower() != s[j].lower():
    #         return False
    #     i += 1
    #     j -= 1
    # return True

if __name__ == "__main__":

    s = "aba"
    print(f"Simple case, string is: '{s}'")
    expected = True
    res = is_palindrome_1(s)
    print(res)
    print(f"{expected=}")


    s = "A man, a plan, a canal: Panama"
    print(f"More complex case, string is: '{s}'")
    expected = True
    res = is_palindrome_2(s)
    print(res)
    print(f"{expected=}")
