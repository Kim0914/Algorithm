######################### O(n) = logn #####################################
a,b = input().split()
a = int(a)
b = int(b)
small_val = 0
large_val = 0
gcd = 0
lcm = 0

if(a>b):
    large_val = a
    small_val = b
else:
    large_val = b
    small_val = a

remainder = large_val % small_val

if(remainder == 0):
    gcd = small_val

while(remainder != 0):
    gcd = remainder
    large_val = small_val
    small_val = remainder
    remainder = large_val % small_val

lcm = int(a * b / gcd)
print(gcd)
print(lcm)

################ O(n) = N ####################
# if(a>b):
#     min_val = b
# else:
#     min_val = a

# for i in range(1,min_val+1):
#     if(a%i == 0 and b%i == 0):
#         gcd = i
#         lcm = int(i * (a/i) * (b/i))
# print(gcd)
# print(lcm)

