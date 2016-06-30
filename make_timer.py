import time
x = 0
def make_timer():
    def escapeTime():
        now = time.time()
        
        if x is None:
            last_call = now
            return None
        result = now - last_call
        last_call = now
        return result
    return escapeTime

