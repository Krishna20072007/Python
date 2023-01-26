def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


number = int(input("Enter a positive number : "))

if number < 0:
	print("Enter a positive number")

i = 0

for i in range(0, number):
	print(fibonacci(i))