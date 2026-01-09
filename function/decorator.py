
def logging(func):
    def wrapper(*args, **kwargs):
        print("addind", args)
        res = func(*args, **kwargs)
        return res
    return wrapper

@logging
def add(a, b):
    return a+b


print(add(2,4))