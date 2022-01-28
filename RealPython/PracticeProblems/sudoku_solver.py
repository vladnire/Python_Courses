""" Sudoku Solver
    NOTE: A description of the Sudoku puzzle can be found at:
        https://en.wikipedia.org/wiki/Sudoku
    Given a string in SDM format, described below, write a program to find and
    return the solution for the Sudoku puzzle given in the string. The solution
    should be returned in the same SDM format as the input.
    Some puzzles will not be solvable. In that case, return the string
    "Unsolvable".
    The general sdx format is described here:
        http://www.sudocue.net/fileformats.php
    For our purposes, each SDX string will be a sequence of 81 digits, one for
    each position on the Sudoku puzzle. Known numbers will be given and unknown
    positions will have a zero value.

    For example, this string of digits (split onto two lines for readability):
        0040060790000006020560923000780610305090004
             06020540890007410920105000000840600100

    represents this starting Sudoku puzzle:
             0 0 4   0 0 6   0 7 9
             0 0 0   0 0 0   6 0 2
             0 5 6   0 9 2   3 0 0
             0 7 8   0 6 1   0 3 0
             5 0 9   0 0 0   4 0 6
             0 2 0   5 4 0   8 9 0
             0 0 7   4 1 0   9 2 0
             1 0 5   0 0 0   0 0 0
             8 4 0   6 0 0   1 0 0
"""
import copy


"""
TIPS:
Read the puzzle into a grid form.
For each cell:
    For each possible number in that cell:
        Place the number in the cell.
        Remove that number from the row, column, and small square.
        Move to the next position.
    If no possible numbers remain, then declare the puzzle unsolvable.
    If all cells are filled, then return the solution.
"""


def line_to_grid(input_string):
    """Create 9x9 matrix from sdx format string"""
    matrix = []
    for i in range(0,81,9):
        matrix.append(list(int(e) for e in input_string[i:i+9]))

    return matrix


def grid_to_line(grid):
    """Create sdx format string from 9x9 grid"""
    line = ""
    for row in grid:
        line += ''.join(str(e) for e in row)

    return line


def small_square(x, y):
    """
    Search for the smaller three-by-three square 
    a given position is in based on coordinates
    and return coordinates
    """
    upper_x = (x + 3) // 3 * 3 
    upper_y = (y + 3) // 3 * 3 

    for subx in range(upper_x - 3, upper_x):
        for suby in range(upper_y - 3, upper_y):
            # If subX != x or subY != y:
            if not (subx == x and suby == y):
                yield subx, suby


def compute_next_position(x, y):
    """
    Takes the current x and y coordinates as input 
    and returns a tuple containing a finished flag 
    along with the x and y coordinates of the next position
    """
    nexty = y
    nextx = (x + 1) % 9
    if nextx < x:
        nexty = (y + 1) % 9
        if nexty < y:
            return (True, 0, 0)

    return (False, nextx, nexty)


def test_and_remove(value, possible):
    """
    If the value is nonzero and appears in the iterable, 
    then the function removes it from the iterable
    """
    if value != 0 and value in possible:
        possible.remove(value)


def detect_possible(grid, x, y):
    """
    Given a grid and a position on that grid, 
    it determines what values that position could still have:
    """
    if grid[x][y]:
        return [grid[x][y]]

    possible = set(range(1,10))
    # Test horizontal and vertical
    for i in range(9):
        if i != y:
            test_and_remove(grid[x][i], possible)
        if i != x:
            test_and_remove(grid[i][y], possible)

    
    # Test in small square
    for idx, idy in small_square(x, y):
        test_and_remove(grid[idx][idy], possible)

    return list(possible)


def solve(start_grid, x, y):
    temp = copy.deepcopy(start_grid)

    while True:
        possible = detect_possible(temp, x, y)
        # There are no possible values for this position. 
        # That indicates the solution it’s testing can’t work.
        if not possible:
            return False

        # It’s walked to the end of the grid and found a 
        # possible value for each position. The puzzle is solved!
        finished, nextx, nexty = compute_next_position(x, y)
        if finished:
            temp[x][y] = possible[0]

            return temp

        if len(possible) > 1:
            break

        temp[x][y] = possible[0]
        x = nextx
        y = nexty

    # One of the guesses at this position, when passed back
    # to the solver, returns a solution.
    for guess in possible:
        temp[x][y] = guess
        result = solve(temp, nextx, nexty)
        if result:
            return result

    # It’s tried all possible values at this position 
    # and none of them will work.
    return False
        

def sudoku_solve(input_string):
    grid = line_to_grid(input_string)
    answer = solve(grid, 0, 0)
    if answer:
        return grid_to_line(answer)
    else:
        return "Unsolvable"