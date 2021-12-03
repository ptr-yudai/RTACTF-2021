import os

# Plaintext (FLAG)
plaintext = os.getenv("FLAG", "FAKE{sample_flag}").encode()
plai  = plaintext[:len(plaintext)//2]
ntext = plaintext[len(plaintext)//2:]
m1 = int.from_bytes(plai  + os.urandom(128), 'big')
m2 = int.from_bytes(ntext + os.urandom(128), 'big')

# Generate key
e = 65537
p = random_prime(1<<2048)
q = random_prime(1<<512)
r = random_prime(1<<512)
n1 = p * q
n2 = next_prime(p) * r
assert m1 < n1 and m2 < n2

# Encryption
c1 = pow(m1, e, n1)
c2 = pow(m2, e, n2)

# Information disclosure
print(f"e = {hex(e)}")
print(f"n1 = {hex(n1)}")
print(f"n2 = {hex(n2)}")
print(f"c1 = {hex(c1)}")
print(f"c2 = {hex(c2)}")
