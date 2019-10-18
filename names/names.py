import time
from lru_cache import LRUCache
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Solution with cache => Runtime on my system == 0.0193 => O(n)
# cache = LRUCache(10000)
# for name in names_1:
#     cache.set(name, name)
# for name in names_2:
#     duplicate = cache.get(name)
#     if duplicate:
#         duplicates.append(duplicate)


# Solution with sorting and binary search => Runtime on my system == 0.054 => Runtime == 2(n log n) => O(n log n)
sorted_names_1 = sorted(names_1)    # O(n log n)
for name in names_2:                # O(n)
    start = 0
    end = len(sorted_names_1) - 1
    duplicate = None
    while start <= end:                 #O(log n)
        middle = int((start + end)/ 2)
        midpoint = sorted_names_1[middle]
        if midpoint > name:
            end = middle - 1
        elif midpoint < name:
            start = middle + 1
        else:
            duplicate = midpoint 
            break
    if duplicate:
        duplicates.append(duplicate) 
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

