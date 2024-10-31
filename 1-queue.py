# # #!/usr/bin/python3

# # from collections import deque

# # q = deque()

# # q.append('a')
# # q.append('b')
# # q.append('c')

# # print("Initial queue", q)

# # q.popleft()
# # # q.popleft()
# # q.popleft()

# # print("after dequuing", q)


# from queue import Queue

# q = Queue(maxsize=3)

# q.put('a')
# q.put('b')
# q.put('c')


# print(q.get())
# print(q.get())
# print(q.get())


# print(q.empty())
# print(q.full())

import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges (nodes will be added automatically)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_color='black')
plt.show()
