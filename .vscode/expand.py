import sys, re
from pathlib import Path

def extract(sol, num, pref, rest):
    res = []
    f = open(sol)
    line = "x"
    while line:
        line =  f.readline()
        if not line.startswith(f"## {num}"):
            continue
        res.append(f"{pref}# {num}{rest}\n")
        line = f.readline()
        while line:
            if line.startswith("##"):
                break
            res.append(f"{pref}{line}")
            line = f.readline()
        res.append("{pref}#\n")
        break
    return res

def expand(sol,line):
    pattern = r'^(\s*)## (\d+\w*)(.*)$'
    match = re.search(pattern, line)
    if match:
        num = match.group(2)
        pref = match.group(1)
        rest = match.group(3)
        #print(id, len(pref))
        line = extract(sol, num, pref, rest)
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

