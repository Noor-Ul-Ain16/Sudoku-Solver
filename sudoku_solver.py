def find_next_empty(puzzle):
    #finds the next row,col on the puzzle that's not filled yet
    #return row,col tuple (or (None,None)) if there is none)
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
            
    return None,None #if no space is empty


def is_valid(puzzle,guess,row,col):
    #figures out whether the guess at [row][col] is a valid guess or not
    #returns True for a valid guess, False otherwise

    #checking the rows
    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    
    #checking the columns
    col_vals=[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #checking the cube/square
    row_start=(row//3)*3
    col_start=(col//3)*3
    
    #iterating through the cube and comparing each value with guess
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if guess == puzzle[r][c]:
                return False 
    
    #if guess is valid, return True
    return True


def find_invalid_cells(puzzle):
    invalid=set()

    for r in range(9):
        for c in range(9):
            val=puzzle[r][c]

            if val==-1:
                continue

            puzzle[r][c]=-1

            if not is_valid(puzzle,val,r,c):
                invalid.add((r,c))

            puzzle[r][c]=val

    return invalid

def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    
    row,col= find_next_empty(puzzle)
    
    if row is None:
        return True,puzzle
    
    for guess in range (1,10):

        if is_valid(puzzle,guess,row,col):

            puzzle[row][col]=guess

            solved,_ = solve_sudoku(puzzle)

            if solved:
                return True,puzzle

            puzzle[row][col]=-1

    return False,None