import math

def create_generator(n: int):
    for i in range(1, n):
        if is_square(i):
            yield i

def is_square(n):
    return math.sqrt(n).is_integer()

if __name__ == "__main__":
    print("Insert number: ")
    n = int(input())
    mygenerator = create_generator(n)
    for i in mygenerator:
        print(i)
