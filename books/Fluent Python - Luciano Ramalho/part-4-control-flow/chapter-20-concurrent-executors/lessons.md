- Concurrency is essential for efficient network I/O: instead of idly waiting for remote machines, the application
  should do something else until a response comes back.
- The HTTPX library is inspired by the Pythonic requests package,
but is built on a more modern foundation. Crucially, HTTPX provides
synchronous and asynchronous APIs,
- The main features of the **concurrent.future**s package are the ThreadPoolExecutor
and ProcessPoolExecutor classes, which implement an API to submit callables for
execution in different threads or processes, respectively.
- The ThreadPoolExecutor constructor takes several arguments not shown, but the
first and most important one is max_workers, setting the maximum number of
worker threads to be executed. When max_workers is None (the default), ThreadPool
Executor decides its value using the following expression—since Python 3.8:
  - max_workers = min(32, os.cpu_count() + 4)
- Futures are core components of concurrent.futures and of asyncio, but as users of
these libraries we sometimes don’t see them
- Since Python 3.4, there are two classes named Future in the standard library: concur
rent.futures.Future and asyncio.Future. They serve the same purpose: an
**instance of either Future class represents a deferred computation that may or may
not have completed**
- This is somewhat similar to the Deferred class in Twisted, the
Future class in Tornado, and Promise in modern JavaScript.
- Futures **encapsulate** **pending** **operations** so that we can **put them in queues**, check
whether they are done, and retrieve results (or exceptions) when they become
available.
- An important thing to know about futures is that you and I should not create them:
they are meant to be instantiated exclusively by the concurrency framework, be it
concurrent.futures or asyncio
- In particular, concurrent.futures.Future instances are created only as
the result of submitting a callable for execution with a concurrent.futures.Execu
tor subclass. For example, the Executor.submit() method takes a callable, schedules
it to run, and returns a Future.
- Both types of Future have a .done() method that is nonblocking and returns a
Boolean that tells you whether the callable wrapped by that future has executed or
not.
- However, instead of repeatedly asking whether a future is done, client code usually
asks to be notified. That’s why both Future classes have an .add_done_call
back() method: you give it a callable, and the callable will be invoked with the future
as the single argument when the future is done.
- Be aware that the callback callable
will run in the same worker thread or process that ran the function wrapped in the
future.
- There is also a .result() method, which works the same in both classes when the
future is done: it returns the result of the callable, or re-raises whatever exception
might have been thrown when the callable was executed.

# Launching Processes with concurrent.futures
- The package enables parallel computation on multicore machines because it
supports distributing work among multiple Python processes using the ProcessPool
Executor class.
- Processes use more memory and take longer to start than threads, so the real value
of ProcessPoolExecutor is in CPU-intensive jobs.