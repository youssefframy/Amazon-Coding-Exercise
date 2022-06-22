import queue

def createGrid():
    grid = []
    grid.append(["O","#", " ", " ", " ", " ", " ", " ", "#", " "])
    grid.append([" ","#", " ", " ", " ", "#", " ", " ", " ", " "])
    grid.append([" ","#", " ", " ", " ", "#", " ", " ", " ", " "])
    grid.append([" ","#", "#", " ", "#", " ", " ", "#", " ", " "])
    grid.append([" ","#", " ", " ", " ", " ", "#", " ", "#", " "])
    grid.append([" ","#", " ", "#", " ", " ", " ", " ", " ", "#"])
    grid.append([" ","#", " ", " ", " ", "#", " ", " ", " ", " "])
    grid.append([" ","#", "#", " ", "#", "#", " ", " ", " ", " "])
    grid.append([" ","#", " ", " ", " ", " ", " ", "#", "#", "#"])
    grid.append([" "," ", " ", " ", " ", " ", " ", " ", " ", "X"])


    return grid


def printGrid(grid, path=""):
    for x, pos in enumerate(grid[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(grid):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print(f"({j},{i})", end="")
        print()
        


def valid(grid, moves):
    for x, pos in enumerate(grid[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(grid[0]) and 0 <= j < len(grid)):
            return False
        elif (grid[j][i] == "#"):
            return False

    return True


def findEnd(grid, moves):
    for x, pos in enumerate(grid[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    count = 0
    for move in moves:
        count = count + 1
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if grid[j][i] == "X":
        print(f"Number of moves: {count} ")
        printGrid(grid, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
grid  = createGrid()

while not findEnd(grid, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(grid, put):
            nums.put(put)