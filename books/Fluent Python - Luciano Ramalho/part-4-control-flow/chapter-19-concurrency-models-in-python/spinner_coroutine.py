import asyncio

import itertools
import time


async def spin(msg: str, ) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1) # using await here
        except asyncio.CancelledError:  # asyncio.CancelledError is raised when the cancel method is called on the
            # Task controlling this coroutine. Time to exit the loop.
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def slow() -> int:
    """
    slow() will be called by the main thread. Imagine this is a slow API call over the
network. Calling sleep blocks the main thread, but the GIL is released so the
spinner thread can proceed.
    """
    # time.sleep(3) # if we use time.sleep here, the spinner doesn't work
    # Never use time.sleep(…) in asyncio coroutines unless you want
    # to pause your whole program. If a coroutine needs to spend some
    # time doing nothing, it should await asyncio.sleep(DELAY). This
    # yields control back to the asyncio event loop, which can drive
    # other pending coroutines.
    await asyncio.sleep(3)
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(
        spin('thinking'))  # asyncio.create_task schedules the eventual execution of spin, immediately
    # returning an instance of asyncio.Task.
    # Called from a coroutine to schedule another coroutine to execute eventually.
    # This call does not suspend the current coroutine. It returns a Task instance, an
    # object that wraps the coroutine object and provides methods to control and
    # query its state
    print(
        f'spinner object: {spinner}')  # <Task pending name='Task-2' coro=<spin() running at /path/to/spinner_async.py:11>>.
    result = await slow()  # The await keyword calls slow, blocking supervisor until slow returns.
    # Called from a coroutine to transfer control to the coroutine object returned by
    # coro(). This suspends the current coroutine until the body of coro returns. The
    # value of the await expression is whatever the body of coro returns.
    spinner.cancel()  # The Task.cancel method raises a CancelledError exception inside the spin coroutine
    return result


def main() -> None:  # only regular function, other are corotines (aysnc
    result = asyncio.run(supervisor())
    #     Called from a regular function to drive a coroutine object that usually is the entry
    # point for all the asynchronous code in the program, like the supervisor in this
    # example. This call blocks until the body of coro returns. The return value of the
    # run() call is whatever the body of coro returns.
    print(f"Answer: {result}")

if __name__ == "__main__":
    main()