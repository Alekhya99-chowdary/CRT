#include<stdio.h>
int main()
{
	char name[30];
	puts("enter your name");
	//gets(name);
	scanf("%[^\n]s",&name);
	puts("your name is");
	puts(name);
	return 0;
}