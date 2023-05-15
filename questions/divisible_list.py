def divisibleList(x: int, y: int):
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

    divisible_list = divisibleList(x, y)

    print(f"List of numbers: \n {divisible_list}")
