''' 
The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm with a
running time of o(n**2) . In these next few challenges, we're covering a divide-and-conquer algorithm called Quicksort
(also known as Partition Sort).This challenge is a modified version of the algorithm that only addresses partitioning. It is implemented as 
follows:
left  eqaul   right
        4
 3             5
 3 2           5 7 

STDIN       Function                        Output 
-----       --------                     --------------
5           arr[] size n =5              3 2 4 5 7
4 5 3 7 2   arr =[4, 5, 3, 7, 2]              '''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    p=arr[0]
    left=[]
    equal=[]
    right=[]
    for i in range(len(arr)):
        if(arr[i]<p):
            left.append(arr[i])
        elif(arr[i]==p):
            equal.append(arr[i])
        elif(arr[i]>p):
            right.append(arr[i])
        
    return left+equal+right   
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
