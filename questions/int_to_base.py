def number_to_base(x, b):
    """
    Converts a provided number to a number in the provided base

    Parameters
    ------------------------------
    x: int
        Number to convert
    b: int
        Base to convert the number

    Returns
    ------------------------------
    str
        Result of conversion represented as a string
    """
    if x == 0:
        return "0"
    digits = list()
    while x:
        digits.append(int(x % b))
        x //= b
    digits.reverse()
    num_str = str()
    for n in digits:
        num_str += str(n)
    return num_str

def base_converter_input():
    """
    Receives the user input for the number converter

    Returns
    ------------------------------
    str
        Result of conversion represented as a string after calling the number_to_base  function
    """
    print("Insert number: ")
    x = int(input())
    print("Insert base: ")
    b = int(input())
    return number_to_base(x, b)

if __name__ == "__main__":
    print(base_converter_input())
