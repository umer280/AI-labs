#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq

# Max-priority queue using heapq (by inverting values)
class MaxPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, value):
        # Invert the value to simulate max-priority queue
        heapq.heappush(self.heap, -value)

    def pop(self):
        # Invert the value back when popping
        return -heapq.heappop(self.heap)

    def __str__(self):
        # Return the heap as a list of positive values
        return str([-x for x in self.heap])

# Create a max-priority queue
max_pq = MaxPriorityQueue()

# Insert elements into the max-priority queue
elements = [4, 8, 1, 7, 3]
for element in elements:
    max_pq.push(element)
    print(f"After inserting {element}: {max_pq}")

