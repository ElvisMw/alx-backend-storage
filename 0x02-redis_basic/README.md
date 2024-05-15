
# 0x02. Redis Basic
## Questions
### 0. Writing strings to Redis
Create a Cache class.
In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.
Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g., using uuid), store the input data in Redis using the random key, and return the key.
Type-annotate store correctly. Remember that data can be a str, bytes, int, or float.
### 1. Reading from Redis and recovering original type
Create a get method that takes a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.
Conserve the original Redis.get behavior if the key does not exist.
Implement two new methods: get_str and get_int that will automatically parametrize Cache.get with the correct conversion function.
### 2. Incrementing values
Familiarize yourself with the INCR command and its Python equivalent.
Implement a system to count how many times methods of the Cache class are called.
Define a count_calls decorator that takes a single method Callable argument and returns a Callable.
Use the qualified name of the method using the __qualname__ dunder method as a key.
Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.
Decorate Cache.store with count_calls.
### 3. Storing lists
Familiarize yourself with Redis commands RPUSH, LPUSH, LRANGE, etc.
Define a call_history decorator to store the history of inputs and outputs for a particular function.
Every time the original function is called, add its input parameters to one list in Redis, and store its output into another list.
In call_history, use the decorated function’s qualified name and append :inputs and :outputs to create input and output list keys, respectively.
call_history has a single parameter named method that is a Callable and returns a Callable.
In the new function that the decorator will return, use rpush to append the input arguments. Normalize input arguments using str(args).
Execute the wrapped function to retrieve the output. Store the output using rpush in the ...:outputs list, then return the output.
Decorate Cache.store with call_history.
### 4. Retrieving lists
Implement a replay function to display the history of calls of a particular function.

```Use keys generated in previous tasks to generate the following output:
python
Copy code
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```
### 5. Implementing an expiring web cache and tracker (advanced)
Implement a get_page function (prototype: def get_page(url: str) -> str:). Use the requests module to obtain the HTML content of a particular URL and return it.
Track how many times a particular URL was accessed in the key count:{url} and cache the result with an expiration time of 10 seconds.
Use http://slowwly.robertomurray.co.uk to simulate a slow response and test your caching.
Bonus: implement this use case with decorators.