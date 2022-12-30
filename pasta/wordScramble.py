# Given a list of letters (as a string), show all dictionary words
# that these letters can make up

import sys
import random

# Takes a list of letters in string and return a list of all permutations
# of those letters
def permute(string):
    if (len(string) == 1):
        return [string]
    if (len(string) == 2):
        return [(string[0] + string[1]), (string[1] + string[0])]

    ret = []
    for i in range(len(string)):
        # Recursively permute all leters except for the ith letter
        perm = permute(string[:i] + string[i+1:])
        perm = [(string[i] + s) for s in perm]
        ret = ret + perm

    return ret
    
def run(srcStr):
    file = open('/usr/share/dict/words', 'r', encoding='utf-8')
    
    dat = file.read().split('\n')
    datFull = [word.lower() for word in dat]
    
    # list of all permutations from input letters
    permutations = permute(srcStr.lower())

    results = []
    for numChar in range(3, len(srcStr) + 1):
        # take only the dictionary words of numChar length
        dat = [word for word in datFull if (len(word) == numChar)]
    
        # take only the first numChar of the input permutations,
        # filter to make the list unique
        choose = [w[:numChar] for w in permutations]
        choose = list(dict.fromkeys(choose))
    
        results = results + sorted([w for w in choose if (w in dat)])

    return results

if (__name__ == "__main__"):
    srcStr = sys.argv[1]
    results = run(srcStr)

    for w in results:
        print(w)
