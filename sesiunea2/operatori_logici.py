# operatorii de logici dau un tip de date bool

x = True
y = False

print('x si y este', x and y)               # true if both are true
print('x sau y este', x or y)               # true if at least one is true
print('inversul lui x este', not x)         # changes truth value
print('inversul lui y este', not y)         # changes false value

print('x &/si y', x & y)                    # nu este corect
print('x &/si x', x & x)                    # nu este corect
