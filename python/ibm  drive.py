                                                                            '''         IBM  CODE KNACK-CIC CAMPUS RECRUITMENT PROCESS: BATCH 2023'''          #  18 Jan 2023
                                ''' INPUT                                                                           OUTPUT                                                                                                       INPUT                                                                                          OUTPUT
                                     ------                                                                      ---------                                                                                           --------                                                                                 -----------
                                  Test 1:                                                                                                                                                                                                 Test 2:                                                                                      No prime is available
                                     4                                                                                 13--->(if  large no is prime no then print this)                         4
                                     4                                                                                                                                                                                                                 4                                                                                                       |          
                                      1  2   3   4                                                                                                                                                                                                 3  2  1   1                                                                            (largest no 8 it is not an prime no)              
                                      4  3  2   1                                                                                                                                                                                                  4 3  3   2          
                                      7  8  9   6                                                                                                                                                                                                 8   1   1   0
                                      13  5  4  3                                                                                                                                                                                                 2   3   1   8
                                    '''                                            
#define function
def fun(matrix):
    l=[]
    f=0
    
#right diagonal elements    
    for i in range(4):
        for j in range(4):
            if (i==j):
                l.append(matrix[i][j])
                
 #left diagonal elements               
    for i in range(4):
        for j in range(4):
            if (i+j==3):
                l.append(matrix[i][j])             
    l.sort()  '''---->'*****assending order '''
    n=len(l)
    #print(l[n-1])

'''************prime no checking***************************
--------------------------------------------------'''
    for i in range(2,l[n-1]):
        if(l[n-1]%i==0):
            f=0
            break
        else:
             f=1

    if (f==1):
      print(l[n-1])
    else:
     print("No prime number is available")


#  main function

r=int(input())
c=int(input())
mat=[]
for i in range(r):
    culm=[]
    for j in range(c):
        culm.append(int(input()))
    mat.append(culm)    
fun(mat)
