#include<stdio.h>
int main()
{
	int height;
	printf("enter your height");
	scanf("%d",&height);
	if(height<150)
	{
		printf("lillyput");
	}
	else if((height>=150)&&(height<=165))
	{
		printf("average height");
	}
	else if((height>=165)&&(height<=190))
	{
		printf("tall");
	}
	else if(height>190)
	{
		printf("abnormal height");
	}
	else
	{
		printf("not a human");
	}
	return 0;
}