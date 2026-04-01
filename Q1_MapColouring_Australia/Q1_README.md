Map Coloring Problem using CSP (Australia)

Overview

The Map Coloring Problem is a classic example of a Constraint Satisfaction Problem (CSP) in Artificial Intelligence. The objective is to assign colors to regions on a map such that no two adjacent regions share the same color.

This project solves the map coloring problem for the seven principal states and territories of Australia using a backtracking-based CSP approach.

Regions Considered
	•	WA (Western Australia)
	•	NT (Northern Territory)
	•	Q (Queensland)
	•	SA (South Australia)
	•	NSW (New South Wales)
	•	V (Victoria)
	•	T (Tasmania)

Domain (Available Colors)

Each region can be assigned one of the following colors:
	•	Red
	•	Green
	•	Blue

Constraints (Adjacency Rules)

No two neighboring regions can have the same color.

Adjacency relationships:
	•	WA → NT, SA
	•	NT → WA, SA, Q
	•	SA → WA, NT, Q, NSW, V
	•	Q → NT, SA, NSW
	•	NSW → Q, SA, V
	•	V → SA, NSW
	•	T → None

CSP Components
	•	Variables: WA, NT, Q, SA, NSW, V, T
	•	Domain: {Red, Green, Blue}
	•	Constraints: Neighboring regions must have different colors

Algorithm Used

Backtracking Search Algorithm:
	1.	Select an unassigned region
	2.	Try assigning a color
	3.	Check if it satisfies constraints
	4.	If valid, continue to next region
	5.	If not, backtrack and try another color

Implementation Details
	•	Language: Python 3
	•	Approach: Recursive Backtracking
	•	Constraint checking is done during assignment

How to Run

Step 1: Save the code

nano map_coloring.py

Step 2: Run the program

python3 map_coloring.py

Sample Output

WA Red  
NT Green  
Q Red  
SA Blue  
NSW Green  
V Red  
T Red  

Features
	•	Simple CSP implementation
	•	Beginner-friendly logic
	•	Uses backtracking technique
	•	Easy to extend

Possible Improvements
	•	Implement MRV heuristic
	•	Add Forward Checking
	•	Use Arc Consistency (AC-3)
	•	Add visualization
	•	Support dynamic color inputs

Applications
	•	Scheduling problems
	•	Resource allocation
	•	Timetabling
	•	Puzzle solving (e.g., Sudoku)

Key Concepts
	•	CSP: Assign values under constraints
	•	Backtracking: Try, check, undo if needed
	•	Constraint: Rule that must be satisfied

Conclusion

This project demonstrates how CSP can be used to solve the map coloring problem efficiently using backtracking while ensuring all constraints are satisfied.
