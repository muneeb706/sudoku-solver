# Sudoku Puzzle Solver

This project contains two types of sudoku puzzle solver. Following is the description for both types of sudoku solvers:

## 1. Basic Sudoku Solver

A python program which will read a sudoku puzzle from a file (some examples are sudoku1.txt, sudoku2.txt, etc) and generate clauses in the DIMACS format for each sudoku puzzle in the files sudokuN.cnf, where N = 1, 2, ..., 5.

Plase refer to the article (http://sat.inesc.pt/~ines/publications/aimath06.pdf) to understand the problem.

Python Program uses the propositional variables S(i,j,d) for a Sudoku puzzle, which is true iff the digit in the cell at row i and column j is d, where i, j, and d are in { 1, 2, ..., 9 }. To encode this variable into an integer in the DIMACS format, we have used following formula:

           code(i, j, d) = 100*i+10*j+d
           
As a result, the maximal variable index is 999, instead of 729. So the first line output by the program is

p cnf 999 999999

Solution of a puzzle can be figured out by looking at the output of minisat.

An executable of minisat for linux can be downloaded from here: (http://minisat.se/). You might need to run

    chmod a+x minisat.exe
    
on linux before running minisat.exe. You need to run minisat as
    
    cat sudoku1.cnf | ./minisat.exe stdin sudoku1.out

## 2. Latin Square Sudoku Solver

A Latin square over N = {0, 1, ..., n-1} is an n by n square where each row and each column of the square is a permutation of the numbers from N. Here n is said to be the order of the square. Note that a Sudoku puzzle is a special Latin square over M = {1, 2, ..., 9} with the additional condition that each of the nine 3x3 regions is also a permutation of M.

Python program uses the propositional variables S(i,j,d) for a Latin square, which is true iff the number in the cell at row i and column j is d in the square, where i, j, and d are in N. To encode this variable into an integer in the DIMACS format, please use

           code(i, j, d) = 100*i+10*j+d+1
           
Python program specifies the Latin square in propositional logic for n = 4, 5, 6, 7, 8, and 9, with the following two additional conditions: For all x, y, z, w in N:
- S(x,x,x)
- -S(x,y,z) \/ -S(y,x,w) \/ S(z,w,x)

where "-" is for negation, such that the set of clauses is satisfiable iff the Latin square with the above two conditions over N = {0, 1, ..., n-1} exists.
Python program reads an integer n and generates propositional clauses in DIMACS format for the Latin square of order N. Program saves these clauses in a file called lsquareN.cnf, where N is a number, then run minisat on lsquareN.cnf as mentioned in the description of basic sudoku solver above.

- #### Note: 
           If we regard the Latin square as the definition for the operation *, such that x*y = z iff S(x,y,z) is true, then the first formula above says x*x = x, and the second formula says (x*y)*(y*x) = x.


