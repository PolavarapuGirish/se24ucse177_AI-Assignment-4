Map Coloring Problem using CSP (Australia)

The Map Coloring Problem is a classic example of a Constraint Satisfaction Problem (CSP) in Artificial Intelligence. The objective is to assign colors to regions on a map such that no two adjacent regions share the same color.
In this project, we solve the map coloring problem for the seven principal states and territories of Australia using a backtracking-based CSP approach.

⸻

 Regions Considered
	•	WA (Western Australia)
	•	NT (Northern Territory)
	•	Q (Queensland)
	•	SA (South Australia)
	•	NSW (New South Wales)
	•	V (Victoria)
	•	T (Tasmania)

⸻

 Domain (Available Colors)

Each region can be assigned one of the following colors:
	•	Red
	•	Green
	•	Blue

⸻

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

⸻

 CSP Components
	•	Variables: WA, NT, Q, SA, NSW, V, T
	•	Domain: {Red, Green, Blue}
	•	Constraints: Neighboring regions must have different colors

⸻

 Algorithm Used

We use the Backtracking Search Algorithm:
	1.	Select an unassigned region
	2.	Try assigning a color
	3.	Check if it satisfies constraints
	4.	If valid, continue to next region
	5.	If not, backtrack and try another color

⸻

 Implementation Details
	•	Language: Python 3
	•	Approach: Recursive Backtracking
	•	Constraint checking is done dynamically during assignment

⸻

 How to Run

Step 1: Save the code

nano map_coloring.py

Paste the code and save.

Step 2: Run the program

python3 map_coloring.py


⸻

 Sample Output

WA Red
NT Green
Q Red
SA Blue
NSW Green
V Red
T Red


⸻

 Features
	•	Simple and clean CSP implementation
	•	Easy to understand for beginners
	•	Uses minimal data structures
	•	Can be extended with advanced heuristics

⸻

 Possible Improvements
	•	Use MRV (Minimum Remaining Values) heuristic
	•	Apply Forward Checking
	•	Use AC-3 (Arc Consistency)
	•	Add graphical visualization of the map
	•	Allow dynamic number of colors

⸻

 Applications
	•	Scheduling problems
	•	Resource allocation
	•	Register allocation in compilers
	•	Sudoku solving
	•	Timetabling problems

⸻

 Key Concepts Explained Simply
	•	CSP: A problem where we assign values under constraints
	•	Backtracking: Try → Check → Undo if wrong
	•	Constraint: Rule that must not be violated

⸻

 Conclusion

This project demonstrates how CSP can be used to solve real-world problems like map coloring efficiently. The backtracking approach ensures that all constraints are satisfied while exploring possible solutions systematically.
