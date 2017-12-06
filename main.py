#Program that solves sodoku puzzle
#The puzzle in puzzle.txt is taken from here: http://elmo.sbs.arizona.edu/sandiway/sudoku/examples.html



#Create function that goes through the file specified in the parameter
#and makes a list containing each row in a list
def createBoardList(puzzle):
    #Opens up the file in the parameter
    sodokuFile = open(puzzle)
    solutionFile = open("solution.txt", "w")
    for line in sodokuFile:
        solutionFile.write(line)
    solutionFile = open("solution.txt")
    sodokuBoard = solutionFile.readlines()
    #This will be the complete list that will later be returned
    boardArray = []
    #Goes through every line in the file, splits it up into multiple lists and makes
    #each value an integer
    for lists in sodokuBoard:
        lists = lists.strip().split()
        rowList = []
        for number in lists:
            number = int(number)
            rowList.append(number)
        boardArray.append(rowList)

    return boardArray

#Function that returns all the numbers not in the given squares row
def notInRow(x, y, boardList):
    #square = boardList[y][x]
    numbersInRow = set([])
    numbersNotInRow = set([])
    for lists in boardList:
        numbersInRow.add(lists[x])
    for number in range(1,10):
        if number not in numbersInRow:
            numbersNotInRow.add(number)
    return numbersNotInRow

#Function that returns all the numbers not in the given squares column
def notInColumn(x, y, boardList):
    #square = boardList[y][x]
    numbersInColumn = set([])
    numbersNotInColumn = set([])
    for numbers in boardList[y]:
        numbersInColumn.add(numbers)
    for number in range(1,10):
        if number not in numbersInColumn:
            numbersNotInColumn.add(number)
    return numbersNotInColumn


#Function that returns all the numbers not in a given squares cubicle
def notInCubicle(x, y, boardList):
    cubicleList = []
    numbersInCubicle = set([])
    numbersNotInCubicle = set([])
    for r in range(3):
        for c in range(3):
            cubicle = []
            for i in range(3):
                for j in range(3):
                    cubicle.append(boardList[3*r + i][3*c + j])
            cubicleList.append(cubicle)

    if x <= 3 and y <= 3:
        x = 0
        y = 0

    elif 3 < x <= 5 and y <= 3:
        x = 1
        y = 0

    elif x > 5 and y <= 3:
        x = 2
        y = 0

    elif x <= 3 and 3 < y <= 5:
        x = 3
        y = 0

    elif 3 < x <= 5 and 3 < y <= 5:
        x = 4
        y = 0

    elif x > 5 and 3 < y <= 5:
        x = 5
        y = 0

    elif x <= 3 and y > 5:
        x = 6
        y = 0

    elif 3 < x <= 5 and y > 5:
        x = 7
        y = 0

    elif x > 5 and y > 5:
        x = 8
        y = 0

    for numbers in cubicleList[x]:
        numbersInCubicle.add(numbers)
    for number in range(1,10):
        if number not in numbersInCubicle:
            numbersNotInCubicle.add(number)
    return numbersNotInCubicle


def main():
    boardList = createBoardList("puzzle.txt")
    print(boardList)

    for y in range(9):
        for x in range(9):
            if boardList[y][x] == 0:
                row = notInRow(x, y, boardList)
                column = notInColumn(x, y, boardList)
                cubicle = notInCubicle(x, y, boardList)
                answer = []
                for number in row:
                    if number in column and number in cubicle:
                        answer.append(number)
                if len(answer) == 1:
                    boardList[y][x] = answer[0]
            else:
                pass

    print("\n")
    print(boardList)


main()
