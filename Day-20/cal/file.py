# First way of importing
import cal
print(cal.add(3,4))
print(cal.sub(3,4))
print(cal.mul(3,4))
print(cal.div(3,4))
print(cal.mod(3,4))
print(cal.exp(3,4))

# output:
# 7
# -1
# 12
# 0.75
# 3
# 81

# Second use an allise name like
import cal as c
print(c.add(3,4))
print(c.sub(3,4))
print(c.mul(3,4))
print(c.div(3,4))
print(c.mod(3,4))
print(c.exp(3,4))

# Third import only the functions
from cal import add,sub,mul
print(add(3,4))
print(sub(3,4))
print(mul(3,4))

# Fourth way 
from cal import *
print(div(3,4))
print(mod(3,4))
print(exp(3,4))