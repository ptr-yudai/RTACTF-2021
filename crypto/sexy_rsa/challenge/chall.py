from Crypto.Util.number import getPrime, isPrime
import os

def getSexyPrime(n=512):
    # Sexy prime: https://en.wikipedia.org/wiki/Sexy_prime
    while True:
        p = getPrime(n)
        if isPrime(p+6):
            return p, p+6

if __name__ == '__main__':
    # Plaintext (FLAG)
    m = int.from_bytes(os.getenv("FLAG", "FAKE{sample_flag}").encode(), 'big')

    # Generate key
    p, q = getSexyPrime()
    n = p * q
    e = 65537

    # Encryption
    c = pow(m, e, n)

    # Information disclosure
    print(f"n = 0x{n:x}")
    print(f"e = 0x{e:x}")
    print(f"c = 0x{c:x}")
