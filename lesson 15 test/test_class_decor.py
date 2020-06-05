
class Decor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return_y = sorted(list(self.func(*args, **kwargs)))
        return_z = [i**2 for i in return_y]
        return return_z


@Decor
def text(y):
    return y

print(text([5, 9, 2, 7]))