import sys, re
from pathlib import Path

def extract(sol, ex, pref, rest):
    res = []
    f = open(sol)
    line = "x"
    while line:
        line =  f.readline()
        if not line.startswith(f"## {ex}"):
            continue
        res.append(f"{pref}#{rest}\n")
        line = f.readline()
        while line:
            if line.startswith("##"):
                break
            res.append(f"{pref}{line}")
            line = f.readline()
        break
    return res

def expand(sol,line):
    pattern = r'^(\s*)## (\d+\w*)(.*)$'
    match = re.search(pattern, line)
    if match:
        id = match.group(2)
        pref = match.group(1)
        rest = match.group(3)
        #print(id, len(pref))
        line = extract(sol, id, pref, rest)
    return line

def main(args):
    file = args[0]
    num = int(args[1]) -1
    sol = args[2]
    lines = Path(file).read_text().splitlines(keepends=True)
    expanded = expand(sol,lines[num])
    lines[num:num+1] = expanded
    Path(file).write_text("".join(lines))


if __name__ == "__main__":
    main(sys.argv[1:])

