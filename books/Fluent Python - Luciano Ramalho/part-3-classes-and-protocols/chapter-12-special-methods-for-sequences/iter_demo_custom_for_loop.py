def manual_for_loop(iterable, operation):
    """
    Manually iterates over any iterable object and applies an operation to each item.

    :param iterable: Any iterable object.
    :param operation: A function that takes one argument and performs an operation on it.
    """
    # Creating an iterator from the iterable
    it = iter(iterable)

    # Manually iterating using a while loop
    while True:
        try:
            # Get the next item
            current_item = next(it)
            # Apply the operation function to the current item
            operation(current_item)
        except StopIteration:
            # If no more items, exit the loop
            break

# Example usage
if __name__ == "__main__":
    # Define a simple operation to print items
    def print_item(item):
        print(item)

    # Example list to iterate over
    my_list = [1, 2, 3, 4]

    # Call the manual_for_loop function with the list and the print_item operation
    manual_for_loop(my_list, print_item)