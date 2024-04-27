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
        res.append(f"{pref}#: {num}{rest}\n")
        line = f.readline()
        while line:
            if line.startswith("##"):
                break
            res.append(f"{pref}{line}")
            line = f.readline()
        res.append(f"{pref}#.\n")
        break
    return res

def expand(sol,line):
    pattern = r'^(\s*)## (\d+\w*)(.*)$'
    match = re.search(pattern, line)
    if match:
        num = match.group(2)
        pref = match.group(1)
        rest = match.group(3)
        print("Expanding", num, rest)
        line = extract(sol, num, pref, rest)
    return line

def contract(lines, num):
    line = lines[num]
    pattern = r'^(\s*)#: (.*)$'
    match = re.search(pattern, line)
    if match:
        pref = match.group(1)
        rest = match.group(2)
        print("Contracting:", rest)
        line = f"{pref}## {rest}\n"
        end = num + 1
        while not lines[end].strip().startswith("#."):
            end += 1
        #print(line, num, end)
        return line, end+1
    return None, 0

def main(file, num, sol):
    # load
    lines = Path(file).read_text().splitlines(keepends=True)
    # contracting
    line, end = contract(lines, num)
    if line:
        lines[num:end] = [line]
    else:
        # expanding
        expanded = expand(sol,lines[num])
        lines[num:num+1] = expanded
    # save
    Path(file).write_text("".join(lines))

if __name__ == "__main__":
    args = sys.argv[1:]

    file = args[0]
    num = int(args[1]) -1
    sol = args[2]

    main(file, num, sol)


