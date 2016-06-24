import time
def make_timer():
    last_call = None
    def escapeTime():
        nonlocal last_call
        now = time.time()
        if last_call is None:
            last_call = now
            return None
        result = now - last_call
        last_call = now
        return result
    return escapeTime

