void main ()
{
	int a, b, c, d, e, f, g;
	int *p, *q, *r, *s, *t, *u, *v; 
     
        
	*p = 13;
	*q = *p;
	*r = *q;
	*s = *r;
	*t = *s;
	*u = *t;
	*v = *u;
	*q = 13;
	*r = 13;
	*s = 13;
	*t = 13;
	*u = 13;
	*v = 13;
	v = v ; u = t;

}

