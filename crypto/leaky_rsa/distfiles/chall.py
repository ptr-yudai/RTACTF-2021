from Crypto.Util.number import getPrime, isPrime, inverse
import os

if __name__ == '__main__':
    # Plaintext (FLAG)
    m = int.from_bytes(os.getenv("FLAG", "FAKE{sample_flag}").encode(), 'big')

    # Generate key
    p = getPrime(600)
    q = getPrime(500)
    n = p*p*q*q
    e = 65537
    s = ((p**3 - 20211219*q) * inverse(p*p+q*q,n)) % n # tekitou (ha?)

    # Encryption
    c = pow(m, e, n)

    # Information disclosure
    print(f"n = 0x{n:x}")
    print(f"e = 0x{e:x}")
    print(f"c = 0x{c:x}")
    print(f"s = 0x{s:x}")
