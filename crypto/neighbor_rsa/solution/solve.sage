with open("../distfiles/output.txt", "r") as f:
    exec(f.read())

K = 1<<1024
M = matrix(ZZ, [
    [K, n2],
    [0, -n1],
])

p = q = r = None
for row in M.LLL():
    q = abs(row[0] // K)
    if n1 % q == 0:
        p = n1 // q
        pp = next_prime(p)
        assert n2 % pp == 0
        r = n2 // pp
        break

phi1 = (p-1)*(q-1)
phi2 = (pp-1)*(r-1)
d1 = inverse_mod(e, phi1)
d2 = inverse_mod(e, phi2)
m1 = pow(c1, d1, n1)
m2 = pow(c2, d2, n2)

print(int.to_bytes(int(m1), 256, 'big').lstrip(b'\x00')[:-128])
print(int.to_bytes(int(m2), 256, 'big').lstrip(b'\x00')[:-128])
