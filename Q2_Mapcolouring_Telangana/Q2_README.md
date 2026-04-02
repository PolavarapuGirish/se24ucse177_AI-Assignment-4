## Map Coloring Problem using CSP (Telangana - 33 Districts)

## Overview
This project solves the Map Coloring Problem for the 33 districts of Telangana using Constraint Satisfaction Problem (CSP).

The goal is to assign colors to districts such that no two adjacent districts share the same color.

## CSP Components
Variables: 33 districts of Telangana  
Domain: Set of colors (user-defined or default)  
Constraints: Adjacent districts must not have the same color  

## Techniques Used
Backtracking  
AC-3 (Arc Consistency Algorithm)  
Forward Checking  
MRV (Minimum Remaining Values Heuristic)  

## Algorithm Used
1. Initialize domains for all districts  
2. Apply AC-3 to reduce domain values  
3. Select district using MRV heuristic  
4. Assign a valid color  
5. Apply forward checking to reduce future conflicts  
6. Continue recursively  
7. Backtrack if any constraint fails  

## Implementation Details
Language: Python 3  
Input: Adjacency list from JSON file  
Output: Valid color assignment  

## How to Run
python3 Q2_Code.py  

## Features
Efficient constraint solving  
Reduces unnecessary computations  
Supports custom color input  
Interactive menu-driven program  

## Options Available
1. Solve with current colors  
2. Set custom colors  
3. Display all districts  
4. Display current colors  
5. Exit  

## Sample Output
District                          Colour  
-------------------------------- -----  
Adilabad                          Red  
Nirmal                            Green  
...  

## Applications
Scheduling  
Resource allocation  
Map design  
Timetabling  

## Conclusion
The problem is efficiently solved using CSP with advanced techniques like AC-3, MRV, and forward checking, making it scalable for larger datasets like Telangana districts.
