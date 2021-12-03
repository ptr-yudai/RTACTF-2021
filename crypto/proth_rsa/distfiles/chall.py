from Crypto.Util.number import getRandomInteger, getPrime, isPrime
import os

def getProthPrime(n=512):
    # Proth prime: https://en.wikipedia.org/wiki/Proth_prime
    while True:
        k = getRandomInteger(n)
        p = (2*k + 1) * (1<<n) + 1
        if isPrime(p):
            return p, k

if __name__ == '__main__':
    # Plaintext (FLAG)
    m = int.from_bytes(os.getenv("FLAG", "FAKE{sample_flag}").encode(), 'big')

    # Generate key
    p, k1 = getProthPrime()
    q, k2 = getProthPrime()
    n = p * q
    e = 65537
    s = (k1 * k2) % n

    # Encryption
    c = pow(m, e, n)

    # Information disclosure
    print(f"n = 0x{n:x}")
    print(f"e = 0x{e:x}")
    print(f"s = 0x{s:x}")
    print(f"c = 0x{c:x}")
