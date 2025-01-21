"""

Utiliser : 
- python3 wordz.py local/taylor_swift.txt
- python3 wordz.py local/taylor_swift.txt love

"""
import sys

from collections import Counter
from typing import Iterable

import regex

TOKEN_PATTERN = regex.compile("(?u)\\b\\w+\\b")

def compte_mots(texte: Iterable[str]) -> Counter[str]:
    """Cette fonction permet de compter le nombre d'occurrences de chaque mot dans un texte."""
    res = Counter()
    for line in texte:
        res.update(TOKEN_PATTERN.findall(line))
    
    return res


def main():

    try:
        inpt = sys.argv[1]
    except IndexError:
        print("Invalid command. Usage: wordz INPT [WORD]")
        return

    inpt = sys.argv[1]
    with open(inpt) as in_stream:
        count = compte_mots(in_stream)
    
    if len(sys.argv) == 3 :
        w = sys.argv[2]
        print(f"{w}: {count[w]}")

    elif len(sys.argv) == 2:
        for w,c in count.most_common(16):
            print(f"{w}: {c}")
   
    else:
        print("Invalid command. Usage: wordz INPT [WORD]")

if __name__ == "__main__":
    main()














