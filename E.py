
""" 
* * * * * 
*
*
*
* * * * *
*
*
*
* * * * *
""" 


def pattern(n):
	rounnd = 1
	for time in range(rounnd):
		print(n*"* ")
		for i in range(0,n):
			print("*")
		print(n*"* ")
		for j in range(0,n):
			print("*")

		print(n*"* ")


n = int(input("enter number of stars : "))
pattern(n)

