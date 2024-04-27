#!/bin/bash

PAT="${1?pattern}"
DOIT="$2"

cd "$(dirname $0)"
cd ..
find packages -type d \( -name virtualenv \) -prune -o -type f -name '*.py' -print >/tmp/files

if test -z "$DOIT"
then echo "*** Dry Run: add a '-' to execute"
     cat /tmp/files | xargs grep -n "$PAT" 
     
else 
    cat /tmp/files | xargs grep -n "$PAT" | awk -F: '{ print $1 $NF }' | while read FILE SEARCH
    do  
        NUM="$(grep -n "$SEARCH" "$FILE" | awk -F: '{print $1}')"
        #echo $FILE $NUM $SEARCH
        python3 .vscode/expand.py "$FILE" "$NUM"  solutions.txt
    done
fi