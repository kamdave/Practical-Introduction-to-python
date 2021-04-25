'''write a program that computes the factorial of a number. The factorial, n!,of a number 
is the product of all the integers between 1 and n, including n. For instance, 5! = 1*2*3*4*5 = 120.
[Hint: Try Using a multiplicative equivalent of the summing technique.]'''

num = int(input("Enter a number(>0): "))
fact = 1
for c in range(num,0,-1):
  fact*=c
if num < 0:
  print("NA")
else:
  print(num,"!",fact)

