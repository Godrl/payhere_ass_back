import re
from time import time
from uuid import uuid4


def get_time(seconds_precision=True):
    """Return current time as Unix/Epoch timestamp, in seconds.
    :param seconds_precision: if True, return with seconds precision as integer (default).
                              If False, return with milliseconds precision as floating point number of seconds.
    """
    return time() if not seconds_precision else int(time())


def get_uuid():
    """Return a UUID4 as string"""
    return str(uuid4())


def check_regex(key, value):
    regex_dictionary = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    }

    return True if re.fullmatch(regex_dictionary.get(key), value) else False
