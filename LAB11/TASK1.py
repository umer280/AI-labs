#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'E'],
    'G': ['E']
}

# BFS function
def bfs(graph, start, goal):
    # Initialize open and closed lists
    open_list = deque([start])  # Use a queue for BFS
    closed_list = set()

    # Track the path
    path = {}

    while open_list:
        # Get the current node
        current_node = open_list.popleft()
        closed_list.add(current_node)

        # Check if the goal is reached
        if current_node == goal:
            # Reconstruct the path
            final_path = []
            while current_node in path:
                final_path.append(current_node)
                current_node = path[current_node]
            final_path.append(start)
            final_path.reverse()
            return final_path, open_list, closed_list

        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
                path[neighbor] = current_node  # Track the path

    return None, open_list, closed_list  # Goal not found

# Run BFS
start = 'A'
goal = 'G'
final_path, open_list, closed_list = bfs(graph, start, goal)

# Display results
print("Final Path:", final_path)
print("Open List at the end:", list(open_list))
print("Closed List at the end:", list(closed_list))


# In[ ]:




