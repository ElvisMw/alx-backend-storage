#!/usr/bin/env python3
import redis
import requests
from typing import Callable


def get_page(url: str) -> str:
    """
    Retrieve a web page either from cache or from the internet.

    Args:
        url (str): The URL of the web page to retrieve.

    Returns:
        str: The contents of the web page.
    """
    redis_client = redis.Redis()
    count_key = f"count:{url}"
    cache_key = f"cache:{url}"

    """ Increment the number of times this URL has been accessed """
    redis_client.incr(count_key)

    """" Check if the URL is already in the cache """
    cached_page = redis_client.get(cache_key)

    if cached_page:
        """ If the URL is in the cache, return the cached page """
        return cached_page.decode('utf-8')

    """ If the URL is not in the cache, retrieve the page from the internet """
    response = requests.get(url)

    """ Set the page in the cache with a TTL of 10 seconds """
    redis_client.setex(cache_key, 10, response.text)

    """ Return the page """
    return response.text