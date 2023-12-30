import math

# 累積和
from itertools import accumulate
from operator import mul
# result = list(accumulate(リスト))
# result = list(accumulate(リスト, operator.mul))

# 二部探索
from bisect import bisect_left, bisect_right
# index = bisect_left(sorted_array, value)
# index = bisect_right(sorted_array, value)

from sortedcontainers import SortedList
# slist = SortedList(リスト)
# slist.add(要素) : 要素追加
# index = slist.index(要素) : 要素検索

from collections import Counter, deque
from queue import Queue
from collections import defaultdict
import heapq
import sys

sys.setrecursionlimit(120000)

t = int(input())
n = int(input())
p = [0] * t
for i in range(n):
    l,r = map(int, input().split())
    p[l]+=1
    if r<t:
        p[r]-=1

p = list(accumulate(p))

for i in p:
    print(i)