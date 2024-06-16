"""
Bubble Sort: Big O: Worst case O(n**2), Best Case O(n) - This involves checking if we did any swaps at all, check my implementation
        1. We bubble up the largest item to the end, by comparing it each.
        2. We start back at beginning, but this time go to len(list) - 1, as the last one is sorted, and put the second largest item to the len-1 place.
        3. Repeat till done.


Selection Sort: Big O: Worst case O(n**2), Best Case O(n**2)
        1. With selection sort, we keep track of the indexes;
        2. Starting from item 1, we set it it's index to min_index.
        3. We loop through the whole list, switching min index depending on if the item we are at is SMALLER than the one we have the min index for.
        4. Once we check the whole list, we switch the 1st item with the one we have that is at min index.
        5. Then we do the same process again, but this time starting from item 2
        
Insertion Sort: Big O: Worst case O(n**2), Best Case O(n)
        1. We start from the 2nd item in the list, we compare it to the previous one. If it's smaller, we insert it before the one we compared it to.
        2. We continue comparing the same item until we:
            1. Hit an item that is bigger or equal to it. If that is the case we do nothing.
            2. We hit the first item in the list and our comapred item is smaller than it too - in that case we insert and stop, and then go to the next item. 
"""


def bubble_sort(unsorted_list: list):  # my solution
    """
    Sorts in place
    """
    list_length = len(unsorted_list)

    for i in range(
        1, list_length
    ):  # start from 1 to ensure we dont get list index out of range
        temp = None
        for j in range(list_length - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                temp = unsorted_list[j + 1]
                unsorted_list[j + 1] = unsorted_list[j]
                unsorted_list[j] = temp
        if (
            temp == None
        ):  # no swaps performed, list already sorted. ensure time complexity can be O(n) if list already sorted.
            print("List already sorted")
            return unsorted_list
        print(f"Loop {i}")
    return unsorted_list


def bubble_sort_2(my_list):  # course solution
    """
    Comment:
    A bit better than my solution as I do a bit more operations when starting the second loop, but the O does not change
    """
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


def selection_sort(my_list):  # my solitoin
    """
    sorts in place but also returns the list
    """
    list_len = len(my_list)
    for i in range(list_len):
        min_index = i
        for j in range(i + 1, list_len):
            if my_list[min_index] > my_list[j]:
                min_index = j
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp
    return my_list


def selection_sort_2(my_list):
    """
    A bit more refined than my code, doesn't run some lines unnecassarily, but func + big o is same it seems
    """
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


def insertion_sort(my_list: list):  # my code
    """
    Sorted in place.
    """
    list_len = len(my_list)
    for i in range(list_len - 1):
        for j in range(i + 1, 0, -1):
            if j == 0:
                break
            if my_list[j] >= my_list[j - 1]:
                break
            temp = my_list[j]
            my_list[j] = my_list[j - 1]
            my_list[j - 1] = temp
    return my_list


def insertion_sort_2(my_list: list):  # course code
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(bubble_sort([1, 2, 3]))
print(bubble_sort([1, 10, 12, 1, 0, -1, 5]))
print(bubble_sort_2([1, 10, 12, 1, 0, -1, 5]))
print(selection_sort([1, 10, 12, 1, 0, -1, 5]))
print(selection_sort_2([1, 10, 12, 1, 0, -1, 5]))
print(insertion_sort([1, 10, 12, 1, 0, -1, 5]))
print(insertion_sort_2([1, 10, 12, 1, 0, -1, 5]))
