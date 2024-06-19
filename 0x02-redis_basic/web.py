#!/usr/bin/env python3
'''
return count
'''
import redis
import requests
from functools import wraps


r = redis.Redis()


def counter(method):
    '''decorator'''
    @wraps(method)
    def wrapper(url):
        '''a wrapper function'''
        key = "cached:" + url
        cached_value = r.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

        key_count = "count:" + url
        content = method(url)

        r.incr(key_count)
        r.set(key, content, ex=10)
        r.expire(key, 10)
        return content
    return wrapper


@counter
def get_page(url: str) -> str:
    '''get contents of html'''
    result = requests.get(url)
    return result.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
