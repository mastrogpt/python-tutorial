#!/bin/bash

PAT="${1?pattern}"
DOIT="$2"

cd "$(dirname $0)"
cd ..
find packages -type d \( -name virtualenv \) -prune -o -type f -name '*.py' -print >/tmp/files

if test -z "$DOIT"
then cat /tmp/files | xargs grep -n "$PAT" 
else 
    cat /tmp/files | xargs grep -n "$PAT" | awk -F: '{ print $1 " " $2 }' | while read FILE NUM
    do  
        python3 .vscode/expand.py "$FILE" "$NUM"  solutions.txt
    done
fi