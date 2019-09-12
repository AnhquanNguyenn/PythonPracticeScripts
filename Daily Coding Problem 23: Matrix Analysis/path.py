def path(matrix, start, end):
    # our starting positions and our x and y traversal points
    moves = [start]
    x, y = start
    
    # Always checking our moves to see if we reached the end, and calculating
    # our position in regards to start and end position
    while True:
        if (x, y) == end:
            return len(moves) - 1
    
        # to move up you need the top value to be false, it needs to be within the bounds of the matrix, and not in our current moves set taken
        moveUp = (x - 1) >= 0 and not matrix[x - 1][y] and (x - 1, y) not in moves 
        
        # to move down you need to be in the bounds of the matrix, the value needs to be false, and is not in the current moves set
        moveDown = (x + 1) < len(matrix) and not matrix[x + 1][y] and (x + 1, y) not in moves
        
        # to move left you need to be in the bounds of the matrix, the value needs to be False, and is not in the current moves set 
        moveLeft = (y - 1) >= 0 and not matrix[x][y - 1] and (x, y - 1) not in moves 
        
        # to move right you need to be in the bounds of the matrix, the value needs to be False, and is not in the current moves set
        moveRight = (y + 1) < len(matrix[x]) and not matrix[x][y + 1] and (x, y + 1) not in moves
        
        # Handling our x coordinate, must be inside our bounds
        if x >= end[0]:
            # handling our y coordinate, must be inside our bounds
            # must not be able to move in the opposite direction, and able to move in that specific direction
            if y >= end[1]:
                if moveUp and (x > end[0] or not moveDown):
                    x = x - 1
                    moves.append((x, y))
                elif moveLeft and (y > end[1] or not moveRight):
                    y = y - 1
                    moves.append((x, y))
                elif moveRight and (y < end[1] or not moveLeft):
                    y = y + 1
                    moves.append((x, y)) 
                elif moveDown and (x < end[0] or not moveUp):
                    x = x + 1
                    moves.append((x, y))
            else:
                if moveUp and (x > end[0] or not moveDown):
                    x = x - 1
                    moves.append((x, y))
                elif moveRight and (y < end[1] or not moveLeft):
                    y = y + 1
                    moves.append((x, y))
                elif moveLeft and (y > end[1] or not moveRight):
                    y = y - 1
                    moves.append((x, y))
                elif moveDown and (x < end[0] or not moveUp):
                    x = x + 1
                    moves.append((x, y))
        else:
            if y >= end[1]:
                if moveDown and (x < end[0] or not moveUp):
                    x = x + 1
                    moves.append((x, y))
                elif moveLeft and (y > end[1] or not moveRight):
                    y = y - 1
                    moves.append((x, y))
                elif moveRight and (y < end[1] or not moveLeft):
                    y = y + 1
                    moves.append((x, y))
                elif moveUp and (x > end[0] or not moveDown):
                    x = x - 1
                    moves.append((x, y)) 
            else:
                if moveDown and (x < end[0] or not moveUp):
                    x = x + 1
                    moves.append((x, y))
                elif moveRight and (y < end[1] or not moveLeft):
                    y = y + 1
                    moves.append((x, y))
                elif moveLeft and (y > end[1] or not moveRight):
                    y = y - 1
                    moves.append((x, y))
                elif moveUp and (x > end[0] or not moveDown):
                    x = x - 1
                    moves.append((x, y))
                    
start = (3, 0) # Start postion: Bottom Left
end = (0, 0) # End Position: Top Left
matrix = [
    [False, False,  False,  False],
    [True,  True,   False,  True],
    [False, False,  False,  False],
    [False, False,  False,  False]
]

print(path(matrix, start, end))
start = (3, 3)
end = (0, 3)
print(path(matrix, start, end))
matrix = [
    [False, False,  False,  False, False],
    [True,  True,   True,  False, False],
    [False, False,  False,  False, True],
    [False, True,  True,  True, False],
    [False, False,  False,  False, False]
]
start = (3, 4)
end = (0, 0)
print(path(matrix, start, end))
