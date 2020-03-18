# Sudoku Puzzle Solver
A python program which will read a sudoku puzzle from a file (some examples are sudoku1.txt, sudoku2.txt, etc) and generate clauses in the DIMACS format for each sudoku puzzle in the files sudokuN.cnf, where N = 1, 2, ..., 5.

Plase refer to the article (http://sat.inesc.pt/~ines/publications/aimath06.pdf) to understand the problem.

We will use the propositional variables S(i,j,d) for a Sudoku puzzle, which is true iff the digit in the cell at row i and column j is d, where i, j, and d are in { 1, 2, ..., 9 }. To encode this variable into an integer in the DIMACS format, we have used following formula:

           code(i, j, d) = 100*i+10*j+d
           
As a result, the maximal variable index is 999, instead of 729. So the first line output by the program is

p cnf 999 999999

Solution of a puzzle can be figured out by looking at the output of minisat.

An executable of minisat for linux can be downloaded from here: (http://minisat.se/). You might need to run

    chmod a+x minisat.exe
    
on linux before running minisat.exe. You need to run minisat as
    
    cat sudoku1.cnf | ./minisat.exe stdin sudoku1.out
