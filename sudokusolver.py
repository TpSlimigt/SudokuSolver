# Alternativt ha en mapp som man lägger sudoku i
def ReadFile(fileName):
    path = "./{}".format(fileName)
    sudoku = []
    try:
        file = open(path)
        fileContent = file.readlines()
        file.close()
    except:
        print("Error: File not valid.")
        return 0
    for line in fileContent:
        newLine = []
        line = line.strip("\n")
        for char in line:
            newLine.append(char)
        sudoku.append(newLine)
    return sudoku


def CheckIsValid(board, row, col, num):
    # Check if num is not in the current row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if num is not in the current column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if num is not in the current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def Solve(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == "0":  # Empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if CheckIsValid(sudoku, row, col, num):
                        sudoku[row][col] = str(num)

                        if Solve(sudoku):
                            return True
                        sudoku[row][col] = "0"  # Backtrack
                return False
    return True


""" def Solve(sudoku, zeroPositions, numbers=[]):
    # Base case, sudoku solved. All blank spaces has numbers.
    if len(numbers) == len(zeroPositions):
        return print(numbers)

    index = len(numbers)

    # Check all the possible numbers at the cell.
    possibleNumbers = CheckForPossibleNumbers(sudoku, zeroPositions[index])
    if not possibleNumbers or len(possibleNumbers) == 0:
        return False

    for pNum in possibleNumbers:
        numbers.append(pNum)

        if Solve(sudoku, zeroPositions, numbers):
            return True

        numbers.pop()

    return False """


# Looks for all the empty cells and returns the coordinates
def CheckForZero(sudoku):
    x = -1
    y = -1

    zeroPositions = []

    for row in sudoku:
        y += 1
        for num in row:
            x += 1
            if num == "0":
                zeroPositions.append((x, y))
        x = -1
    return zeroPositions


# Checks the possible numbers for a given cell
def CheckForPossibleNumbers(sudoku, coordinate):
    possibleNumbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    occupiedNumbers = []

    row = CheckRow(sudoku, coordinate)
    col = CheckCol(sudoku, coordinate)
    block = CheckBlock(sudoku, coordinate)
    # print(row, col, block)

    for r in row:
        if r not in occupiedNumbers:
            occupiedNumbers.append(r)
    for c in col:
        if c not in occupiedNumbers:
            occupiedNumbers.append(c)
    for b in block:
        if b not in occupiedNumbers:
            occupiedNumbers.append(b)

    return possibleNumbers.difference(occupiedNumbers)


# Checks possible numbers on a cell's row
def CheckRow(sudoku, coordinate):
    occupiedNumbers = []
    for num in sudoku[coordinate[1]]:
        if num != "0":
            occupiedNumbers.append(num)
    return occupiedNumbers if len(occupiedNumbers) > 0 else ["0"]


# Checks possible numbers on a cell's column
def CheckCol(sudoku, coordinate):
    occupiedNumbers = []
    col = coordinate[0]
    for row in range(9):
        num = CheckCell(sudoku, (col, row))
        if num != "0":
            occupiedNumbers.append(num)
    return occupiedNumbers if len(occupiedNumbers) > 0 else ["0"]


# Checks possible numbers on a cell's block
def CheckBlock(sudoku, coordinate):
    occupiedNumbers = []
    currentBlock = (int((coordinate[0]) / 3), int((coordinate[1]) / 3))
    currentBlockStartCell = (currentBlock[0] * 3, currentBlock[1] * 3)
    for row in range(0, 3):
        for col in range(0, 3):
            num = CheckCell(
                sudoku, (currentBlockStartCell[0] + col, currentBlockStartCell[1] + row)
            )
            if num != "0":
                occupiedNumbers.append(num)
    return occupiedNumbers if len(occupiedNumbers) > 0 else ["0"]


# Gets the value of given cell
def CheckCell(sudoku, coordinate):
    return sudoku[coordinate[1]][coordinate[0]]


# Renders the sudoku to a file
def RenderSudoku(sudoku):
    topLeftCorner = "╔"
    bottomLeftCorner = "╚"
    topRightCorner = "╗"
    bottomRightCorner = "╝"
    horizontalBlock = "═"
    horizontal = "─"
    horizontalBlockDown = "╦"
    horizontalDown = "╤"
    horizontalBlockUp = "╩"
    horizontalUp = "╧"
    verticalBlock = "║"
    vertical = "│"
    verticalLeftBlock = "╠"
    verticalLeft = "╟"
    verticalRightBlock = "╣"
    verticalRight = "╢"
    intersectionBlock = "╬"
    intersection = "┼"
    intersectionHorizontalBlockCell = "╪"
    intersectionVerticalBlockCell = "╫"
    # empty = " "  # Number goes here

    topRow = [0]
    bottomRow = [18]
    blockDividerRow = [6, 12]
    numberDividerRow = [2, 4, 8, 10, 14, 16]
    numberRow = [1, 3, 5, 7, 9, 11, 13, 15, 17]

    sudokuRow = 0
    sudokuRender = []

    for row in range(19):
        newRow = []
        if row in topRow:
            newRow.append(topLeftCorner)
            newRow.append(horizontalBlock)
            newRow.append(horizontalDown)
            newRow.append(horizontalBlock)
            newRow.append(horizontalDown)
            newRow.append(horizontalBlock)
            newRow.append(horizontalBlockDown)
            newRow.append(horizontalBlock)
            newRow.append(horizontalDown)
            newRow.append(horizontalBlock)
            newRow.append(horizontalDown)
            newRow.append(horizontalBlock)
            newRow.append(horizontalBlockDown)
            newRow.append(horizontalBlock)
            newRow.append(horizontalDown)
            newRow.append(horizontalBlock)
            newRow.append(horizontalDown)
            newRow.append(horizontalBlock)
            newRow.append(topRightCorner)

        elif row in bottomRow:
            newRow.append(bottomLeftCorner)
            newRow.append(horizontalBlock)
            newRow.append(horizontalUp)
            newRow.append(horizontalBlock)
            newRow.append(horizontalUp)
            newRow.append(horizontalBlock)
            newRow.append(horizontalBlockUp)
            newRow.append(horizontalBlock)
            newRow.append(horizontalUp)
            newRow.append(horizontalBlock)
            newRow.append(horizontalUp)
            newRow.append(horizontalBlock)
            newRow.append(horizontalBlockUp)
            newRow.append(horizontalBlock)
            newRow.append(horizontalUp)
            newRow.append(horizontalBlock)
            newRow.append(horizontalUp)
            newRow.append(horizontalBlock)
            newRow.append(bottomRightCorner)

        elif row in numberDividerRow:
            newRow.append(verticalLeft)
            newRow.append(horizontal)
            newRow.append(intersection)
            newRow.append(horizontal)
            newRow.append(intersection)
            newRow.append(horizontal)
            newRow.append(intersectionVerticalBlockCell)
            newRow.append(horizontal)
            newRow.append(intersection)
            newRow.append(horizontal)
            newRow.append(intersection)
            newRow.append(horizontal)
            newRow.append(intersectionVerticalBlockCell)
            newRow.append(horizontal)
            newRow.append(intersection)
            newRow.append(horizontal)
            newRow.append(intersection)
            newRow.append(horizontal)
            newRow.append(verticalRight)

        elif row in blockDividerRow:
            newRow.append(verticalLeftBlock)
            newRow.append(horizontalBlock)
            newRow.append(intersectionHorizontalBlockCell)
            newRow.append(horizontalBlock)
            newRow.append(intersectionHorizontalBlockCell)
            newRow.append(horizontalBlock)
            newRow.append(intersectionBlock)
            newRow.append(horizontalBlock)
            newRow.append(intersectionHorizontalBlockCell)
            newRow.append(horizontalBlock)
            newRow.append(intersectionHorizontalBlockCell)
            newRow.append(horizontalBlock)
            newRow.append(intersectionBlock)
            newRow.append(horizontalBlock)
            newRow.append(intersectionHorizontalBlockCell)
            newRow.append(horizontalBlock)
            newRow.append(intersectionHorizontalBlockCell)
            newRow.append(horizontalBlock)
            newRow.append(verticalRightBlock)

        elif row in numberRow:
            currentSudokuRow = sudoku[sudokuRow]
            sudokuRow += 1
            # randomList = []  # Replace with sudoku data
            # for _ in range(9):
            #     randomList.append(str(random.randint(1, 9)))
            newRow.append(verticalBlock)
            newRow.append(currentSudokuRow[0])
            newRow.append(vertical)
            newRow.append(currentSudokuRow[1])
            newRow.append(vertical)
            newRow.append(currentSudokuRow[2])
            newRow.append(verticalBlock)
            newRow.append(currentSudokuRow[3])
            newRow.append(vertical)
            newRow.append(currentSudokuRow[4])
            newRow.append(vertical)
            newRow.append(currentSudokuRow[5])
            newRow.append(verticalBlock)
            newRow.append(currentSudokuRow[6])
            newRow.append(vertical)
            newRow.append(currentSudokuRow[7])
            newRow.append(vertical)
            newRow.append(currentSudokuRow[8])
            newRow.append(verticalBlock)

        sudokuRender.append(newRow)

    index = len(sudokuRender) - 1
    with open("./out.txt", "w", encoding="utf-8") as file:
        for row in sudokuRender:
            for char in row:
                file.write(char)
            if index != 0:
                file.write("\n")
                index -= 1


if __name__ == "__main__":
    # file = input("Enter file to solve: ")
    sudokuToSolve = ReadFile("example.txt")
    if sudokuToSolve != 0:
        # zeroPositions = CheckForZero(sudokuToSolve)
        # depth = len(zeroPositions) - 1
        # print(depth + 1)
        if Solve(sudokuToSolve):
            for row in sudokuToSolve:
                row

        # RenderSudoku(solution)
    # print(sudokuToSolve)
