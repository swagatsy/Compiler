int *g3, l3;
int *func1(int *x, int *y);
int *func2(int *a, float *b);
void func3();
float *var1, var2;
int *func1(int *a ,int *b)
{
    int *h1;

    if(*b == 32)
    {
        *var1 = 3.0;
    }
    
    return a;
}

void func3()
{
    int**a;
}


void main()
{
    int *g, **a1, *a2, a,**pp;
    float **f;
    *g = 4;
    if(*g < 4)
    {
        while(*g != 0)
        {
            *g = *g - 1;
        }
        **f = 3.0;
    }
    else
    {
        **f = 2.0;
    }   
    g = func1(*pp,a2);

    g = func2(*pp,*f);
}
int *func2(int *b1, float *b2)
{
    int **h1;
    if(*b1 == 32)
    {
        *var1 = 3.0;
    }
    else
    {
        while(*b2 != *var1)
        {

            *b2 = *b2 - 1.0;
        }
    } 
    return *&*&**h1;
}