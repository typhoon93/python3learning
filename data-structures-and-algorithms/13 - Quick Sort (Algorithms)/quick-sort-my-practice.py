"""
# Quick Sort:
We start with a pivot point, the first item;
    - we compare it to each number after the pivot:
        - see if it's greater than or less than the pivot
            -if greater we do not do anything.
            -if less than pivot, we swap it with the first item that was greater than the pivot.
            -> continue doing that, swapping less items with the leftmost greater than item until we are done with the list.
            -> we swap the pivot with the last of the greater than items.
    -> pivot is now sorted, everything less than the pivot is on the left, everything more than the 4 is on the right
    -> we do the quick sort again on the lists on the right and left of pivot
    
## Pivot function (helper):
    - pick pivot - item 1
    - all items on greater than on the one side, all items that are less than on the other side.
    - we swap the last less than item with the pivot
    - pivot returns the list, and also the new index of the pivot
    
## Complexity:
    Pivot - O(n)
    Quick sort recursive part - O(log n)
    Whole quick sort (best and average case): O(n log n)
    Worst case: O (n*2), this happens when we have already sorted data, 
        in that case best use something like INSERTION sort, that is best for already sorted data.
"""


def pivot(lst):  # my code
    pivot_index = 0
    swap_index = 0
    for i in range(1, len(lst)):
        if lst[pivot_index] > lst[i]:
            swap_index += 1
            temp = lst[swap_index]
            lst[swap_index] = lst[i]
            lst[i] = temp

    temp = lst[swap_index]
    lst[swap_index] = lst[pivot_index]
    lst[pivot_index] = temp

    return swap_index, lst


def swap(my_list, index1, index2):  # course code
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):  # course code

    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):  # course code
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


my_list = [4, 6, 1, 7, 3, 2, 5]

quick_sort(my_list)
print(my_list)
# swap_index = pivot(my_list, 0, 6)
# swap_index_left = pivot(my_list, 0, swap_index)
# swap_index_left_left = pivot(my_list, 0, swap_index_left)
# swap_index_left_right = pivot(my_list, swap_index_left + 1, 6)

# swap_index_right = pivot(my_list, swap_index + 1, 6)
# print(swap_index)
# print(swap_index_left_left)
# print(swap_index_left_right)

# print(my_list)
