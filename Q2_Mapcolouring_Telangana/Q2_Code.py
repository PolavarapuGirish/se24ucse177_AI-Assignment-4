from collections import deque
import json

with open("telangana_adj.json") as f:
    adj = json.load(f)

colors_default = ["Red","Green","Blue","Black","White","Grey"]

def make_domains(cols):
    return {v:list(cols) for v in adj}

def revise(dom, xi, xj):
    changed = False
    for val in dom[xi][:]:
        if not any(val != o for o in dom[xj]):
            dom[xi].remove(val)
            changed = True
    return changed

def ac3(dom):
    queue = deque((xi, xj) for xi in adj for xj in adj[xi])
    while queue:
        xi, xj = queue.popleft()
        if revise(dom, xi, xj):
            if not dom[xi]:
                return False
            for xk in adj[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def is_valid(var, val, assignment):
    return all(assignment.get(n) != val for n in adj[var])

def select_var(assignment, dom):
    unassigned = [v for v in adj if v not in assignment]
    return min(unassigned, key=lambda v: len(dom[v]))

def forward_check(var, val, assignment, dom):
    pruned = {}
    for n in adj[var]:
        if n not in assignment:
            new_dom = [v for v in dom[n] if v != val]
            if not new_dom:
                return None, pruned
            pruned[n] = dom[n][:]
            dom[n] = new_dom
    return True, pruned

def backtrack(assignment, dom):
    if len(assignment) == len(adj):
        return assignment

    var = select_var(assignment, dom)

    for val in dom[var]:
        if is_valid(var, val, assignment):
            assignment[var] = val
            ok, pruned = forward_check(var, val, assignment, dom)

            if ok:
                result = backtrack(assignment, dom)
                if result:
                    return result

            assignment.pop(var)
            for k, v in pruned.items():
                dom[k] = v

    return None

def solve(cols):
    dom = make_domains(cols)
    if not ac3(dom):
        print("No solution possible with given colors")
        return None
    return backtrack({}, dom)

def display(solution):
    if not solution:
        print("No solution found\n")
        return

    print("\nSolution:\n")
    print(f"{'District':<30} Color")
    print("-"*40)

    for d in adj:
        print(f"{d:<30} {solution[d]}")
    print()

colors = list(colors_default)

while True:
    print("1. Solve")
    print("2. Set Colors")
    print("3. Show Districts")
    print("4. Show Colors")
    print("5. Exit\n")

    try:
        choice = int(input("Enter choice: "))
    except:
        continue

    if choice == 1:
        print("Using colors:", ", ".join(colors))
        result = solve(colors)
        display(result)

    elif choice == 2:
        raw = input("Enter colors (comma separated): ").split(",")
        new = [c.strip() for c in raw if c.strip()]
        if len(new) >= 3:
            colors = new

    elif choice == 3:
        for i, d in enumerate(adj, 1):
            print(i, d)

    elif choice == 4:
        print("Colors:", ", ".join(colors))

    elif choice == 5:
        break
