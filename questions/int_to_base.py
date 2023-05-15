def number_to_base(x, b):
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
    print("Insert number: ")
    x = int(input())
    print("Insert base: ")
    b = int(input())
    return number_to_base(x, b)

print(base_converter_input())
