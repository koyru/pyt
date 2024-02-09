
var = 1

def func(arg): # arg is a copy of var
    arg += 1
    return arg

var = func(var)

print(var)




