from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.dictionary = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if not key in self.dictionary:
            return None
        node = self.dictionary[key]
        self.storage.move_to_front(node)
        return self.storage.head.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        value = [key, value]
        if key in self.dictionary:           
            node = self.dictionary[key]
            node.value = value 
            self.storage.move_to_front(node)
        elif self.size == self.limit:
            self.dictionary.pop(self.storage.tail.value[0])
            self.storage.remove_from_tail()
            self.storage.add_to_head(value)
            self.dictionary[key] = self.storage.head
        else:
            self.storage.add_to_head(value)
            self.dictionary[key] = self.storage.head
            self.size += 1
