'''

                        HackerRank Software Development intern.
                input                                                                   output
         ---------------------                                                      -----------------
   Test 1:
   nine two double three four tripule five zero six                                    9233455506

   Test 2:
   double five four six one zero six eight one two                                     5546106812
'''
def getnumber(s):
    st=''
    l=s.split()
    ch={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    word=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(len(l)):
        for j in range(len(word)):
            if(l[i]==word[j]):
                st+=str(j)
                break
            elif(l[i]=='double'):
                v=ch[l[i+1]]
                st+=(str(v)*1)
                break
            elif(l[i]=='tripule'):
                v=ch[l[i+1]]
                st+=(str(v)*2)
                break             
    print(st)    

s=input()
getnumber(s)
