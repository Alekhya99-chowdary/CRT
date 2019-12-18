#include <stdio.h>

int main()
{
char name[20];
char sname[20];
printf("enter your name");
scanf("%s",&name);
printf("enter your surname");
scanf("%s",&sname);
printf("your name is %s\n",name); //prints in next line
printf("your surname is %s\n",sname);
printf("your name is %s\t",name); // prints with one tab space
printf("your surname is %s\n",sname);
printf("your name is %s\b",name); //prints two sentences combinly
printf("your surname is %s\n",sname);
printf("your name is %s\r",name); //replaces 1st sentence with 2nd
printf("your surname is %s\n",sname);
return 0;
}
