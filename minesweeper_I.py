# UGLY CODE

# This challenge is based on the game Minesweeper.

# Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot. 
# Return a list where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).

# Examples
# num_grid([
#   ["-", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-"],
#   ["-", "-", "#", "-", "-"],
#   ["-", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-"]
# ]) ➞ [
#   ["0", "0", "0", "0", "0"],
#   ["0", "1", "1", "1", "0"],
#   ["0", "1", "#", "1", "0"],
#   ["0", "1", "1", "1", "0"],
#   ["0", "0", "0", "0", "0"],
# ]

# num_grid([
#   ["-", "-", "-", "-", "#"],
#   ["-", "-", "-", "-", "-"],
#   ["-", "-", "#", "-", "-"],
#   ["-", "-", "-", "-", "-"],
#   ["#", "-", "-", "-", "-"]
# ]) ➞ [
#   ["0", "0", "0", "1", "#"],
#   ["0", "1", "1", "2", "1"],
#   ["0", "1", "#", "1", "0"],
#   ["1", "2", "1", "1", "0"],
#   ["#", "1", "0", "0", "0"]
# ]

# num_grid([
#   ["-", "-", "-", "#", "#"],
#   ["-", "#", "-", "-", "-"],
#   ["-", "-", "#", "-", "-"],
#   ["-", "#", "#", "-", "-"],
#   ["-", "-", "-", "-", "-"]
# ]) ➞ [
#   ["1", "1", "2", "#", "#"],
#   ["1", "#", "3", "3", "2"],
#   ["2", "4", "#", "2", "0"],
#   ["1", "#", "#", "2", "0"],
#   ["1", "2", "2", "1", "0"],
# ]


def num_grid(lst):
    # Create zero grid
    zeroGrid = [[0 for i in lst[0]] for i in lst]
    
    # loop through grid and detect mines
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == '#':
                zeroGrid[i][j] = -100000
                
                # check if in one of the corners or against a wall. (many ifs)
                if (i==0):
                    zeroGrid[i+1][j] += 1
                    # case top left corner
                    if (j==0):
                        zeroGrid[i][j+1] += 1
                        zeroGrid[i+1][j+1] += 1
                    # case top right corner
                    elif (j == len(lst[1])-1):
                        zeroGrid[i][j-1] += 1
                        zeroGrid[i+1][j-1] += 1
                    # case top wall
                    else:
                        zeroGrid[i][j-1] += 1
                        zeroGrid[i+1][j-1] += 1
                        zeroGrid[i][j+1] += 1
                        zeroGrid[i+1][j+1] += 1

                elif (i == len(lst)-1):
                    zeroGrid[i-1][j] += 1
                    # case bottom left corner
                    if (j==0):
                        zeroGrid[i][j+1] += 1
                        zeroGrid[i-1][j+1] += 1
                    # case bottom right corner
                    elif (j == len(lst[1])-1):
                        zeroGrid[i][j-1] += 1
                        zeroGrid[i-1][j-1] += 1
                    # case bottom wall
                    else:
                        zeroGrid[i][j-1] += 1
                        zeroGrid[i-1][j-1] += 1
                        zeroGrid[i][j+1] += 1
                        zeroGrid[i-1][j+1] += 1
                
                # case wall left
                elif (j == 0):
                    zeroGrid[i-1][j] += 1
                    zeroGrid[i-1][j+1] += 1
                    zeroGrid[i][j+1] += 1
                    zeroGrid[i+1][j+1] += 1
                    zeroGrid[i+1][j] += 1
                # case wall right
                elif (j == len(lst[1])-1):
                    zeroGrid[i-1][j] += 1
                    zeroGrid[i-1][j-1] += 1
                    zeroGrid[i][j-1] += 1
                    zeroGrid[i+1][j-1] += 1
                    zeroGrid[i+1][j] += 1
                # case not against wall
                else:
                    zeroGrid[i-1][j] += 1
                    zeroGrid[i-1][j+1] += 1
                    zeroGrid[i][j+1] += 1
                    zeroGrid[i+1][j+1] += 1
                    zeroGrid[i+1][j] += 1
                    zeroGrid[i-1][j-1] += 1
                    zeroGrid[i][j-1] += 1
                    zeroGrid[i+1][j-1] += 1

    # replace big negative with '#' 
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if (zeroGrid[i][j] < 0):
                zeroGrid[i][j] = '#'

    # int array -> string array
    for i in range(len(zeroGrid)):
        zeroGrid[i] = list(map(str, zeroGrid[i]))

    for i in zeroGrid:
        print (i)

    return (zeroGrid)
