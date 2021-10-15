
def tripler(func):


    def init():
        func()
        func()
        func()
    return init

@tripler
def printfunc():
    print("The students will be called three times")
    
printfunc()
