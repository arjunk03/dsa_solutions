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


from functools import reduce

numbers = [1, 2, 3]

# Without initializer (default: first element is initial value)
sum_no_init = reduce(lambda x, y: x + y, numbers)
print(sum_no_init) # Output: 6 (1+2=3, 3+3=6)

# With initializer
sum_with_init = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_init) # Output: 16 (10+1=11, 11+2=13, 13+3=16)

# Example: Concatenating strings with an initial empty string
words = ["hello", "world"]
sentence = reduce(lambda x, y: x + " " + y, words, "")
print(sentence) # Output: " hello world"

from functools import reduce
import operator # operator.add is more efficient than lambda x,y: x+y

numbers = [1, 2, 3, 4, 5]
total_sum = reduce(operator.add, numbers)
print(total_sum) # Output: 15


from functools import partial

def power(base, exponent):
    return base ** exponent

# map expects a function that takes one argument.
# We want to calculate 2^x for a list of x values.
# power_of_2 is a new function where 'base' is fixed to 2.
power_of_2 = partial(power, 2)

numbers = [1, 2, 3, 4, 5]
results = list(map(power_of_2, numbers))
print(results) # Output: [2, 4, 8, 16, 32]



def complex_func(a, b, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")

# Fix 'a' and 'c'
p = partial(complex_func, 10, c=30)

# Call with remaining arguments
p(20, d=40) # Output: a=10, b=20, c=30, d=40


# Squaring numbers using map
numbers = [1, 2, 3, 4, 5]
squared_map = map(lambda x: x * x, numbers)
print(squared_map) # <map object at 0x...> (an iterator)
print(list(squared_map)) # [1, 4, 9, 16, 25]

# Using map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
added_map = map(lambda x, y: x + y, list1, list2)
print(list(added_map)) # [11, 22, 33]



# Squaring numbers using a generator expression
numbers = [1, 2, 3, 4, 5]
squared_gen_exp = (x * x for x in numbers)
print(squared_gen_exp) # <generator object <genexpr> at 0x...> (an iterator)
print(list(squared_gen_exp)) # [1, 4, 9, 16, 25]

# Generator expression with filtering
even_squared = (x * x for x in numbers if x % 2 == 0)
print(list(even_squared)) # [4, 16]

# Generator expression with multiple iterables (using zip)
list1 = [1, 2, 3]
list2 = [10, 20, 30]
added_gen_exp = (x + y for x, y in zip(list1, list2))
print(list(added_gen_exp)) # [11, 22, 33]