#include <stdio.h>

int hello()
{
    printf ("Hello from DLL\n");
}

int SumNumbers(int a, int b)
{
    int c;
    c=a+b;
    return c;
}
/*
int main(void)
{
    int a ;
a=SumNumbers(4,5);
printf("%d",a);
}*/