- Concurrency is about dealing with lots of things at once. 
- Parallelism is about doing lots of things at once.
- Concurrency provides a way to structure a solution to solve a problem that may (but
not necessarily) be parallelizable.
- All parallel systems are
concurrent, but not all concurrent systems are parallel.
- In the early 2000s we used
single-core machines that handled 100 processes concurrently on GNU Linux.
- A modern laptop with 4 CPU cores is routinely running more than 200 processes at any
given time under normal, casual use.
- Python’s core packages for concurrent programming: 
  - threading (threads)
  - multi processing (processes)
  - asyncio (native coroutines)
- YouTube, DropBox, Instagram, Reddit, and others were able to achieve web scale when they started, using Python as their primary
language—despite persistent claims that “Python doesn’t scale.”
- Often you want to amortize
the startup cost by making each thread or process into a “worker” that enters a
loop and stands by for inputs to work on.
- the usual answers involve messages and queues.
- Python coroutines and threads are not suitable for CPU-intensive tasks, as
we’ll see.
- Concurrency - The ability to handle multiple pending tasks, making progress one at a time or in
parallel (if possible) so that each of them eventually succeeds or fails. A singlecore
CPU is capable of concurrency if it runs an OS scheduler that interleaves the
execution of the pending tasks. Also known as multitasking
- Parallelism - The ability to execute multiple computations at the same time. This requires a
multicore CPU, multiple CPUs, a GPU, or multiple computers in a cluster.
- Execution unit - General term for objects that execute code concurrently, each with independent
state and call stack. Python natively supports three kinds of execution units: processes,
threads, and coroutines.
- Process
An instance of a computer program while it is running, using memory and a slice
of the CPU time. Modern desktop operating systems routinely manage hundreds
of processes concurrently, with each process isolated in its own private memory
space. Processes communicate via pipes, sockets, or memory mapped files—all of
which can only carry raw bytes. Python objects must be serialized (converted)
into raw bytes to pass from one process to another. This is costly, and not all
Python objects are serializable. A process can spawn subprocesses, each called a
child process. These are also isolated from each other and from the parent. Processes
allow preemptive multitasking: the OS scheduler preempts—i.e., suspends
—each running process periodically to allow other processes to run. This means
that a frozen process can’t freeze the whole system—in theory.
- Thread
An execution unit within a single process. When a process starts, it uses a single
thread: the main thread. A process can create more threads to operate concurrently
by calling operating system APIs. Threads within a process share the same
memory space, which holds live Python objects. This allows easy data sharing
between threads, but can also lead to corrupted data when more than one thread
updates the same object concurrently. Like processes, threads also enable preemptive
multitasking under the supervision of the OS scheduler. A thread consumes
less resources than a process doing the same job.
- Coroutine
A function that can suspend itself and resume later. In Python, classic coroutines
are built from generator functions, and native coroutines are defined with async
def. “Classic Coroutines” on page 641 introduced the concept, and Chapter 21
covers the use of native coroutines. Python coroutines usually run within a single
thread under the supervision of an event loop, also in the same thread. Asynchronous
programming frameworks such as asyncio, Curio, or Trio provide an event
loop and supporting libraries for nonblocking, coroutine-based I/O. Coroutines
support cooperative multitasking: each coroutine must explicitly cede control
with the yield or await keyword, so that another may proceed concurrently (but
not in parallel). This means that any blocking code in a coroutine blocks the execution
of the event loop and all other coroutines—in contrast with the preemptive
multitasking supported by processes and threads. On the other hand, each
coroutine consumes less resources than a thread or process doing the same job.
- Queue
A data structure that lets us put and get items, usually in FIFO order: first in, first
out. Queues allow separate execution units to exchange application data and control
messages, such as error codes and signals to terminate. The implementation
of a queue varies according to the underlying concurrency model: the queue package in Python’s standard library provides queue classes to support threads,
while the multiprocessing and asyncio packages implement their own queue
classes. The queue and asyncio packages also include queues that are not FIFO:
LifoQueue and PriorityQueue.
- Lock
An object that execution units can use to synchronize their actions and avoid
corrupting data. While updating a shared data structure, the running code
should hold an associated lock. This signals other parts of the program to wait
until the lock is released before accessing the same data structure. The simplest
type of lock is also known as a mutex (for mutual exclusion). The implementation
of a lock depends on the underlying concurrency model.
- Contention
Dispute over a limited asset. Resource contention happens when multiple execution
units try to access a shared resource—such as a lock or storage. There’s also
CPU contention, when compute-intensive processes or threads must wait for the
OS scheduler to give them a share of the CPU time.
- Access to object reference counts and other internal interpreter state is controlled
by a lock, the Global Interpreter Lock (GIL). Only one Python thread can
hold the GIL at any time. This means that only one thread can execute Python
code at any time, regardless of the number of CPU cores.
- To prevent a Python thread from holding the GIL indefinitely, Python’s bytecode
interpreter pauses the current Python thread every 5ms by default,4 releasing the
GIL. The thread can then try to reacquire the GIL, but if there are other threads
waiting for it, the OS scheduler may pick one of them to proceed.
- When we write Python code, we have no control over the GIL. But a built-in
function or an extension written in C—or any language that interfaces at the
Python/C API level—can release the GIL while running time-consuming tasks
- Every Python standard library function that makes a syscall5 releases the GIL.
This includes all functions that perform disk I/O, network I/O, and
time.sleep(). Many CPU-intensive functions in the NumPy/SciPy libraries, as
well as the compressing/decompressing functions from the zlib and bz2 modules,
also release the GIL.
- The effect of the GIL on network programming with Python threads is relatively
small, because the I/O functions release the GIL, and reading or writing to the
network always implies high latency—compared to reading and writing to memory.
Consequently, each individual thread spends a lot of time waiting anyway,
so their execution can be interleaved without major impact on the overall
throughput. That’s why David Beazley says: “Python threads are great at doing
nothing.”
- Contention over the GIL slows down compute-intensive Python threads.
Sequential, single-threaded code is simpler and faster for such tasks.
- To run CPU-intensive Python code on multiple cores, you must use multiple
Python processes
- A syscall is a call from user code to a function of the operating system kernel. I/O, timers, and locks are some
of the kernel services available through syscalls.
- This section did not mention coroutines, because by default they
share the same Python thread among themselves and with the
supervising event loop provided by an asynchronous framework,
therefore the GIL does not affect them. It is possible to use multiple
threads in an asynchronous program, but the best practice is that
one thread runs the event loop and all coroutines, while additional
threads carry out specific tasks.
- Thread
  - By design, there is no API for terminating a thread in Python. You must send it
  a message to shut down.
  The threading.Event class is Python’s simplest signalling mechanism to coordinate
  threads. An Event instance has an internal boolean flag that starts as False. Calling
  Event.set() sets the flag to True. While the flag is false, if a thread calls
  Event.wait(), it is blocked until another thread calls Event.set(), at which time
  Event.wait() returns True. If a timeout in seconds is given to Event.wait(s), this
  call returns False when the timeout elapses, or returns True as soon as Event.set()
  is called by another thread
- Process
  - When you create a **multiprocessing.Process** instance,
  a whole new Python interpreter is started as a child process in the background. Since
  each Python process has its own GIL, this allows your program to use all available CPU cores.
  - The spinner object is displayed as <Process name='Process-1' parent=14868
initial>, where 14868 is the process ID of the Python instance running
spinner_proc.py.
  - The basic API of threading and multiprocessing are similar, but their implementation
is very different, and multiprocessing has a much larger API to handle the
added complexity of multiprocess programming.
  - For example, one challenge when
converting from threads to processes is how to communicate between processes that
are isolated by the operating system and can’t share Python objects. This means that
objects crossing process boundaries have to be serialized and deserialized, which creates
overhead.
  - In Example spinner_process.py, the only data that crosses the process boundary is the
Event state, which is implemented with a low-level OS semaphore in the C code
underlying the multiprocessing module.
  - Since Python 3.8, there’s a multiprocessing.shared_memory package
in the standard library, but it does not support instances of
user-defined classes.
  - Besides raw bytes, the package allows processes
to share a ShareableList, a mutable sequence type that can
hold a fixed number of items of types int, float, bool, and None,
as well as str and bytes up to 10 MB per item. See the ShareableL
ist documentation for more.
  - The semaphore is a fundamental building block that can be used to implement other synchronization mechanisms.
Python provides different semaphore classes for use with threads, processes, and coroutines.
    - A semaphore is a synchronization primitive used to control access to a shared resource in concurrent programming. It helps manage how many threads, processes, or coroutines can access a particular resource at the same time, preventing race conditions and ensuring safe execution.
    - A semaphore maintains a counter. This counter represents the number of "permits" available. Threads or processes can:

      - Acquire a permit (decrease the counter).

      - Release a permit (increase the counter).
    - If the counter is zero when a thread tries to acquire, it will block until a permit is released by another thread.
    - A **semaphore** is a way for one process or thread to "signal" another.
      - Before computers, a semaphore referred to a visual signaling device—think of:
        - From Greek:  "sēma" (σῆμα) = sign; "phoros" (φορός) = bearing or carrying
          - Railroad signals with moving arms
          - Maritime signal flags
          - Semaphore towers in the 18th–19th centuries, which used pivoting arms to send messages over long distances visually
          - You can think of a traffic LIGHT as a semaphore. Traffic semaphore, another name for automotive traffic lights based on their early resemblance to railway semaphores. Turning semaphore or trafficators, retractable arms to indicate turns on automobiles from the 1920s to 1950s.
      - A semaphore is a way for one process or thread to "signal" another.
        - Instead of using visible arms or flags, it's a numeric counter and blocking mechanism.
        - It tells other threads: "You may (or may not) proceed."
      - In Bulgarian language, "семафор" most commonly refers to a traffic light

- Coroutines
  - It is the job of OS schedulers to allocate CPU time to drive threads and processes. In
contrast, coroutines are driven by an application-level event loop that manages a
queue of pending coroutines, drives them one by one, monitors events triggered by
I/O operations initiated by coroutines, and passes control back to the corresponding
coroutine when each event happens.
  - The event loop and the library coroutines and
the user coroutines all execute in a single thread. Therefore, any time spent in a
coroutine slows down the event loop—and all other coroutines
  - Remember: invoking a coroutine as coro() immediately returns a
coroutine object, but does not run the body of the coro function.
Driving the body of coroutines is the job of the event loop.
  - Never use time.sleep(…) in asyncio coroutines unless you want
to pause your whole program. If a coroutine needs to spend some
time doing nothing, it should await asyncio.sleep(DELAY). This
yields control back to the asyncio event loop, which can drive
other pending coroutines.
  - Greenlet and gevent
    - The package
supports cooperative multitasking through lightweight coroutines—named greenlets
—that don’t require any special syntax such as yield or await, therefore are easier to
integrate into existing, sequential codebases.
    - The gevent networking library monkey patches Python’s standard socket module
making it nonblocking by replacing some of its code with greenlets.
    - Numerous open source projects use gevent, including the widely deployed Gunicorn—
- if you’ve done any nontrivial
programming with threads, you know how challenging it is to reason about the program
because the scheduler can interrupt a thread at any time. You must remember
to hold locks to protect the critical sections of your program, to avoid getting interrupted
in the middle of a multistep operation—which could leave data in an invalid
state.
- With coroutines, your code is protected against interruption by default. You must
explicitly await to let the rest of the program run.
- Instead of holding locks to synchronize
the operations of multiple threads, coroutines are “synchronized” by definition:
only one of them is running at any time.
- That’s why it is possible to safely
cancel a coroutine: by definition, a coroutine can only be cancelled when it’s suspended
at an await expression, so you can perform cleanup by handling the Cancel
ledError exception.
- The multiprocessing.cpu_count() function returns 12 on the
MacBook Pro I’m using to write this chapter. It’s actually a 6-CPU
Core-i7, but the OS reports 12 CPUs because of hyperthreading, an
Intel technology which executes 2 threads per core. However,
hyperthreading works better when one of the threads is not working
as hard as the other thread in the same core—perhaps the first
is stalled waiting for data after a cache miss, and the other is
crunching numbers. Anyway, there’s no free lunch: this laptop performs
like a 6-CPU machine for compute-intensive work that
doesn’t use a lot of memory—like that simple primality test.
- Loops, Sentinels, and Poison Pills
- The loop ends when the queue produces a
sentinel value. In this pattern, the sentinel that shuts down the worker is often called a
“poison pill.”
- A race condition is a bug that may or may not occur depending on
the order of actions performed by concurrent execution units. If
“A” happens before “B,” all is fine; but it “B” happens first, something
goes wrong. That’s the race.
- threads - To switch to a new thread, the OS
needs to save CPU registers and update the program counter and stack pointer, triggering expensive side effects like invalidating CPU caches and possibly even
swapping memory pages.
- The GIL makes the interpreter faster when running on a single core, and its
implementation simpler.18 The GIL also makes it easier to write simple extensions
through the Python/C API.
- The main point: all of these application servers can potentially use all CPU cores on
the server by forking multiple Python processes to run traditional web apps written
in good old sequential code in Django, Flask, Pyramid, etc. This explains why it’s
been possible to earn a living as a Python web developer without ever studying the
threading, multiprocessing, or asyncio modules: the application server handles
concurrency transparently.
- Celery and RQ are the best known open source task queues with Python APIs.
- These products wrap a message queue and offer a high-level API for delegating tasks
to workers, possibly running on different machines.
- In the context of task queues, the words producer and consumer are
used instead of traditional client/server terminology. For example,
a Django view handler produces job requests, which are put in the
queue to be consumed by one or more PDF rendering processes
- My Perl script is faster than your Hadoop cluster.

# The Real Impact of the GIL

