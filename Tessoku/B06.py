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

n = int(input())
a = list(map(int, input().split()))
suma = list(accumulate(a))
suma = [0] + suma
q = int(input())

for i in range(q):
    l,r = map(int, input().split())
    if r-l+1 < 2 * (suma[r] - suma[l-1]):
        print('win')
    elif r-l+1 == 2 * (suma[r] - suma[l-1]):
        print('draw')
    elif r-l+1 > 2 * (suma[r] - suma[l-1]):
        print('lose')
    
