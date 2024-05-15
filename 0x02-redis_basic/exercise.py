#!/usr/bin/env python3
import redis
import uuid
from typing import Callable, Union, Optional


class Cache:
    """
    Simple cache using Redis

    Exposes methods to store data, retrieve data,
    and retrieve data in different formats
    """
    def __init__(self):
        """
        Create a new Cache object

        Creates a new Redis connection and
        flushes the database (to start with a clean slate)
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the cache

        Generates a new key, sets the key to the data,
        and returns the key

        Args:
            data: The data to store

        Returns:
            The key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from the cache

        Retrieves data from the cache using the key,
        and optionally applies a function to the data

        Args:
            key: The key used to store the data
            fn: A function to apply to the data

        Returns:
            The data retrieved from the cache,
            or None if the key does not exist
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve a string from the cache

        Retrieves data from the cache using the key,
        and decodes it to a string

        Args:
            key: The key used to store the data

        Returns:
            The data retrieved from the cache,
            or None if the key does not exist
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer from the cache

        Retrieves data from the cache using the key,
        and converts it to an integer

        Args:
            key: The key used to store the data

        Returns:
            The data retrieved from the cache,
            or None if the key does not exist
        """
        return self.get(key, int)