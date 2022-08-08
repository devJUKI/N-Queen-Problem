class Board:
    size = 0
    array = []
    queenCombinationCount = 0
    
    def __init__(self, size):
        self.size = size
        self.array = [["."] * size for _ in range(size)]

    def addBlockedTile(self, x, y):
        self.array[x][y] = "*"

    def isQueenOnBlockedTile(self, queenArray):
        for i in range(0, len(queenArray)):
            if self.array[queenArray[i]][i] == "*":
                return True
        return False

    def isBoardValid(self, queenArray):
        # Is queen on blocked tile
        if self.isQueenOnBlockedTile(queenArray) == True:
            return False
        
        for i in range(0, len(queenArray)):
            for j in range(0, len(queenArray)):
                # If it is the same queen - skip
                if i == j:
                    continue

                # Are queens in the same row
                if queenArray[i] == queenArray[j]:
                    return False

                # Are queens diagonal to each other
                if queenArray[i] + i == queenArray[j] + j or\
                   queenArray[i] - i == queenArray[j] - j:
                    return False
        return True

    def checkQueenCombinations(self, numbers, index):
        if index >= self.size:
            return
        else:
            for i in reversed(range(0, self.size)):
                newNumbers = numbers.copy()
                newNumbers[index] = newNumbers[index] + i

                if self.isBoardValid(newNumbers[:index + 1]):
                    self.checkQueenCombinations(newNumbers, index + 1)

                if index == self.size - 1 and self.isBoardValid(newNumbers):
                    self.queenCombinationCount = self.queenCombinationCount + 1
        

def main():
    caseNumber = 1
    
    # Reading data from file
    file = open("input.txt", "r")
    while True:
        i = j = 0
        size = int(file.readline())
        if size == 0:
            break
        board = Board(size)
        for p in range(0, size):
            i = i + 1
            j = 0
            for character in file.readline():
                j = j + 1
                if character == "*":
                    board.addBlockedTile(i - 1, j - 1)

        # Calculating the result after reading each board's data            
        board.checkQueenCombinations([0] * board.size, 0)
        print("Case " + str(caseNumber) + ": " + str(board.queenCombinationCount))
        caseNumber = caseNumber + 1

    print("Program finished")

if __name__ == "__main__":
    main()
