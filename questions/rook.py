def rook_movement():
    rook = [0, 0]
    total_moves = 0

    while True:
        movement = print_menu()
        if movement is False:
            break
        if movement[1] == "x":
            rook[0] += movement[0]
        elif movement[1] == "y":
            rook[1] += movement[0]
        total_moves += abs(movement[0])
    distance = abs(rook[0]) + abs(rook[1])
    print(f"The Rook has traveled a distance of {total_moves} spaces and is {distance} spaces away from its starting point")

def print_menu():
    operator = 1

    print("Choose a direction:")
    print("1 - Up")
    print("2 - Down")
    print("3 - Left")
    print("4 - Right")
    print("e - Exit")
    print("Choice: ")
    direction = input()

    if direction == "e":
        return False
    else:
        if direction == "2" or direction == "3":
            operator = -1
        if direction == "1" or direction =="2":
            axis = "y"
        elif direction == "3" or direction =="4":
            axis = "x"

    print("Insert number of spaces to move (input e to exit): ")
    moves = input()
    if moves == "e":
        return False
    return [int(moves) * operator, axis]

if __name__ == "__main__":
    rook_movement()
