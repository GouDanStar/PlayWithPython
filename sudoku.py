NumSet={1,2,3,4,5,6,7,8,9}

def inputClue():
    global keyboard
    print('Input clue x,y coordinate and value, end with -1 -1 -1')
    x, y, val = input('').split()
    x = int(x) - 1
    y = int(y) - 1
    val = int(val)
    while x>=0:
        keyboard[x][y]=val
        x, y, val = input('').split()
        x=int(x)-1
        y=int(y)-1
        val=int(val)

def getCandicates(keyboard,indexX,indexY):
    global NumSet
    setRow = set(keyboard[indexX])
    setRow.remove(0)
    setCol = set([keyboard[i][indexY] for i in range(9)])
    setCol.remove(0)

    rectX=indexX//3
    rectY=indexY//3
    setRect=set([keyboard[x][y] for x in range(3*rectX,3*rectX+3) for y in range(3*rectY,3*rectY+3)])
    # setRect=[]
    # for x in range(3*rectX,3*rectX+3):
    #     for y in range(3*rectY,3*rectY+3):
    #         setRect.append(keyboard[x][y])
    # setRect=set(setRect)
    setRect.remove(0)
    setCandicate = NumSet.difference(setRow.union(setCol.union(setRect)))
    return setCandicate

def sudoku(keyboard,indexX,indexY):
    # print('X:%d,Y:%d'%(indexX,indexY))
    state=True
    if keyboard[indexX][indexY]!=0:
        if indexX==8 and indexY==8:
            return True
        elif indexY<8:
            state=sudoku(keyboard,indexX,indexY+1)
        else:
            state=sudoku(keyboard,indexX+1,0)
        return state
    else:
        setCandicate=getCandicates(keyboard,indexX,indexY)
        if len(setCandicate)==0:
            return False
        elif indexX==8 and indexY==8:
            val = setCandicate.pop()
            keyboard[indexX][indexY] = val
            return True
        else:
            while len(setCandicate):
                val=setCandicate.pop()
                keyboard[indexX][indexY]=val
                if indexY < 8:
                    state=sudoku(keyboard, indexX, indexY + 1)
                else:
                    state=sudoku(keyboard, indexX + 1, 0)
                if state:
                    return True
            keyboard[indexX][indexY]=0
            return False

keyboard = [[0 for y in range(9)] for x in range(9)]
inputClue()
sudoku(keyboard,0,0)
print(keyboard)