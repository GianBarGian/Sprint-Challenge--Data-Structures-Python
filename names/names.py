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
cache = LRUCache(10000)
for name in names_1:
    cache.set(name, name)
for name in names_2:
    duplicate = cache.get(name)
    if duplicate:
        duplicates.append(duplicate)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

