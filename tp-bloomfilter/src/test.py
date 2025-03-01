# -*- coding: utf-8 -*-

import random
from hash_functions import HashFunctions
from bloomfilter import BloomFilter

def random_word ():
    """
    Returns a word with random letters whose length is between 4 and 7.

    :rtype: string
    """
    letters = [ chr(i) for i in range(ord('a'),ord('z')+1) ] + [ chr(i) for i in range(ord('A'),ord('Z')+1) ]
    length = 4 + random.randint(0,4)
    str = ""
    for i in range(length):
        str = str + random.choice(letters)
    return str
if __name__ == "__main__":
    """
    hashes = HashFunctions(8)
    bf = BloomFilter(16, hashes)
    w = random_word()
    bf.add("timoleon")
    if bf.contains("timoleon"):
        print("%s est present" % ("timoleon"))
    if bf.contains(w):
        print("%s est present" % (w))
    """
    with open('res.txt','w') as f:
        words = [random_word() for i in range(2**10)]
        for n in range(1,9):
            for t in range (10,21):
                tested = 0
                pos = 0
                hashes = HashFunctions(n)
                bf = BloomFilter(t,hashes)
                for e in words:
                    bf.add(e)
                for k in range(2**14):
                    r = random_word()
                    if not (r in words):
                        tested += 1
                        if bf.contains(r):
                            pos += 1
                f.write(f" {t} {n} {tested} {pos} {pos/tested} \n")
                f.write("\n")
                f.write("\n")





