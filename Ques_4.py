# Write the python program to solve a quadratic equation?
import cmath

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter thr value of c: "))

# calculate the dicriminant
dis = (b**2)-(4*a*c)

# find the 2 result
ans1 = (-b-cmath.sqrt(dis))/(2*a)
ans2 = (+b-cmath.sqrt(dis))/(2*a)

print("The roots are: ")
print(ans1)
print(ans2)