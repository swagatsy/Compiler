void main(){
	int a;
	pl=&l;
	pt=&t;
	pa=&a;
	pm=&m;
	pn=&n;
	pb=&b;
	pu=&u;
	pv=&v;
	if(*pb<4){
		*pa=40;
	}
	else if(*pm<30){
		*pt=0;
	}
	else if(*pu<30){
		*pv=0;
	}
	else{
		*pb=0;
	}
	*pu=90;
	*pn=50;
}
