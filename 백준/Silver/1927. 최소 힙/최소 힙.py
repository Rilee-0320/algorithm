import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, number)