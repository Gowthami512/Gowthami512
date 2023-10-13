'''  convert capitalize formate
 input               output
-------              ---------
chrish alan           Chrish Alan      '''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l=list(s)
    l[0]=l[0].capitalize()
    for i in range(1,len(l)):
        if(l[i].isspace() and i<(len(l)-1)):
            if(l[i+1].isalpha()):
                l[i+1]=l[i+1].upper()
    return "".join(l)                   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
