import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:
    """
    The done argument is an instance of
    threading.Event, a simple object to synchronize threads
    The trick for text-mode animation: move the cursor back to the start of the line
with the carriage return ASCII control character ('\r').
    """
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):  # The Event.wait(timeout=None) method returns True when the event is set by
            # another thread; if the timeout elapses, it returns False. The .1s timeout sets the
            # “frame rate” of the animation to 10 FPS. If you want the spinner to go faster, use
            # a smaller timeout.
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def slow() -> int:
    """
    slow() will be called by the main thread. Imagine this is a slow API call over the
network. Calling sleep blocks the main thread, but the GIL is released so the
spinner thread can proceed.
    """
    time.sleep(3)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=("thinking!", done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set() # Set the Event flag to True; this will terminate the for loop inside the spin function.
    spinner.join() # wait until spinner thread finishes
    # When the main thread sets the done event, the spinner thread will eventually notice
    # and exit cleanly.
    return result

if __name__ == "__main__":
    result = supervisor()
    print(f'Answer: {result}')