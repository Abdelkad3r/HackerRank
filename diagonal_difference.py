#!/usr/bin/env python
#HackerRank | Practice Algorithms [Diagonal Difference]
#@Abdelkader

import sys

n = int(raw_input().strip())
arr = []

for i in range(n):
	arr.extend(list(map(int, raw_input().strip().split(' '))))

first_index, first_sum = 0, 0

for j in range(n):
	first_sum = first_sum + arr[first_index]
	first_index = first_index + n + 1

second_index, second_sum = n - 1, 0

for k in range(n):
	second_sum = second_sum + arr[second_index]
	second_index = second_index + n - 1

res = abs(first_sum - second_sum)

print res
