#!/usr/bin/env python3
import redis
import uuid
from typing import Union


class Cache:
    """
    Simple cache class that stores data in Redis
    """

    def __init__(self):
        """
        Initialize Redis connection and clear previous data
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a unique key

        Args:
            data: Data to store

        Returns:
            Key under which data is stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key