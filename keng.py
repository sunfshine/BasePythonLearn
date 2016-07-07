x = 10
#when you make an assignment to a variable in a scope, 
#that variable is automatically considered by Python to be local to that scope and shadows any similarly named variable in any outer scope.
def foo():
    x += 2
    print x
foo()