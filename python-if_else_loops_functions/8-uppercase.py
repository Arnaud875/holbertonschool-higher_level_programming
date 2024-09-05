#!/usr/bin/python3
def uppercase(s):
    result = ''.join([chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in s])
    print(result)
