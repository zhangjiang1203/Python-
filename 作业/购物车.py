def functionNmae(func):
    def wrapper(*args,**kwargs):
        print('我就是你')
        res = func(*args,**kwargs)
        return res

    return wrapper


@functionNmae
def show():
    print('我就是我')


show()