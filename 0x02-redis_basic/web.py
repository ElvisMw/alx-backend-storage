#!/usr/bin/env python3
"""
This module defines a function for fetching web pages with caching and tracking
using Redis.
"""
import redis
import requests
from typing import Callable

# Initialize Redis client
r = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetch the content of a web page and cache it in Redis with an expiration.

    Track how many times a particular URL was accessed.

    Args:
        url (str): The URL of the web page to fetch.

    Returns:
        str: The content of the web page.
    """
    # Track the number of times the URL is accessed
    r.incr(f"count:{url}")

    # Check if the URL content is already cached
    cached_content = r.get(f"cached:{url}")
    if cached_content:
        return cached_content.decode('utf-8')

    # Fetch the web page content
    response = requests.get(url)
    content = response.text

    # Cache the content with an expiration time of 10 seconds
    set_result = r.setex(f"cached:{url}", 10, content)
    if set_result != b'OK':
        print(f"Failed to cache the content for URL: {url}")

    return content


def replay(method: Callable):
    """
    Displays the history of calls to a particular method.

    Args:
        method (Callable): The method to replay the call history for.
    """
    cache = method.__self__
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> "
              f"{out.decode('utf-8')}")
