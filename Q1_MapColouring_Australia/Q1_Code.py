regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

colors = ['Red', 'Green', 'Blue']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment

    for region in regions:
        if region not in assignment:
            break

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]

    return None

solution = backtrack({})

for region in solution:
    print(region, solution[region])
