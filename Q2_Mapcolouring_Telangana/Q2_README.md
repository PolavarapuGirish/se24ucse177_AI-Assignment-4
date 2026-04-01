## Map Coloring Problem using CSP (Telangana - 33 Districts)

## Overview
The objective is to assign colors to the 33 districts of Telangana such that no two adjacent districts have the same color.

This problem is solved using Constraint Satisfaction Problem (CSP) with a backtracking approach.

## Districts Considered
Adilabad  
Kumuram Bheem Asifabad  
Nirmal  
Mancherial  
Nizamabad  
Kamareddy  
Jagitial  
Peddapalli  
Karimnagar  
Rajanna Sircilla  
Siddipet  
Medak  
Sangareddy  
Vikarabad  
Hyderabad  
Medchal-Malkajgiri  
Rangareddy  
Yadadri Bhuvanagiri  
Jangaon  
Mahabubabad  
Warangal Rural  
Warangal Urban  
Jayashankar Bhupalpally  
Mulugu  
Bhadradri Kothagudem  
Khammam  
Suryapet  
Nalgonda  
Nagarkurnool  
Wanaparthy  
Jogulamba Gadwal  
Narayanpet  
Mahabubnagar  

## Domain (Available Colors)
Red  
Green  
Blue  
Yellow  

## Constraints (Adjacency Rules - Sample)
Adilabad -> Kumuram Bheem, Nirmal  
Kumuram Bheem -> Adilabad, Mancherial  
Nirmal -> Adilabad, Nizamabad  
Nizamabad -> Nirmal, Kamareddy, Jagitial  
Kamareddy -> Nizamabad, Medak  
Medak -> Kamareddy, Sangareddy, Siddipet  
Sangareddy -> Medak, Vikarabad  
Hyderabad -> Rangareddy, Medchal  
Rangareddy -> Hyderabad, Vikarabad, Mahabubnagar  
Mahabubnagar -> Rangareddy, Narayanpet, Wanaparthy  
Nalgonda -> Suryapet, Yadadri  
Khammam -> Bhadradri Kothagudem, Suryapet  

(You can expand all district adjacencies similarly)

## CSP Components
Variables: 33 districts  
Domain: Red, Green, Blue, Yellow  
Constraints: Adjacent districts must have different colors  

## Algorithm Used
1. Select an unassigned district  
2. Assign a color  
3. Check constraints  
4. Continue if valid  
5. Backtrack if invalid  

## Implementation Details
Language: Python 3  
Technique: Backtracking  

## How to Run
nano telangana_map.py  
python3 telangana_map.py  

## Sample Output
Adilabad Red  
Nirmal Green  
Nizamabad Blue  
Kamareddy Yellow  
...  

## Features
Handles large number of regions  
Uses CSP approach  
Backtracking ensures valid solution  

## Possible Improvements
Use MRV heuristic  
Forward checking  
Arc consistency (AC-3)  
Graph visualization  

## Applications
Scheduling  
Resource allocation  
Map design  
Timetabling  

## Conclusion
This demonstrates how CSP can scale from small problems (Australia) to larger real-world maps like Telangana with 33 districts.
