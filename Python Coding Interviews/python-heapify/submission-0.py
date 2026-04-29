import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heap = []

    for s in strings:
        heapq.heappush(heap, s)

    return heap


def heapify_integers(integers: List[int]) -> List[int]:
    heap = []

    for i in integers:
        heapq.heappush(heap, i)

    return heap


def heap_sort(nums: List[int]) -> List[int]:
    heap = heapify_integers(nums)
    res = []

    while heap:
        res.append(heapq.heappop(heap))

    return res


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
