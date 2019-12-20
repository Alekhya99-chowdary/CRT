#include<stdio.h>
int main()
{
	int n;
	printf("enter a number");
	scanf("%d",&n);
	if(n%3==0)
	{
	 if(n%5==0)
		printf("fizzbizzz");
	else
		printf("fizz");
	}
	else if(n%5==0)
	{
		printf("bizz");
	}
		else
		{
			printf("%d",n);
		}
	return 0;
}