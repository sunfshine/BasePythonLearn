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


def test_multi_para_func(para1,     para2):
    print para1, para2
dfs = None
ddfdf = None
test_multi_para_func(dfs, ddfdf)
make_timer()

print "222"
