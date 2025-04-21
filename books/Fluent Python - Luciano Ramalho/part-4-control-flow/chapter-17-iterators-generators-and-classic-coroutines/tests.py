"""sentinel is 1 - equals stopiter;"""
from random import randint


def d6():
    return randint(1, 6)


d6_iter = iter(d6, 1)
# d6_iter
# <callable_iterator object at 0x10a245270>
for roll in d6_iter:
    print(roll)

# 4
# 3
# 6
# 3
print("try 2")
d6_iter = iter(d6, 3)

for roll in d6_iter:
    print(roll)

# for loop
s = 'ABC'
for char in s:
    print(char)

# exact equivalent with while loop

s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break


def sub_gen():
    yield 1.1
    yield 1.2


def gen():
    yield 1
    yield from sub_gen()
    yield 2


for x in gen():
    print(x)

from collections.abc import Generator


def averager() -> Generator[float, float, None]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


coro_avg = averager()
avg_list = []
avg = next(coro_avg)  # we must prime the coroutine (advance to first yield) before sending values
avg_list.append(avg)
avg = coro_avg.send(10)  # Classic generator-based coroutine (not async/await). We use .send() to pass values in.
# this is not async programming, but the coroutine itself keeps state and can update the average over time
avg_list.append(avg)
avg = coro_avg.send(10)
avg_list.append(avg)
avg = coro_avg.send(10)
avg_list.append(avg)
coro_avg.close() # closes coroutine, it cannot used .send anymore.
print(avg_list)
# coro_avg.send(5)
