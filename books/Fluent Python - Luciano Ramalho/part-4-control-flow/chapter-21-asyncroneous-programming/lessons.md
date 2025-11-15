- Generator-based coroutine - A generator function decorated with @types.coroutine—introduced in Python 3.5. That
  decorator makes the generator compatible with the new await keyword.

## Asynchronous generator

A generator function defined with async def and using yield in its body. It returns an asynchronous generator object
that provides __anext__, a coroutine method to retrieve the next item.

### New Concept: Awaitable

The for keyword works with iterables. The await keyword works with awaitables.

If you don’t expect to cancel the task or wait for it, there is no need to keep the Task object returned from
create_task. Creating the task is enough to schedule the coroutine to run.

## Semaphore vs lock
- A semaphore is a synchronization primitive, more flexible than a lock. A semaphore
can be held by multiple coroutines, with a configurable maximum number. This
makes it ideal to throttle the number of active concurrent coroutines. “Python’s Semaphores”
on page 791 has more information.
- Main Differences
### Capacity
Lock: capacity is 1 (only one holder).
Semaphore: capacity is N (configurable, e.g. 3, 10, etc.).
### Typical Use Case
Lock: protect one critical section or piece of shared data.
Semaphore: limit concurrency level for a resource pool.
### Semantics
Lock is conceptually simpler: lock/unlock a resource.
Semaphore is about counting access slots.
### APIs (threading)
Both have acquire() and release(), and both work with with:
    with lock:
        # critical section
    with sem:
        # up to N threads can be in here


### Asyncaio semaphor
An asyncio.Semaphore has an internal counter that is decremented whenever we
await on the .acquire() coroutine method, and incremented when we call
the .release() method—which is not a coroutine because it never blocks. The initial
value of the counter is set when the Semaphore is instantiated:
semaphore = asyncio.Semaphore(concur_req)

Instead of using those methods directly, it’s safer to use the semaphore as an asynchronous
context manager, as I did in Example 21-6, function download_one:
async with semaphore:
image = await get_flag(client, base_url, cc)
The Semaphore.__aenter__ coroutine method awaits for .acquire(), and its
__aexit__ coroutine method calls .release().

### Delagating tasks to executors
In Python, if you’re not careful, file I/O can seriously degrade the performance
of asynchronous applications, because reading and writing to storage in the
main thread blocks the event loop.

- to be able to run awaitables in python, start it with this command: `python -m asyncio`