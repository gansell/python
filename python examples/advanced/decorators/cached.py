"""Caching results with a decorator.
"""

import functools
import pickle


def cached(func):
    """Decorator that caches.
    """
    cache = {}

    @functools.wraps(func)
    def _cached(*args, **kwargs):
        """Takes the arguments.
        """
        # dicts cannot be use as dict keys
        # dumps are strings and can be used
        key = pickle.dumps((args, kwargs))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return _cached
