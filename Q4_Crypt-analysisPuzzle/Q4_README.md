## Crypt-Arithmetic Puzzle using CSP

## Overview
This project implements a crypt-arithmetic puzzle solver using the Constraint Satisfaction Problem (CSP) approach. The goal is to assign digits to letters such that the arithmetic equation formed by words is valid and satisfies all constraints.

## Problem Description
Each letter in the given words represents a unique digit from 0 to 9. The same letter must always represent the same digit, and different letters must represent different digits.

The objective is to solve equations of the form:

WORD1 + WORD2 = RESULT

Example:
TWO + TWO = FOUR

## CSP Formulation
Variables: All unique letters present in the words  
Domain: Digits from 0 to 9  
Constraints:
- No two letters can have the same digit  
- Leading letters cannot be assigned zero  
- The arithmetic equation must hold true  

## State Space
The total possible assignments are permutations of digits for the given letters. The search space is reduced using constraint checking and forward checking.

## Techniques Used
Backtracking Search  
Forward Checking  
Constraint Propagation  
Variable Selection Strategy  

## Algorithm Workflow
1. Extract unique letters from input words  
2. Initialize domains with digits 0–9  
3. Select an unassigned variable  
4. Assign a digit from its domain  
5. Check partial constraints  
6. Apply forward checking to reduce domains  
7. Recursively continue assignment  
8. Backtrack if any constraint is violated  
9. Return solution when all variables are assigned  

## Implementation Details
Language: Python 3  
Paradigm: Constraint Satisfaction Problem  
Technique: Recursive backtracking with domain pruning  

## Input Format
User provides three words:
- First operand  
- Second operand  
- Result word  

All inputs are case-insensitive and converted to uppercase.

## Output Format
- Displays numeric values of each word  
- Shows arithmetic verification  
- Prints mapping of letters to digits  

## How to Run
python3 crypt.py  

## Features
- Works for different crypt-arithmetic puzzles  
- Dynamic input support  
- Efficient search using forward checking  
- Avoids invalid assignments early  
- Menu-driven interaction  

## Menu Options
1. Solve current puzzle  
2. Enter new words  
3. Display current puzzle  
4. Exit program  

## Sample Execution
Input:
TWO  
TWO  
FOUR  

Output:
TWO = 734  
+ TWO = 734  
  ----  
FOUR = 1468  

734 + 734 = 1468  

Mapping:
F = 1  
O = 4  
U = 6  
R = 8  
T = 7  
W = 3  

## Advantages
- Reduces brute-force complexity  
- Ensures correctness using constraints  
- Flexible for different puzzles  
- Easy to understand and extend  

## Limitations
- Performance may decrease with very large puzzles  
- Depends on effectiveness of constraint pruning  
- No graphical interface  

## Applications
Artificial Intelligence  
Puzzle solving systems  
Constraint-based systems  
Educational tools for CSP  

## Future Enhancements
- Add heuristics like MRV or Degree Heuristic  
- Implement AC-3 for stronger consistency  
- Add graphical visualization  
- Improve performance for larger puzzles  

## Conclusion
This project demonstrates how CSP techniques such as backtracking and forward checking can efficiently solve crypt-arithmetic puzzles by systematically exploring valid assignments while pruning invalid possibilities.
