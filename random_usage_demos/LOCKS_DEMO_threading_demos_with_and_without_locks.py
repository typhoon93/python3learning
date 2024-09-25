import threading
import time

"""

Thread safety is a concept applicable in environments where multiple threads operate concurrently. If a data structure is thread-safe, you can read from, write to, and modify it from multiple threads without causing interference among those threads, and without corrupting the data structure.

For lists, sets, and dictionaries, Python provides some mechanisms to make operations thread-safe: Locks: You can use locks from the threading module to ensure that only one thread can access a part of code at a time.

Queue module: This provides the queue.Queue, queue.LifoQueue, and queue.PriorityQueue, which are thread-safe implementations for FIFO, LIFO (stack-like behavior), and priority queues respectively.

Scenario: Popping Two Items Simultaneously
If two threads attempt to pop items from the queue at the same time, here’s what happens:

Lock Acquisition: The first thread that reaches the get() method acquires the lock.
Item Removal: This thread removes an item from the queue.
Lock Release: After the item is removed, the thread releases the lock.
Next Thread: The second thread, which has been waiting for the lock to become available, now acquires the lock, and can then safely remove the next item from the queue.


Implementing a locking mechanism in a Python list can be useful when your application evolves to involve multiple threads. Even though a typical Python process starts as a single thread, you might opt to use multiple threads to handle tasks simultaneously, such as in a GUI application, network server, or when performing parallel data processing.


Implementing Locking in a List

To implement a locking mechanism for a list in Python, you can use the Lock object from the threading module. Here’s a simple example of how you can use a lock to synchronize access to a list:

####
import threading

# Create a global lock
lock = threading.Lock()

# Shared resource
my_list = []

# Function to add elements to the list
def add_to_list(item):
    with lock:  # This block is now thread-safe
        my_list.append(item)
        print(f"Added {item}")

# Function to remove elements from the list
def remove_from_list():
    with lock:  # This block is also thread-safe
        if my_list:
            item = my_list.pop(0)
            print(f"Removed {item}")
        else:
            print("List is empty")

# Creating threads
thread1 = threading.Thread(target=add_to_list, args=(1,))
thread2 = threading.Thread(target=add_to_list, args=(2,))
thread3 = threading.Thread(target=remove_from_list)

# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Joining threads to wait for them to finish
thread1.join()
thread2.join()
thread3.join()

# Final state of the list
print(my_list)

####

In this example, the with lock: block ensures that only one thread can execute the block at any given time. This prevents issues like data corruption or race conditions, where two threads might try to modify the list simultaneously.

Relevance of Threading in Python
Python processes start as single-threaded, but you can create multiple threads explicitly using the threading module. This is useful in several scenarios:

I/O-Bound Applications: In applications where the program spends significant time waiting for I/O operations (like network communication or disk reads/writes), threading can help by allowing one thread to run while another is waiting on I/O.
User Interfaces: In GUI applications, threading is used to keep the user interface responsive while performing background tasks.
Concurrency in Server Applications: Web servers and network servers often use threading to handle multiple connections simultaneously, allowing each connection to be handled in a separate thread.
Considerations with Python’s GIL
One important aspect to keep in mind is Python's Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time in the CPython interpreter. This means that CPU-bound multithreaded Python programs might not see a performance benefit from threading due to the GIL. However, for I/O-bound tasks, threading can significantly improve performance by overlapping I/O and computation.

By implementing a locking mechanism, as shown above, you can safely manipulate shared resources across multiple threads in Python. This approach ensures that your multi-threaded application behaves predictably and maintains data integrity.

"""


def run_threading_without_locks():
    """Demonstrates threading issues without using locks."""
    # Local variables for this function
    shared_list = []
    counter = [0]

    def list_append(item):
        """Appends an item to the local list."""
        shared_list.append(item)
        print(f"Appended {item} to list")

    def increment_counter():
        """Increments a local counter without locking."""
        local_copy = counter[0]
        local_copy += 1
        time.sleep(0.1)  # Delay to enhance the chance of a race condition
        counter[0] = local_copy

    # Create threads for list appending
    list_threads = [threading.Thread(target=list_append, args=(i,)) for i in range(5)]
    for thread in list_threads:
        thread.start()
    for thread in list_threads:
        thread.join()

    print(f"Final list content: {shared_list}")

    # Create threads for counter incrementing
    counter_threads = [threading.Thread(target=increment_counter) for _ in range(100)]
    for thread in counter_threads:
        thread.start()
    for thread in counter_threads:
        thread.join()

    print(f"Counter should be 100, actual value is {counter[0]}")


def run_threading_with_locks():
    """Demonstrates threading issues resolved by using locks."""
    # Local variables for this function
    shared_list = []
    counter = [0]
    lock = threading.Lock()

    def list_append_with_lock(item):
        """Appends an item to the local list using a lock."""
        with lock:
            shared_list.append(item)
            print(f"Appended {item} to list with lock")

    def increment_counter_with_lock():
        """Increments a local counter using a lock."""
        with lock:
            local_copy = counter[0]
            local_copy += 1
            counter[0] = local_copy

    # Create threads for list appending with locks
    list_threads = [threading.Thread(target=list_append_with_lock, args=(i,)) for i in range(5)]
    for thread in list_threads:
        thread.start()
    for thread in list_threads:
        thread.join()

    print(f"Final list content with lock: {shared_list}")

    # Create threads for counter incrementing with locks
    counter_threads = [threading.Thread(target=increment_counter_with_lock) for _ in range(100)]
    for thread in counter_threads:
        thread.start()
    for thread in counter_threads:
        thread.join()

    print(f"Counter should be 100, actual value with lock is {counter[0]}")


def simple_locks_example():
    # Initialize a shared list and a lock
    shared_list = []
    list_lock = threading.Lock()

    def add_item_to_list(item):
        """Function to add an item to the list with locking."""
        with list_lock:  # Acquire the lock before modifying the list
            shared_list.append(item)
            print(f"Added {item} to the list")

    def remove_item_from_list():
        """Function to safely remove the first item from the list with locking."""
        with list_lock:  # Acquire the lock before modifying the list
            if shared_list:
                item = shared_list.pop(0)
                print(f"Removed {item} from the list")
            else:
                print("List is empty, nothing to remove")

    # Creating threads for adding and removing items
    thread1 = threading.Thread(target=add_item_to_list, args=("apple",))
    thread2 = threading.Thread(target=add_item_to_list, args=("banana",))
    thread3 = threading.Thread(target=remove_item_from_list)
    thread4 = threading.Thread(target=remove_item_from_list)

    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    # Check the final content of the list
    print(f"Final list content: {shared_list}")


simple_locks_example()
run_threading_without_locks()
run_threading_with_locks()
