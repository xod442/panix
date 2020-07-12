import time
from flask import current_app
import datetime

def utc_now_ts():
    return int(time.time())

def utc_now_ts_ms():
    return lambda: int(round(time.time() * 1000))
