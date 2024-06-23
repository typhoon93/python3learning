"""
Merge Sort High Level Overview:
    The idea with Merge Sort is that it is very easy to combine 2 sorted lists and sort it after that.
    Steps:
    We break the list in half until we only have lists with 1 item in them.
        A list with 1 item is by definition sorted.
    Then we combine the 1 item lists into 2 item lists -> sorted.
    And then combine again, to get 4 item lists -> sorted...
    and so on.
    
Merge Function - A helper function, does a part of merge sort. Takes 2 sorted lists, and creates 1 sorted list. 
Merge Sort:
    1) Breaks list in half
    2) Base case: when len list is 1
    3) Uses merge() to put lists together

Merge sort space complexity: O (n), as it creates new lists
Merge sort Time complexity: 
    Breaking down the lists complexity: O (log n): 8 items in the list, breaking it down until we have 1 item lists takes 3 steps
    Merge time complexity O(n)
    Merge sort time complexity is: O(n log n)
    O(n log n) is the m ost efficient you can make a sorting algorhithm that will sort multiple types of data.
"""


def merge(lst1, lst2):  # my code
    new_list = []
    i = 0
    j = 0
    max_i = len(lst1)
    max_j = len(lst2)
    while i < max_i and j < max_j:
        if lst1[i] < lst2[j]:
            new_list.append(lst1[i])
            i += 1
            continue
        new_list.append(lst2[j])
        j += 1
    if i == max_i:
        new_list.extend(lst2[j:])
        return new_list
    new_list.extend(lst1[i:])
    return new_list


def merge_2(list1, list2):  # course code
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(lst):  # my code
    if len(lst) == 1:
        return lst
    mid = int(len(lst) / 2)
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])
    return merge(lst1, lst2)


def merge_sort_2(my_list):  # course code
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list) / 2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


# lst2 = [1, 1, 1, 1]
# lst1 = [2, 4, 6, 8]
# print(merge_2(lst1, lst2))

print(merge_sort_2([-1, 10, 2, 4, -10]))
