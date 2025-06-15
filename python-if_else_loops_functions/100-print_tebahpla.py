#!/usr/bin/python3
print("".join([chr(c) if i % 2 == 0 else chr(c - 32) for i, c in enumerate(range(122, 96, -1))]), end="")
