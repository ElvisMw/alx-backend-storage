#!/usr/bin/env python3
import redis
import uuid
from typing import Callable, Optional, Union
import functools


# Decorator to count the number of times a method is called
def count_calls(method: Callable) -> Callable:
    """Count the number of times a method is called

    Args:
        method: Method to be wrapped

    Returns:
        Wrapped method
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increments the number of times the method is called

        Args:
            self: Cache instance
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        Returns:
            Whatever the wrapped method returns
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class

    Stores data in Redis
    """
    def __init__(self):
        """Constructor

        Connects to Redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis

        Creates a new key and stores the data in it

        Args:
            data: Data to be stored

        Returns:
            Key where the data is stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get data from Redis

        Gets data from the specified key

        Args:
            key: Key where the data is stored
            fn: Function to be applied to the data, if present

        Returns:
            Data from the key, or None if not found
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Get string data from Redis

        Gets data from the specified key and decodes it as a string

        Args:
            key: Key where the data is stored

        Returns:
            String data from the key, or None if not found
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Get int data from Redis

        Gets data from the specified key and converts it to an integer

        Args:
            key: Key where the data is stored

        Returns:
            Integer data from the key, or None if not found
        """
        return self.get(key, int)