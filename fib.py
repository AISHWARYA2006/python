def fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return (fib(n-1)+fib(n-2))
x=input()
for i in range(x):
	a=fib(i)
	print a
