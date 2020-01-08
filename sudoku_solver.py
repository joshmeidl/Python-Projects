# Josh Meidl
# Sudoku Solver, 12/26/19

import sys

sys.setrecursionlimit(5000)

def solve(boardList, startList):
    solvedList = solveHelper(0, boardList, startList)
    if len(solvedList) == 1:
        print("No solution")
    else:
        print("=========SOLUTION=========")
        printBoard(solvedList)


def solveHelper(index, boardList, startList):
    print(index)
    if index < 0: # no solution
        return []
    elif index > 80: # completed puzzle
        return boardList
    # continue to solve
    if startList[index]:
        return solveHelper(index+1, boardList, startList)
    boardList[index] += 1
    while (not validState(index, boardList)) and (boardList[index] < 10): # try all 1-10
        boardList[index] += 1
    if boardList[index] < 10:
        return solveHelper(index+1, boardList, startList)
    else: #back track
        boardList[index] = 0
        return solveHelper(index-1, boardList, startList)

def validState(index, boardList):
    column = index % 9 # 0-8
    row = (index - column)//9 #0-8
    for i in range(9): #check row and column rule
        rowcheck = row*9 + i
        columncheck = 9*i + column
        if boardList[rowcheck] == boardList[index] and rowcheck != index:
            return False
        if boardList[columncheck] == boardList[index] and columncheck != index:
            return False
    #check square
    if row < 3:
        if column < 3:
            check = [0,1,2,9,10,11,18,19,20]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
        elif column < 6:
            check = [3, 4, 5, 12, 13, 14, 21, 22, 23]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
        elif column < 9:
            check = [6, 7, 8, 15, 16, 17, 24, 25, 26]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
    elif row < 6:
        if column < 3:
            check = [27,28,29,36,37,38,45,46,47]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
        elif column < 6:
            check = [30,31,32,39,40,41,48,49,50]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
        elif column < 9:
            check = [33,34,35,42,43,44,51,52,53]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
    elif row < 9:
        if column < 3:
            check = [54,55,56,63,64,65,72,73,74]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
        elif column < 6:
            check = [57,58,59,66,67,68,75,76,77]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
        elif column < 9:
            check = [60,61,62,69,70,71,78,79,80]
            for each in check:
                if boardList[each] == boardList[index] and index != each:
                    return False
    return True

def printBoard(boardList):
    for i in range(81):
        # format
        if i % 9 == 0:
            print()
            print("-----------------------------------------")
        if i % 27 == 0 and i != 0:
            print("-----------------------------------------")
        if i % 3 == 0 and i % 9 != 0:
            print("||", end="")
        # print number
        if(boardList[i] != 0):
            print("|",boardList[i],"", end="")
        else:
            print("|   ", end="")
        if i % 9 == 8:
            print("|", end="")
    print()
    print("-----------------------------------------")


def main():
    print("Sudoku Solver")
    print("Please input the puzzle values starting from the top left corner and filling out each row before the next")
    print("Note: if space is empty, please input 0")
    # initialize board
    boardList = []
    startList = []
    for i in range(81):
        boardList.append(0) # 0 representing empty spot
        startList.append(False)
    correctInput = False
    while not correctInput: # fill board with user input
        for i in range(1,82):
            validInput = False
            while validInput == False:
                print("space", i, end=":")
                num = input("")
                if not num.isnumeric():
                    print("Error: must input integer")
                elif int(num) < 0 or int(num) > 9:
                    print("Error: input must be between 0-9")
                else:
                    validInput = True
            boardList[i-1] = int(num)
            if int(num) != 0:
                startList[i-1] = True
            if (i-1) % 9 == 8: # check to see if correct so far
                printBoard(boardList)
                correct = ""
                while correct != "y" and correct != "n":
                    correct = input("Is this correct so far? (y/n)")
                    correct = correct.lower()
                if correct == "n": # error in input
                    for j in range(i-1): # clear board
                        boardList[j] = 0
                        startList[j] = False
                    correctInput = False
                    print("Resetting Board")
                    break
                elif correct == "y" and i == 81:
                    correctInput = True
    solve(boardList, startList)

main()
