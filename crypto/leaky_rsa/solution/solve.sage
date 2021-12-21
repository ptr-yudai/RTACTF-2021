with open("../distfiles/output.txt", "r") as f:
    exec(f.read())

P.<x> = PolynomialRing(Zmod(n))
f = (s*x + 20211219).monic()

kbits = 512
sol = f.small_roots(X=1<<kbits, beta=0.3)
q = int(sol[0])

pq = int(sqrt(int(n)))
assert pq % q == 0
p = pq // q

phi = p*q*(p-1)*(q-1)
d = inverse_mod(e, phi)
m = pow(c, d, n)

print(int.to_bytes(int(m), 256, 'big').lstrip(b'\0'))
