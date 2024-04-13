from functools import wraps
from datetime import datetime


def timer(f):
    @wraps(f)
    def decorated_view(*args, **kwargs):
        start = datetime.now()
        rv = f(*args, **kwargs)
        end = datetime.now()
        time_elapsed = end - start
        print(time_elapsed.microseconds)
        return rv
    return decorated_view
