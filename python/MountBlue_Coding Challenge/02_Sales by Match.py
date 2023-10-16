#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    shocks=0
    lst=list(set(ar))
    ar=list(map(int,ar))
    for i in range(len(lst)):
       
        '''for j in range(len(ar)):
            if(lst[i]==int(ar[i])):
                print(lst[i],ar[i])'''
        
        c=ar.count(lst[i]) 
        if(c>=2):
            print(c)
            shocks+=c//2
            
    return shocks         
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
