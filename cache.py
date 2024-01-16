"""
Caching in Django is a mechanism that stores frequently accessed data in a temporary storage 
location, known as a cache, to improve system performance and reduce the time and resources required 
to fetch or generate data

"""

# 1.     File System Caching: This method involves serializing and storing individual cache values in a file. 
#       You need to specify the path to the directory to be used to store the cache


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# 2.     Memcached Caching: This method involves storing cache values in a shared memory location.

#       This is the most efficient way of caching. It stores the cached data in memory. Django supports using Memcached 
#       as a cache backend, which is a fast memory-based cache server that can handle high loads of data

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# 3.     Redis Caching: This method involves storing cache values in a shared memory location.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'CLIENT_CLASS':'redis_cache.client.DefaultClient',
        }
    }
}

# 4.     Database Caching: This method involves storing cache values in a shared memory location.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': '127.0.0.1:3306',
        'OPTIONS': {
            'CLIENT_CLASS': 'django.db.backends.mysql',
            'CONN_MAX_AGE': 600,
        }
    }
}

