'''
Generators
----------
-->Generators in python is enable lazy evaluation for producing sequence of values efficiently.
-->They differ from regular functions by execution and resuming on demand.
-->Generators create iterators that yield values one at a time using the yield keyword

Function vs Generators
-----------------------
-->Regular functions execute fully upon call and return a single value,terminating afterward.
-->Generators use yield to produce multiple value lazily, acting like iterators without building the entire sequence in memory.

def count_(num):
    i = 1
    while i<=num:
        yield i
        i += 1
Gene_ = count_(3)
print(next(Gene_))
print(next(Gene_))
print(next(Gene_))

Yield
-----
-->Yield pauses the generator function, saves its state(local variable, position), and returns the yielded value to the caller.

Next
----
-->This advances the generator by executing until the next yield, returning that value, subsequent calls resume from there. 
'''
def message_gen():
    yield("First msg")
    yield("second msg")
    yield("third msg")
gen_=message_gen()
print(next(gen_))
print(next(gen_))
print(next(gen_))





