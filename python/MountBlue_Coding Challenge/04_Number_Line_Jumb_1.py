''' You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number
line ready to jump in the positive direction (i.e, toward positive infinity).

        The first kangaroo starts at location  and moves at a rate of  meters per jump.
        The second kangaroo starts at location  and moves at a rate of  meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
If it is possible, return YES, otherwise return NO.

Example
 x1=2               x=(x1+v1,x2+v2)=3 YES either !=3 NO
 v1=1
 x2=1
 x3=2
    Input                   Output
   --------                 ---------
   0 3 4 2                      YES
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    win=" "
    kang1=x1+v1
    kang2=x2+v2
    j1,j2=1,1
    f=True
    while(f):
        if(kang1==kang2 and j1==j2):
            win="YES"
            f=False
        elif(x2-v1>1):
            win="NO"
            f=False
        else:
            kang1+=v1
            kang2+=v2
            j1+=1
            j2+=1
            
    return win         
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
