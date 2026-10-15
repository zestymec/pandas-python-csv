def add(*args):
    print(args[1])
    totall = 0
    for n in args:
        totall += n
    print(totall)

add(5, 10, 5, 34)


def calculate(n , **kwargs):
    for key , value in kwargs.items():
        print(key , value)
        n+=value
    print(kwargs["add"])

       
    print(n)


calculate(5 ,add=4 , multiply=5 , umer =34)