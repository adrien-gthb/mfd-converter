#!/usr/bin/env python

########## MIFARE Classic 4K B keys converter ##########
# input: list of B keys                                #
# ouput: mfd file                                      #
########################################################

import sys

def usage():
    print sys.argv[0] + ' <in.txt> <out.mfd>'

def _convert(key):
    b = ''
    j = 0
    for i in range(len(key) / 4):
        j += 2
        b += key[j-2:j]
        b += key[j:j+2]
        j += 2
    return bytearray.fromhex(b)

def _write_trailer(f, d):
    for j in range(10):
        f.write(b'\x00')
    f.write(d)

def _write_n_block(f, n, d):
    for i in range(n):
        for j in range(16):
            f.write(d)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)
    k = open(sys.argv[1], 'r')
    f = open(sys.argv[2], 'wb')
    l = k.read().splitlines()
    for i, d in enumerate(l):
        block_per_sector = 16
        if i < 32:
            block_per_sector = 4
        _write_n_block(f, block_per_sector - 1, b'\x00')
        _write_trailer(f, _convert(d))
    k.close();
    f.close();
