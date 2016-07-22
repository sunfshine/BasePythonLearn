def _valid_func(t):
    a = t
    try:
        a = int(t)
    except:
        print "exception"
dic_obj = {'a': 1, 'b': 2}
_valid_func(dic_obj)
hhh = dic_obj['a']
print hhh
