## Crypt-Arithmetic Puzzle using CSP

## Overview
This project implements a crypt-arithmetic puzzle solver using the Constraint Satisfaction Problem (CSP) approach. The goal is to assign digits to letters such that the arithmetic equation formed by words is valid.

## Problem Description
Each letter represents a unique digit (0–9). The objective is to find a mapping such that:

WORD1 + WORD2 = RESULT

Example:
TWO + TWO = FOUR

## CSP Components
Variables: Unique letters in the given words  
Domain: Digits from 0 to 9  
Constraints:  
- Each letter must have a unique digit  
- Leading letters cannot be zero  
- Arithmetic equation must be satisfied  

## Techniques Used
Backtracking  
Forward Checking  
Constraint Propagation  

## Algorithm Used
1. Extract all unique letters  
2. Assign domain (0–9) to each letter  
3. Select an unassigned variable  
4. Try assigning a digit  
5. Check constraints  
6. Apply forward checking  
7. Continue recursively  
8. Backtrack if constraints fail  

## Implementation Details
Language: Python 3  
Approach: CSP with recursive backtracking  

## How to Run
python3 crypt.py  

## Features
Supports any valid crypt-arithmetic puzzle  
Ensures all constraints are satisfied  
Interactive menu-driven program  
Efficient pruning using forward checking  

## Options Available
1. Solve puzzle  
2. Enter new words  
3. Show current puzzle  
4. Exit  

## Sample Input
TWO  
TWO  
FOUR  

## Sample Output
TWO = 734  
+ TWO = 734  
  ----  
FOUR = 1468  

734 + 734 = 1468  

Values:  
F = 1  
O = 4  
U = 6  
R = 8  
T = 7  
W = 3  

## Applications
Puzzle solving  
Artificial Intelligence problems  
Constraint solving systems  
Logic-based problem solving  

## Conclusion
This project demonstrates how CSP techniques like backtracking and forward checking can be applied to solve crypt-arithmetic puzzles efficiently.
