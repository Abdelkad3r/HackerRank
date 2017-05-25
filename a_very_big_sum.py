#!/usr/bin/env python
#HackerRank | Practice Algorithms [A Very Big Sum]
#@Abdelkader

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

for i in range(n):
	s = sum(arr)

print s
