'''             Text Wrap
  input                          output
---------                       -------------
ABCDEFGHIJKLMNOPQRSTUVWXYZ        ABCD
4                                 EFGH  
                                  IJKL
                                  MNOP 
                                  QRST 
                                  UVWX 
                                  YZ    '''
import textwrap

def wrap(string, max_width):
   st_val=''
   ln=len(string)
   r=l% max_width
   for i in range(0,ln,max_width):
       if(i==(l-r)):
         st_val=st_val+string[i:ln]
       else:
          st_val+=string[i:i+max_width]+'\n'  
    return st_val

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
