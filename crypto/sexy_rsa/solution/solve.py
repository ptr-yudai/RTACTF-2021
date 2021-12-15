from ptrlib import root, inverse

with open("../distfiles/output.txt", "r") as f:
    exec(f.read())

p = -3 + root(n+9, 2)
q = n // p
d = inverse(e, (p-1)*(q-1))
m = pow(c, d, n)
print(int.to_bytes(m, 128, 'big').lstrip(b'\0'))
