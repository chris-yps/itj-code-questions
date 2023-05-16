def divisible_list(x: int, y: int):
    """
    Creates a list of integers in a provided range which members are divisible by 5 but not divisible by 7

    Parameters
    ------------------------------
    x: int
        Start of the interval
    y: int
        End of the interval

    Returns
    ------------------------------
    list
        List of numbers in interval divisible by 5 but not by 7
    """
    divisible_list = list()

    for n in range(x, y+1):
        if n % 5 == 0 and n % 7 != 0:
            divisible_list.append(n)

    return divisible_list


if __name__ == "__main__":
    print("Insert x: ")
    x = int( input() )
    print("Insert y: ")
    y = int( input() )

    divisible_list_value = divisible_list(x, y)

    print(f"List of numbers: \n {divisible_list_value}")
