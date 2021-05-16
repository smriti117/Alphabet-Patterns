
""" 

* * * * * 
*         *
*         *
*        *
* * * * *   
*        *
*   	  *      
*         *
* * * * * 

Print Letter : B

"""
n = int(input("enter number of stars : "))
#n = 5
print(n * " * ")
for row in range(0,3):
	print(" * ",end= "")
	print((n-row)*"  ",end="")
	print(" * ")
print((n-2)* " * ")
for col in range(0,3):
	print(" * ",end="")
	print((col+(n-2))*"  ",end="")
	print(" * ")
print(n * " * ")
