"""
Shared utility functions for TaskFlow.
"""

import logging

from django.core.cache import cache

logger = logging.getLogger('apps')


def invalidate_cache_pattern(pattern):
    """
    Invalidate all cache keys matching a pattern.
    Uses Redis SCAN to find matching keys.
    """
    try:
        from django_redis import get_redis_connection
        con = get_redis_connection('default')
        keys = con.keys(f'*{pattern}*')
        if keys:
            con.delete(*keys)
            logger.debug(f"Invalidated {len(keys)} cache keys matching '{pattern}'")
    except Exception as e:
        logger.warning(f"Cache invalidation failed for pattern '{pattern}': {e}")


def get_or_set_cache(key, callback, timeout=300):
    """
    Get value from cache, or compute and store it.

    Args:
        key: Cache key string
        callback: Callable that returns the value to cache
        timeout: Cache TTL in seconds (default 5 minutes)

    Returns:
        Cached or freshly computed value
    """
    value = cache.get(key)
    if value is None:
        value = callback()
        cache.set(key, value, timeout)
    return value
