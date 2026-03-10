# Sudoku Solver 
A web-based Sudoku Solver built with Python (Flask) and HTML/CSS. Enter any Sudoku puzzle, and it will automatically solve it using a backtracking algorithm.

I learned how to implement the backtracking Sudoku solver from a tutorial by Kylie Ying. The web interface, validation logic, and Flask integration were implemented by me.


## Features

- Interactive 9×9 Sudoku grid
- Accepts user input directly in the browser
- Backtracking algorithm solves the puzzle
- Detects invalid puzzles
- Highlights incorrect cells in red
- Displays "No solution exists" if unsolvable
- Differentiates:
  - User entered cells (green)
  - Solver generated cells (black)


## How It Works

1. Enter the puzzle into the grid (leave empty cells blank).  
2. Click **Solve**.  
3. The solver will:
   - Check for invalid numbers
   - Solve the puzzle if possible
   - Display the solution on the same page

If there are invalid numbers, they will be highlighted, and a message will appear. If the puzzle has no solution, a message will be displayed.


## Algorithm Used

The solver uses **backtracking**, a recursive algorithm for constraint satisfaction problems:

1. Find the next empty cell.  
2. Try numbers **1–9**.  
3. Check if the number is valid:
   - Row constraint  
   - Column constraint  
   - 3×3 box constraint  
4. If valid, place the number and recurse.  
5. If a dead-end occurs, backtrack and try the next number.  


## Learning Outcomes

This project helped me:

- Understand backtracking and recursion  
- Work with 2D arrays / matrices  
- Build a full-stack web application (Python + frontend)  
- Handle input validation and user feedback  
- Learn to integrate algorithms into a web app  

## Possible Improvements

- Step-by-step solving visualization  
- Sudoku puzzle generator  
- Difficulty levels  
- Animated solving process  
- Keyboard navigation for grid input  

## Acknowledgements

- **Tutorial:** Kylie Ying   
-
