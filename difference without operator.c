#include<stdio.h>
#define begin main
int begin()
{
    int n1,n2;
    printf("enter 2 numbers ");
    scanf("%d %d",&n1,&n2);
    printf("difference=%d",n1+~n2+1); //using ~ ( complement operator)
}


