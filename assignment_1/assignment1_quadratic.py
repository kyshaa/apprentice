# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 2
b = 8
c = 1

# calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# find two solutions
r_1 = (- b - cmath.sqrt(discriminant)) / (2 * a)
root_1 = "{:.2f}".format(r_1)

r_2= (- b + cmath.sqrt(discriminant)) / (2 * a)
root_2 = "{:.2f}".format(r_2)

print('The roots are {0} and {1}'.format(root_1,root_2))
