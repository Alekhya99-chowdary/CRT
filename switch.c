#include<stdio.h>
int main()
{
	int a,b,choice;
	printf("enter 2 numbers");
	scanf("%d%d",&a,&b);
	printf("enter your choice");
	scanf("%d",&choice);
	switch(choice)
	{
		case 1:
		printf("addition");
		printf("%d",a+b);
		break;
		case 2:
		printf("subtraction");
		printf("%d",a-b);
		break;
		case 3:
		printf("multiplication");
		printf("%d",a*b);
		break;
		case 4:
		printf("division");
		printf("%d",a%b);
		break;
		default:
		printf("can't be determined");
		break;
	}
	return 0;
}