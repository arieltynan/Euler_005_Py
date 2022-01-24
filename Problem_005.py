## Euler Problem 005
# Solved January 2021

# Smallest multiple
# smallest positive num evenly divisible by 1 to 20?

# only need to consider 11-20
# multiply primes 11, 13, 17, 19
# find min number of other prime factors 
# 2^4, 3^2, 5^1, 7^1
# Multiply all together

min = 11*13*17*19*16*9*5*7
print(min)