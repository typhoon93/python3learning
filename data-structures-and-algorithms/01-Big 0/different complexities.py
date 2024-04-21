"""
a code that is of complexity O(n)
"""
def print_items(n):
    for i in range(n):
        print(i)
        
# print_items(10)



"""
a code that is of complexity O(2n), still noted 0(n)
"""
def print_items_2(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
        
# print_items_2(10)


"""
Big O with different inputs, you might assume that the complexity is 
O(2n) as with the prev example, but in this case the big O is:
O(a) + O(b) = O(a + b), it cannot be simplified further since the inputs are different.
"""
def print_items_diff_inputs(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
        
# print_items_diff_inputs(10, 20)




"""
a code that is of complexity O(n^2), a for loop inside a for loop
"""
def print_items_3(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
        
# print_items_3(10)




"""
a code that is of complexity O(n^3), a for loop inside a for loop, inside a for loop, we still denote it 0(n^2)
"""
def print_items_4(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
        
# print_items_4(10)




"""
a code that is of complexity O(n^2 + n), a for loop inside a for loop + another separate for loop;
the second n becomes insignificant at some point, so we drop it and just denote O(n^2)
"""
def print_items_5(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
            print(k)
         
print_items_5(10)


"""
A code that is of complexity O(1) -> only one operation.
if return n+n+n, even though we have 2 operations (+), we still call it O(1)
O(1) is constant time.
"""
def add_items(n):
    return n+n 

