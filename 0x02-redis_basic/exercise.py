#!/usr/bin/env python3
import redis
import uuid
from typing import Callable, Union, Optional
import functools


# Decorator to count number of calls to a method
def count_calls(method: Callable) -> Callable:
    """Count the number of times a method is called.

    Args:
        method: The method to be wrapped

    Returns:
        A wrapped version of the method that also increments a Redis counter
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the Redis counter for the given method and return the result of the method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


# Decorator to save input/output arguments and results of a method
def call_history(method: Callable) -> Callable:
    """Save the input/output arguments and results of a method.

    Args:
        method: The method to be wrapped

    Returns:
        A wrapped version of the method that saves the input/output arguments and results to Redis
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Save the input arguments, output arguments and result of the method to Redis"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    """Cache class that stores data in Redis

    Attributes:
        _redis: A Redis client
    """
    def __init__(self):
        """Create a new Cache instance

        Clears the Redis database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store an item in the cache

        Generates a unique key for the item and stores the item in Redis

        Args:
            data: The data to be stored

        Returns:
            The key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve an item from the cache

        If the key is not found in the cache, returns None

        Args:
            key: The key used to store the data
            fn: Optional function to apply to the retrieved data

        Returns:
            The data stored at the key, or None if the key is not found
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve a string from the cache

        If the key is not found in the cache, or the
        data is not a string, returns None

        Args:
            key: The key used to store the data

        Returns:
            The data stored at the key as a string, or None if
            the key is not found or the data is not a string
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve an integer from the cache

        If the key is not found in the cache, or the data is not an
        integer, returns None

        Args:
            key: The key used to store the data

        Returns:
            The data stored at the key as an integer, or None if
            the key is not found or the data is not an integer
        """
        return self.get(key, int)