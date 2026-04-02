## Sudoku Solver using CSP

## Overview
This project implements a Sudoku solver using the Constraint Satisfaction Problem (CSP) approach. The objective is to fill a 9x9 Sudoku grid such that all constraints are satisfied.

## Problem Description
A Sudoku puzzle consists of a 9x9 grid divided into:
- 9 rows
- 9 columns
- 9 subgrids (3x3 boxes)

The goal is to assign numbers from 1 to 9 to each cell such that:
- Each row contains unique numbers
- Each column contains unique numbers
- Each 3x3 box contains unique numbers

## CSP Components
Variables: Each cell in the grid (81 variables)  
Domain: Values from 1 to 9  
Constraints: No repetition in row, column, or 3x3 box  

## Techniques Used
Backtracking  
AC-3 (Arc Consistency Algorithm)  
Forward Checking  
MRV (Minimum Remaining Values Heuristic)  

## Algorithm Used
1. Initialize domains for all cells  
2. Apply AC-3 algorithm to reduce domains  
3. Select unassigned variable using MRV  
4. Assign a valid value  
5. Apply forward checking  
6. Continue recursively  
7. Backtrack if constraints fail  

## Implementation Details
Language: Python 3  
Approach: CSP with optimization techniques  

## How to Run
python3 Q3_Code.py  

## Features
Efficient solving using constraint propagation  
Reduces search space using AC-3  
Uses MRV for better variable selection  
Supports custom input  
Menu-driven interface  

## Options Available
1. Load default puzzle  
2. Enter custom puzzle  
3. Solve puzzle  
4. Show current puzzle  
5. Exit  

## Sample Input
003020600  
900305001  
001806400  
008102900  
700000008  
006708200  
002609500  
800203009  
005010300  

## Sample Output
Solution grid with all cells filled correctly following Sudoku rules  

## Applications
Puzzle solving  
Game development  
Constraint solving problems  
Artificial Intelligence research  

## Conclusion
This project demonstrates how CSP techniques like AC-3, MRV, forward checking, and backtracking can efficiently solve Sudoku puzzles.
