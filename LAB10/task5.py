#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue

# Create a LIFO queue
lifo_queue = queue.LifoQueue()

# Add items to the queue
lifo_queue.put("First")
lifo_queue.put("Second")
lifo_queue.put("Third")

# Retrieve items from the queue (LIFO order)
while not lifo_queue.empty():
    print(lifo_queue.get())

