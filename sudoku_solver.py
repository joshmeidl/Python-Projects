# Josh Meidl
# Sudoku Solver

def validState(index, boardList):
    
    

def solve(boardList):
    print("")

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
    for i in range(81):
        boardList.append(0) # 0 representing empty spot
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
            if i-1 % 9 == 8: # check to see if correct so far
                printBoard(boardList)
                correct = ""
                while correct != "y" and correct != "n":
                    correct = input("Is this correct so far? (y/n)")
                    correct = correct.lower()
                if correct == "n": # error in input
                    for j in range(i-1): # clear board
                        boardList[j] = 0
                    correctInput = False
                    print("Resetting Board")
                    break
                else:
                    if i == 81:
                        correctInput = True
    solvedList = solve(boardList)
    printBoard(solvedList)







main() 
