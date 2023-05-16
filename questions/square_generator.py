import math

def create_generator(n: int):
    """
    Creates a generator with the perfects squares beforea provided number

    Parameters
    ------------------------------
    n: int
        Number to check all perfect squares before

    Returns
    ------------------------------
    generator
        Generator containing the perfect squares
    """
    for i in range(1, n):
        if is_square(i):
            yield i

def is_square(n):
    """
    Checks if the square root of the provided number is a perfect square

    Parameters
    ------------------------------
    n: int
        Number to check square root

    Returns
    ------------------------------
    bool
        True if it's a perfect square, False if it isn't
    """
    return math.sqrt(n).is_integer()

if __name__ == "__main__":
    print("Insert number: ")
    n = int(input())
    mygenerator = create_generator(n)
    for i in mygenerator:
        print(i)
