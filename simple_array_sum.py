#!/usr/bin/env python
#HackerRank | Practice [Simple Array Sum]
#@Abdelkader

from sys import *

n = int(raw_input())
arr = map(int, raw_input().strip().split(' '))

for i in range(n):
	s = sum(arr)

print s
