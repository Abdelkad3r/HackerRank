#!/usr/bin/env python
#HackerRank | Practice Algorithms [Compare the Triplets]
#@Abdelkader

import sys

a = list(map(int, raw_input().split(' ')))
b = list(map(int, raw_input().split(' ')))

score = [0, 0]

alice = map(lambda x,y: x > y, a, b)
bob = map(lambda x,y: x < y, a, b)

score[0] += sum(alice)
score[1] += sum(bob)

print score[0], score[1]