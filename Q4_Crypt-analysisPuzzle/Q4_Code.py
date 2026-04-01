letters=[]
domains={}

def init_words(a,b,c):
    global letters,domains
    letters=list(set(a+b+c))
    domains={x:list(range(10)) for x in letters}

def to_number(word,assign):
    return int("".join(str(assign[ch]) for ch in word))

def valid_partial(assign,a,b,c):
    if any(assign.get(x)==0 for x in [a[0],b[0],c[0]] if x in assign):
        return False
    vals=[assign[x] for x in assign]
    if len(vals)!=len(set(vals)):
        return False
    return True

def valid_full(assign,a,b,c):
    if not valid_partial(assign,a,b,c):
        return False
    return to_number(a,assign)+to_number(b,assign)==to_number(c,assign)

def select_var(assign):
    for v in letters:
        if v not in assign:
            return v

def forward(assign,var,val):
    removed={}
    for v in letters:
        if v not in assign and val in domains[v]:
            removed[v]=domains[v][:]
            domains[v]=[x for x in domains[v] if x!=val]
            if not domains[v]:
                return None,removed
    return True,removed

def restore(removed):
    for v in removed:
        domains[v]=removed[v]

def backtrack(assign,a,b,c):
    if len(assign)==len(letters):
        return assign if valid_full(assign,a,b,c) else None

    var=select_var(assign)

    for val in domains[var]:
        assign[var]=val

        if valid_partial(assign,a,b,c):
            ok,removed=forward(assign,var,val)

            if ok:
                res=backtrack(assign,a,b,c)
                if res:
                    return res

            if removed:
                restore(removed)

        assign.pop(var)

    return None

def solve(a,b,c):
    return backtrack({},a,b,c)

def display(sol,a,b,c):
    n1=to_number(a,sol)
    n2=to_number(b,sol)
    n3=to_number(c,sol)

    print("\nSolution:\n")
    print(f"  {a} = {n1}")
    print(f"+ {b} = {n2}")
    print(f"  {'-'*len(str(n3))}")
    print(f"  {c} = {n3}")

    print(f"\n  {n1} + {n2} = {n1+n2}")

    print("\nValues:\n")
    for k in sorted(sol):
        print(f"  {k} = {sol[k]}")
    print()

w1="TWO"
w2="TWO"
w3="FOUR"

init_words(w1,w2,w3)

print("\n*** Crypt-Arithmetic Puzzle using CSP ***\n")

while True:
    print("1. Solve Puzzle")
    print("2. Enter New Words")
    print("3. Show Current Puzzle")
    print("4. Exit\n")

    try:
        ch=int(input("Enter choice: "))
    except:
        continue

    if ch==1:
        solution=solve(w1,w2,w3)
        if solution:
            display(solution,w1,w2,w3)
        else:
            print("No solution\n")

    elif ch==2:
        w1=input("First word: ").strip().upper()
        w2=input("Second word: ").strip().upper()
        w3=input("Result word: ").strip().upper()
        init_words(w1,w2,w3)

    elif ch==3:
        print(f"\n  {w1}")
        print(f"+ {w2}")
        print(f"  {'-'*len(w3)}")
        print(f"  {w3}\n")

    elif ch==4:
        break
