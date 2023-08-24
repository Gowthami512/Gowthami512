/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/


#include <stdio.h>

int main()
{
   int n;
   scanf("%d",&n);
   int k[n];
   for(int i=0;i<n;i++)
   {
       scanf("%d",&k[i]);
   }
   for( int i=0;i<n;i++){
       for(int j=i+1;j<n;j++){
           if(k[i]==k[j]){
               for(int l=j;l<n-1;l++)
               {
                   k[l]=k[l+1];
               }
               n--;
               
           }
       }

   }
   for(int i=0;i<n;i++){
       printf("%d ",k[i]);
   }
   

    return 0;
}
