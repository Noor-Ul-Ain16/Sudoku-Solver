from flask import Flask,render_template,request,url_for,redirect
import sudoku_solver

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home(puzzle = [["" for _ in range(9)] for _ in range(9)],original=None):
    return render_template("index.html",puzzle=puzzle,original=original)

@app.route("/choice",methods=["POST","GET"])
def check():
    if request.method=='POST':
        if request.form['action']=="clear-all":
            return redirect(url_for("home"))

        elif request.form['action']=="solve":

            puzzle = [[-1 for _ in range(9)] for _ in range(9)]

            for r in range(9):
                for c in range(9):
                    cell_name = f"cell-{r}-{c}"
                    value = request.form.get(cell_name)

                    if value:
                        puzzle[r][c] = int(value)
                    else:
                        puzzle[r][c] = -1

            original = [row[:] for row in puzzle]

            invalid_cells = set()

            for r in range(9):
                for c in range(9):

                    guess = original[r][c]

                    if guess == -1:
                        continue

                    puzzle[r][c] = -1

                    if not sudoku_solver.is_valid(puzzle, guess, r, c):
                        invalid_cells.add((r,c))

                    puzzle[r][c] = guess

            if invalid_cells:
                return render_template(
                    "index.html",
                    puzzle=original,
                    original=original,
                    invalid_cells=invalid_cells,
                    message="Invalid puzzle: duplicate numbers"
                )

            result, solved_puzzle = sudoku_solver.solve_sudoku(puzzle)

            if result:
                return render_template(
                    "index.html",
                    original=original,
                    puzzle=solved_puzzle
                )
            else:
                return render_template(
                    "index.html",
                    original=original,
                    puzzle=original,
                    message="No solution exists"
                )
if __name__ == "__main__":
    app.run(debug=True)