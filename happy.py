num=input()
k=num
def square(n):
	x=0
	while n>0:
		r=n%10
		n=n/10
		x=x+r**2
	return x
for i in range(1000):
	num=square(num)
if num==1:
	print k,"is a happy number"
else:
	print k,"is not a happy number"
	
