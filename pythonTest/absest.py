def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad')
    if x>=0:
        return x;
    else:
        return -x,x
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
def add_end(L=None):
	if L is None:
		L=[]
	L.append('end')
	return L


def calc(*numbers):
	sum=0
	for n in numbers:
		sum = sum+n*n
	return sum,'中文'
def person(name,age,**kw):
	print('name:',name,'age:','other',kw)
def person1(name,age,*,city,job):
	print(city,job)