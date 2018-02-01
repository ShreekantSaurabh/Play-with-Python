def even_odd(number):
    if number % 2 == 0:
        print(str(number) + ' is even')
    if number % 2 != 0:
        print(str(number) + ' is odd')
        


def generate(start):
        for i in range(start):
            even_odd(start)
            yield(start)
            start = start +1


gen = generate(10)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
