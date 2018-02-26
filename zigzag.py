import numpy as np
someSquareMatrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                    [9,10,11,12,13,14,15,16],
                    [17,18,19,20,21,22,23,24],
                    [25,26,27,28,29,30,31,32],
                    [33,34,35,36,37,38,39,40],
                    [41,42,43,44,45,46,47,48],
                    [49,50,51,52,53,54,55,56],
                    [57,58,59,60,61,62,63,64]]

print("starting matrix")
print(np.matrix(someSquareMatrix ))



def zigzag(matrix):
    dim = len(matrix)
    goDown = True
    totalIndexesSum = 0
    nElementsInDiagonal = 1
    biggestDiagonalReached = False
    wae = True
    res = []
    x = 0
    y = 0
    res.append(matrix[x][y])

    for loopInSidewaysDiagonal in range(0, dim * 2 - 2):

        if not biggestDiagonalReached:
            nElementsInDiagonal += 1
            if nElementsInDiagonal == dim:
                biggestDiagonalReached = True
        else:
            nElementsInDiagonal -= 1
        totalIndexesSum += 1
        if goDown:
            y += 1
            res.append(matrix[x][y])
            if nElementsInDiagonal != dim:
                goDown = False
        else:
            x += 1
            res.append(matrix[x][y])
            goDown = True
        elementsFound = 1
        while(elementsFound < nElementsInDiagonal):
            if wae:
                y -= 1
                x += 1
                res.append(matrix[x][y])
            else:
                y += 1
                x -= 1
                res.append(matrix[x][y])
            elementsFound += 1
        wae = not wae

    print("answer: " + str(res))
    return res




zigzag(someSquareMatrix)