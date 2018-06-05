# mfd-converter
Converts a list of MIFARE classic 4K B keys to mfd format.

Usage:

```
./mfd-converter.py b_keys.txt b_keys.mfd
```

The input file needs to be in this format:
```
000000000000
000000000000
000000000000
```

This is a very basic script that requires you to give **all** the B keys as
input. It is based on the memory layout of the MIFARE Classic 4K, therefore it
will not work with other types of card.
