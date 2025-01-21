"""

Utiliser : 
- python3 wordz.py local/taylor_swift.txt
- python3 wordz.py local/taylor_swift.txt love

"""
import sys

from collections import Counter
from typing import Iterable

import click
import regex

TOKEN_PATTERN = regex.compile("(?u)\\b\\w+\\b")

def compte_mots(texte: Iterable[str]) -> Counter[str]:
    """Cette fonction permet de compter le nombre d'occurrences de chaque mot dans un texte."""
    res = Counter()
    for line in texte:
        res.update(TOKEN_PATTERN.findall(line))
    
    return res

@click.command()
@click.argument("inpt")
@click.argument("word", required=False)
def main(inpt: str, word: str | None):

    with open(inpt) as in_stream:
        count = compte_mots(in_stream)
    
    if word is not None :
        print(f"{word}: {count[word]}")

    else :
        for w,c in count.most_common(16):
            print(f"{w}: {c}")
   
if __name__ == "__main__":
    main()


















