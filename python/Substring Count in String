def count_substring(string, sub_string):
    c=0
    sl=len(sub_string)
    v=sub_string
    for i in range(len(string)-sl+1):
        k=string[i:i+sl]
        if(k==v):
            c+=1
           
    return c
    #return string.find(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
