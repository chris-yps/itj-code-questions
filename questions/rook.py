class Rook:
    """
    Class representing the rook piece and its movement in a chess board

    Returns
    ------------------------------
    str:
        String describing the number of moves and the distance from the start position
    """

    def __init__(self):
        """
        Starts the position of the rook at coordintates 0,0
        Starts total moves done by the rook at 0
        """
        self._position = [0, 0]
        self._total_moves = 0

    @property
    def summary_string(self):
        """
        Property for getting a summary string for the movements done by the rook

        Returns
        ------------------------------
        str:
            String describing the number of moves and the distance from the start position
        """
        return f"The Rook has traveled a distance of {self.total_moves} spaces and is {self.distance} spaces away from its starting point"

    @property
    def distance(self):
        """
        Poperty for getting the total spaces traveled by the rook

        Returns
        ------------------------------
        int:
            Summatory of the absolute values of the coordinates to determine the distance traveled
        """
        return abs(self._position[0]) + abs(self._position[1])

    @property
    def total_moves(self):
        """
        Poperty for getting the total movement spaces done by the rook after a sequence

        Returns
        ------------------------------
        int:
            total moves after the sequence
        """
        return self._total_moves

    def movement_input(self, direction, moves):
        """
        Take input for sequence of movement and send it to the execute_movement_command function
        Determine the axis and real value of the movement to be done

        Parameters
        ------------------------------
        direction: str
            Direction for the piece to move, used to calculate real value and axis

        moves: str
            moves to be done in the present movement, used to calculate real value
        """
        operator = 1
        axis = ''
        if direction == "2" or direction == "3":
            operator = -1
        if direction == "1" or direction =="2":
            axis = "y"
        elif direction == "3" or direction =="4":
            axis = "x"

        movement_command = [int(moves) * operator, axis]
        self.execute_movement_command(movement_command)

    def execute_movement_command(self, movement_command):
        """
        Calculate the movement in the coordinates according to the real value and the axis.
        Calculate the total moves using the absolute number of movements

        Parameters
        ------------------------------
        movement_command: list
            List containing the real value for the movement and the axis to apply the calculation to.
        """
        if movement_command[1] == "x":
            self._position[0] += movement_command[0]
        elif movement_command[1] == "y":
            self._position[1] += movement_command[0]
        self._total_moves += abs(movement_command[0])


if __name__ == "__main__":
    rook = Rook()

    while True:
        print("Choose a direction:")
        print("1 - Up")
        print("2 - Down")
        print("3 - Left")
        print("4 - Right")
        print("e - Exit")
        print("Choice: ")

        direction = input()
        if direction == "e":
            break

        print("Insert number of spaces to move (input e to exit): ")

        moves = input()
        if moves == "e":
            break

        rook.movement_input(direction, moves)

    print(rook.summary_string)
