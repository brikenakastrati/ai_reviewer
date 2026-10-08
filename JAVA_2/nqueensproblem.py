def solve_8_queens():
    """
    Solve the 8-Queens problem using Depth-First Search (DFS)
    with an explicit stack.

    The goal is to place 8 queens on an 8x8 chessboard such that
    no two queens attack each other.

    A queen attacks another queen if they are in the same:
        - row
        - column
        - diagonal

    Each state in the stack represents a partial solution.
    The position in the list represents the row, while the value
    represents the column where the queen is placed.

    Example:
        [0, 4, 7]
        means:
            Row 0 -> Column 0
            Row 1 -> Column 4
            Row 2 -> Column 7

    Returns:
        list: A solution containing the column position of each
              queen for rows 0 through 7, or None if no solution
              exists.
    """

    N = 8

    # Stack used to implement DFS.
    # Initially, we have an empty board.
    stack = [[]]

    # Continue searching while there are states in the stack.
    while stack:

        # Remove the last element from the stack.
        # This gives us LIFO behavior and therefore implements DFS.
        queens = stack.pop()

        # If 8 queens have been placed, we found a solution.
        if len(queens) == N:
            return queens

        # The next queen will be placed in the next row.
        row = len(queens)

        # Try placing the queen in every column.
        for col in range(N):

            # Check if the column is already occupied.
            if col in queens:
                continue

            # Check whether the position is on the same
            # diagonal as any previously placed queen.
            safe = True

            for previous_row in range(row):
                previous_col = queens[previous_row]

                # Two positions are on the same diagonal when
                # the difference between their rows equals the
                # difference between their columns.
                if abs(row - previous_row) == abs(col - previous_col):
                    safe = False
                    break

            # If the position is safe, create a new state
            # and add it to the DFS stack.
            if safe:
                stack.append(queens + [col])

    # No solution was found.
    return None


def print_board(solution):
    """
    Print an 8x8 chessboard based on a given solution.

    Args:
        solution (list): A list where the index represents the row
                         and the value represents the column of
                         the queen.

    Returns:
        None
    """

    N = 8

    # Go through every row.
    for row in range(N):

        # Go through every column.
        for col in range(N):

            # Print Q if a queen is located here.
            if solution[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


def main():
    """
    Main function that solves the 8-Queens problem using DFS
    and prints the resulting chessboard.
    """

    solution = solve_8_queens()

    if solution:
        print("Solution:", solution)
        print("\nChessboard:")
        print_board(solution)
    else:
        print("No solution found.")


# Run the program.
if __name__ == "__main__":
    main()