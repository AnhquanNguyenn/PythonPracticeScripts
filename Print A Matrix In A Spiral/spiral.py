def printSpiral(matrix, rows, columns):
    startingRowIndex = 0
    endingRowIndex = rows
    startingColumnIndex = 0
    endingColumnIndex = columns
    
    while startingRowIndex < endingRowIndex and startingColumnIndex < endingColumnIndex:
        # printing the first row
        for i in range(startingColumnIndex, endingColumnIndex):
            print(matrix[startingRowIndex][i], end=" ")
            
        startingRowIndex += 1
        
        # printing the last column
        for i in range(startingRowIndex, endingRowIndex):
            print(matrix[i][endingColumnIndex - 1], end=" ")
            
        endingColumnIndex -= 1
        
        # printing the last row
        if (startingRowIndex < endingRowIndex):
            for i in range(endingColumnIndex - 1, startingColumnIndex - 1, -1):
                print(matrix[endingRowIndex - 1][i], end=" ")
                
        endingRowIndex -= 1
        
        # printing whatever is left of the first column
        if (startingColumnIndex < endingColumnIndex):
            for i in range(endingRowIndex - 1, startingRowIndex - 1, -1):
                print(matrix[i][startingColumnIndex], end=" ")
                
        startingColumnIndex += 1 
    
    
matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]
rows = 4
columns = 5
printSpiral(matrix, rows, columns)
print("\n")

