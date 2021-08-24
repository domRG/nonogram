import numpy as np
import itertools


def improveGuess(clue, length, guess):
    # make 'blocks' for permutations
    clueBlocks = [[2] * clue[0]]
    blockLengthInternal = clue[0]
    for idx, elem in enumerate(clue):
        if idx != 0:
            clueBlocks.append([1] + [2] * elem)
            blockLengthInternal += 1 + elem

    perms = []
    for permutation in semiOrderedCombination(clueBlocks, len(clueBlocks) + length - blockLengthInternal, [1]):
        perms.append(list(itertools.chain.from_iterable(permutation)))
    # printNono(perms)

    rmIdx = []
    for idx, perm in enumerate(perms):
        withGuess = [i | k for i, k in zip(guess, perm)]
        if any(t == 3 for t in withGuess):
            rmIdx.append(idx)

    for idx in sorted(rmIdx, reverse=True):
        perms.pop(idx)

    newGuess = list(guess)
    for perm in perms:
        newGuess = [i | k for i, k in zip(newGuess, perm)]

    newGuess = [i % 3 for i in newGuess]

    if newGuess == guess:
        change = 0
    else:
        change = 1

    return newGuess, change


def semiOrderedCombination(orderedList, finalLength, fillItem):
    # semiOrderedCombination([[2,2,2,2],[1,2,2]], 3, [1])
    empty = [fillItem] * finalLength
    # print(empty)
    result = []

    for comb in itertools.combinations(range(finalLength), len(orderedList)):
        # print(comb)
        perm = list(empty)
        for idx, elem in zip(comb, orderedList):
            perm[idx] = elem
        result.append(perm)

    return result


def printNono(arr):
    if isinstance(arr, np.ndarray):
        mat = arr
    else:
        mat = np.array(arr)

    try:
        rows, cols = mat.shape
    except:
        rows = 1
        cols = mat.shape[0]

    print(''.join(list(['0-'] + ['---'] * cols + ['-0'])))
    for row in range(rows):
        edgeChar = " "
        if (row + 1) % 5 == 0:
            edgeChar = "_"
        print(f"|{edgeChar}", end='')
        for col in range(cols):
            try:
                elem = mat[row][col]
            except:
                elem = mat[col]

            if elem == 2:
                sym = '\u2588\u2588 '
            if elem == 1:
                sym = '   '
            if elem == 0:
                sym = '\u2592\u2592 '
            print(sym, end='')
        print(f"{edgeChar}|")
    print(''.join(list(['0-'] + ['---'] * cols + ['-0'])))


def makeGrid(n, m):
    grid = np.array([[0] * m] * n)
    return grid


def getClues(rowCol):
    clues = []
    print(f"Enter clues for {rowCol}s:")
    while True:
        line = input()
        if line:
            clues.append(list(map(int, line.split(','))))
        else:
            break
    return clues


if __name__ == "__main__":
    rowClues = getClues("row")
    colClues = getClues("col")
    grid = makeGrid(len(rowClues), len(colClues))
    colLength, rowLength = grid.shape

    printNono(grid)

    iterChange = 0
    breakFlag = 0

    while True:
        for row in range(colLength):
            clue = rowClues[row]
            grid[row, :], change = improveGuess(clue, rowLength, list(grid[row, :]))
            iterChange |= change

        if iterChange != 0:
            printNono(grid)

        for col in range(rowLength):
            clue = colClues[col]
            grid[:, col], change = improveGuess(clue, colLength, list(grid[:, col]))
            iterChange |= change

        if iterChange != 0:
            printNono(grid)

        if iterChange == 0:
            breakFlag += 1
        else:
            breakFlag = 0
            iterChange = 0

        if breakFlag >= 3:
            # requires 3 consecutive passes with no change (just to be safe!)
            break

    printNono(grid)