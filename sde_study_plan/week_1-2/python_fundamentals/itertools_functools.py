from itertools import chain

a = [1,2,4]
b = [3,6,[77]] 
c = (5,99)
d = {"name":"arjun", 'age': "25"}
res = chain(a, b, c, d)
print(list(res))


a = [[1,2,4], [3,6,[77]], (5,99), {"name":"arjun", 'age': "25"}]
res = chain.from_iterable(a)
print(list(res))


from itertools import groupby
a = [1, 1, 2,2,2,2,1,3,3,4,5, "arjun", "arun"]
for key , val in groupby(a):
    print(f"key is {key} and value is {list(val)}")


a = [ "arjun", "arun", "bob", "ajay", "bunny", "charles", "jake"]
for key , val in groupby(a, key= lambda a : a[0]):
    print(f"key is {key} and value is {list(val)}")


from itertools import accumulate
a = [1, 1, 2,2,2,2,1,3,3,4,5]
res = accumulate(a)
print(list(res))



from functools import lru_cache
import time

@lru_cache(maxsize=None) # maxsize=None means unlimited cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

start = time.time()
fibonacci(30)
end = time.time()
print(f"Time with cache: {end - start:.6f} seconds")

# Without cache (would be much slower)
def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

start = time.time()
fibonacci_no_cache(30)
end = time.time()
print(f"Time without cache: {end - start:.6f} seconds")


@lru_cache(typed=True)
def process_data(value):
    print(f"Processing: {value} ({type(value)})")
    return value * 2

print(process_data(5))      # Cache miss
print(process_data(5.0))    # Cache miss (due to typed=True)
print(process_data(5)  )    # Cache hit