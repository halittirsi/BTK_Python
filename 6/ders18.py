#Python Scope

x = 50

def myfunc():
    global x
    x = 300
    print(x)

def func2():
    print(x)

func2()
myfunc()
func2()