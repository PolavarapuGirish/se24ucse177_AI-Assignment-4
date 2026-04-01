## Map Coloring Problem using CSP (Australia)

## Overview
The Map Coloring Problem is a classic example of a Constraint Satisfaction Problem (CSP) in Artificial Intelligence. The objective is to assign colors to regions on a map such that no two adjacent regions share the same color.

This project solves the map coloring problem for the seven principal states and territories of Australia using a backtracking-based CSP approach.

## Regions Considered
WA (Western Australia)
NT (Northern Territory)
Q (Queensland)
SA (South Australia)
NSW (New South Wales)
V (Victoria)
T (Tasmania)

## Domain (Available Colors)
Red
Green
Blue

## Constraints (Adjacency Rules)
WA -> NT, SA  
NT -> WA, SA, Q  
SA -> WA, NT, Q, NSW, V  
Q  -> NT, SA, NSW  
NSW -> Q, SA, V  
V -> SA, NSW  
T -> None  

## CSP Components
Variables: WA, NT, Q, SA, NSW, V, T  
Domain: Red, Green, Blue  
Constraints: Neighboring regions must have different colors  

## Algorithm Used
1. Select an unassigned region  
2. Assign a color  
3. Check constraints  
4. Continue if valid  
5. Backtrack if invalid  

## Implementation Details
Language: Python 3  
Technique: Backtracking  

## How to Run
nano map_coloring.py  
python3 map_coloring.py  

## Sample Output
WA Red  
NT Green  
Q Red  
SA Blue  
NSW Green  
V Red  
T Red  

## Features
Simple implementation  
Beginner-friendly  
Uses backtracking  

## Possible Improvements
MRV heuristic  
Forward Checking  
AC-3  
Visualization  

## Applications
Scheduling  
Resource allocation  
Timetabling  
Sudoku  

## Conclusion
The problem is solved using CSP and backtracking ensuring all constraints are satisfied.
