#!/usr/bin/env python3

import sys
from random import randint

def makeRandom(length: int) -> str:
  res = ''
  while len(res) < length:
    options = list(range(0x30, 0x39))
    options.extend(list(range(0x41, 0x5A)))
    options.extend(list(range(0x61, 0x7A)))
    index = randint(0, len(options))
    res += chr(options[index])
  return res

if __name__ == '__main__':
  args = sys.argv
  res = makeRandom(int(args[1]))
  print(res)

