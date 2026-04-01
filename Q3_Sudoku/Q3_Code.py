from collections import deque
import copy

rows = 'ABCDEFGHI'
cols = '123456789'

cells = [r + c for r in rows for c in cols]

def build_units():
    u = []
    for r in rows:
        u.append([r + c for c in cols])
    for c in cols:
        u.append([r + c for r in rows])
    for rset in ['ABC','DEF','GHI']:
        for cset in ['123','456','789']:
            u.append([r + c for r in rset for c in cset])
    return u

unit_list = build_units()

cell_units = {v: [u for u in unit_list if v in u] for v in cells}

peers = {v: set(x for u in cell_units[v] for x in u if x != v) for v in cells}

def build_arcs():
    arc_list = set()
    for u in unit_list:
        for x in u:
            for y in u:
                if x != y:
                    arc_list.add((x, y))
    return list(arc_list)

arc_pairs = build_arcs()

default_puzzle = (
"003020600"
"900305001"
"001806400"
"008102900"
"700000008"
"006708200"
"002609500"
"800203009"
"005010300"
)

def initialize_domains(puzzle):
    dom = {}
    for i, v in enumerate(cells):
        num = int(puzzle[i])
        dom[v] = [num] if num != 0 else list(range(1, 10))
    return dom

def revise_domain(dom, x, y):
    updated = False
    for val in dom[x][:]:
        if not any(val != k for k in dom[y]):
            dom[x].remove(val)
            updated = True
    return updated

def apply_ac3(dom):
    queue = deque(arc_pairs)
    while queue:
        xi, xj = queue.popleft()
        if revise_domain(dom, xi, xj):
            if not dom[xi]:
                return False
            for neighbor in peers[xi]:
                if neighbor != xj:
                    queue.append((neighbor, xi))
    return True

def is_complete(dom):
    return all(len(v) == 1 for v in dom.values())

def select_unassigned(dom, assign):
    remaining = [v for v in cells if v not in assign]
    return min(remaining, key=lambda v: len(dom[v]))

def consistent(var, val, assign):
    return all(assign.get(p) != val for p in peers[var])

def forward_prune(var, val, dom):
    removed = {}
    for p in peers[var]:
        new_vals = [x for x in dom[p] if x != val]
        if not new_vals:
            return None, removed
        if len(new_vals) != len(dom[p]):
            removed[p] = dom[p][:]
            dom[p] = new_vals
    return True, removed

def backtrack_search(assign, dom):
    if len(assign) == len(cells):
        return assign

    var = select_unassigned(dom, assign)

    for val in dom[var][:]:
        if consistent(var, val, assign):
            assign[var] = val
            ok, removed = forward_prune(var, val, dom)

            if ok:
                result = backtrack_search(assign, dom)
                if result:
                    return result

            assign.pop(var)
            for p, vals in removed.items():
                dom[p] = vals

    return None

def solve_sudoku(dom):
    dom = copy.deepcopy(dom)

    if not apply_ac3(dom):
        return None

    if is_complete(dom):
        return {v: dom[v][0] for v in cells}

    initial_assign = {v: dom[v][0] for v in cells if len(dom[v]) == 1}

    return backtrack_search(initial_assign, dom)

def display(board, title=""):
    if title:
        print("\n" + title + "\n")

    for i, r in enumerate(rows):
        line = []
        for j, c in enumerate(cols):
            key = r + c
            val = board.get(key)

            if isinstance(val, list):
                val = val[0] if len(val) == 1 else "_"
            elif val is None:
                val = "."

            line.append(str(val))

        output = ""
        for k, v in enumerate(line):
            if k in [3, 6]:
                output += "| "
            output += v + " "

        print("  " + output)

        if i in [2, 5]:
            print("  ------+-------+------")

    print()

def input_puzzle():
    print("\nEnter 9 rows (use 0 for blanks):\n")
    s = ""
    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ").strip()
            if len(row) == 9 and row.isdigit():
                s += row
                break
    return s

print("\n*** Sudoku Solver using CSP ***\n")

puzzle_str = None
domains = None

while True:
    print("1. Load default puzzle")
    print("2. Enter custom puzzle")
    print("3. Solve puzzle")
    print("4. Show puzzle")
    print("5. Exit\n")

    try:
        choice = int(input("Enter choice: "))
    except:
        continue

    if choice == 1:
        puzzle_str = default_puzzle
        domains = initialize_domains(puzzle_str)
        display(domains, "Puzzle")

    elif choice == 2:
        puzzle_str = input_puzzle()
        domains = initialize_domains(puzzle_str)
        display(domains, "Puzzle")

    elif choice == 3:
        if domains is None:
            print("Load a puzzle first\n")
            continue

        solution = solve_sudoku(domains)

        if solution:
            display(solution, "Solution")
        else:
            print("No solution\n")

    elif choice == 4:
        if domains:
            display(domains, "Current Puzzle")
        else:
            print("No puzzle loaded\n")

    elif choice == 5:
        break
