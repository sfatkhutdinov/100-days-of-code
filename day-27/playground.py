def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 1, 1, 1, 1))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.seats = kwargs.get('seats')


my_car = Car(make='Nissan', model='Altima')
print(my_car.seats)
