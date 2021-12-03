from ptrlib import inverse

with open("../distfiles/output.txt") as f:
    exec(f.read())

"""
a = k1, b = k2, s = ab
n = pq
  = 2^1024(2a+1)(2b+1) + 2^512((2a+1)+(2b+1)) + 1
  = 2^1024(4ab + 2a + 2b + 1) + 2^512(2a + 2b + 2) + 1
n-1 = 2^1024(4ab + 2a + 2b + 1) + 2^512(2a + 2b + 2)

phi(n) = (p-1)(q-1)
       = (2a+1)2^512 (2b+1)2^512
       = 2^1024(4ab + 2a + 2b + 1)
4ab + 2a + 2b + 1 = phi(n)/2^1024

n-1 = 2^1024(phi(n) / 2^1024) + 2^512(phi(n) - 4ab + 1)
    = phi(n) + 2^512(phi(n) - 4s + 1)
    = phi(n) + 2^512 phi(n) - 2^514 s + 2^512
"""

assert (n-1+(1<<514)*s-(1<<512)) % (1+(1<<512)) == 0
phi = (n-1+(1<<514)*s-(1<<512)) // (1+(1<<512))

d = inverse(e, phi)
m = pow(c, d, n)
print(int.to_bytes(m, 128, 'big').lstrip(b'\x00'))
