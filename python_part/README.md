# python DSA

---

## basic data structures / tools

### queue (FIFO) -> [tree BFS](#bfs)

```python
from collections import deque

queue = deque()         # create
queue.append(x)         # enqueue
item = queue.popleft()  # dequeue
```

### stack (LIFO) -> [tree DFS](#dfs)

```python
from collections import deque

stack = deque()
stack.append(x)
item = stack.pop()
```

- method 2

```python
stack = []
stack.append(x)     # push
item = stack.pop()  # pop
```



### tree / graph

- (a) Adjacency list (good for general trees & graphs)
```python
# a “tree” keyed by node_id, pointing to list of children
tree = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': [],
    'D': [],
    'E': []
}
```

- (b) Simple binary‑tree node class

```python
class TreeNode:
    __slots__ = ('val','left','right')
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# example:
root = TreeNode(1,
        left=TreeNode(2),
        right=TreeNode(3,
            left=TreeNode(4),
            right=TreeNode(5)))

```

#### BFS & DFS Traversals

```python
# BFS on adjacency list
def bfs(adj, start):

# DFS on adjacency list
def dfs(adj, start):
```

> When you’re traversing a graph (or a general ​tree​) given as an adjacency list, you need to decide:
> 1. What you feed in
> 2. How you record what you’ve already visited
> 3. How you record the order in which you visit nodes

##### 1. The Input: an Adjacency List + a Start Node
```
An adjacency list in Python is usually a dict whose keys are node‑identifiers and whose values are lists of their neighbors. For example:
```
```python
adj = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [], 
    'E': [],
    'F': []
}
start = 'A'
```

Here:

- `adj['A'] == ['B','C']` means `A` has two outgoing edges: `A→B` and `A→C`.
- The traversal routine will begin at the start node.

##### 2. Why Track `seen`

- Graphs can have cycles or multiple paths to the same node:
```
   A
  / \
 B – C
```

- Without remembering which nodes you’ve already queued or pushed, you might:
    - Visit B, then go B→C
    - From C, follow C→B again
    - From B go back to C … and never stop
- By keeping a seen set, you ensure each node is enqueued/pushed exactly once, giving you:
    - Correctness: you visit each node at most once
    - Termination: you avoid infinite loops in cyclic graphs

##### 3. Why Record `order`

Most traversal routines aren’t just about reaching every node—they also want to `return the sequence `in which nodes were `visited`. That sequence is often used for:
- Printing or inspecting the structure
- `Layer‑by‑layer processing (BFS)`
- `Pre‑order / post‑order analyses (DFS)`
You collect nodes into an order list at the moment you “officially” visit them (i.e. when you dequeue/popol or on the recursive call).

##### BFS

- BFS on adjacency list

```python
from collections import deque

def bfs(adj, start):
    seen  = {start}      # mark start as visited
    order = []           # will record visit order
    queue = deque([start])
    while queue:
        node = queue.popleft()  # visit in FIFO order; this node represents the first element in queue
        order.append(node)  # record that visit; record the traversal order
        for nbr in adj[node]:
            if nbr not in seen:
                seen.add(nbr)
                queue.append(nbr)
    return order

```

- deque gives us O(1) popleft()
- We only enqueue a neighbor when we first see it
- order grows in “wavefront” order: all nodes at distance 1, then distance 2, …

- Example
With the earlier adj:
```python
# 1. Start:
q = ['A'], seen = {'A'}
# 2. Pop A, enqueue its neighbors B,C →
order = ['A'], q = ['B','C'], seen = {'A','B','C'}
# 3. Pop B, enqueue D,E →
order = ['A','B'], q = ['C','D','E'], seen adds D,E
# 4. … and so on, producing ['A','B','C','D','E','F'].
```

##### DFS

- DFS on adjacency list

```python
def dfs(adj, start):
    seen  = {start}      # mark start as visited
    order = []           # will record visit order
    stack = [start]      # LIFO stack
    while stack:
        node = stack.pop()  # take the most recently added: LIFO
        order.append(node)
        # push children in reverse if you want left‑to‑right
        # push neighbors in reverse if you want the “natural” order
        for nbr in reversed(adj[node]):
            if nbr not in seen:
                seen.add(nbr)
                stack.append(nbr)
    return order
```

- A stack makes you dive “deep” first
- Reversing the neighbor list before pushing preserves left‑to‑right order
- `order` reflects a pre‑order walk of the graph/tree

---

### heap

#### min-heap

```python
import heapq
# 1) Start from a regular list
data = [5, 1, 7, 3, 2]
# 2) Turn it into a heap in O(n)
heapq.heapify(data)    # now data == [1, 2, 7, 3, 5] (the smallest element is at data[0])
# 3) Push/pop in O(log n)
heapq.heappush(data, 0)   # adds 0
smallest = heapq.heappop(data)  # pops and returns 0
```
Useful helpers
- `heapq.heappushpop(heap, x)` → push x, then pop & return the smallest (faster than push + pop).
- `heapq.heapreplace(heap, x)` → pop & return the smallest, then push x.
- `heapq.nlargest(k, iterable)` / `heapq.nsmallest(k, iterable)` → get the k biggest/smallest items in O(n + k log n).


#### max-heap

```python
import heapq

data = [5, 1, 7, 3, 2]
max_heap = [-x for x in data]  # negate it
heapq.heapify(max_heap)

# To pop the largest element:
largest = -heapq.heappop(max_heap)  # negate it back
```

---

## search

### binary search
```python
def binary_search(self, arr, target):
    """
    left, mid, right are index!
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # found
        elif arr[mid] < target:
            left = mid + 1  # search right
        else:
            right = mid - 1  # search left
    return -1  # not found
```

---

## common functions

### sort

#### for list

```python
lst.sort()
```

##### list of list sort by one of its value
```python
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
------------------------------------------------
intervals: List[Interval]
"""
intervals.sort(                   key=lambda elem: elem.start)
```

#### sort for dict

##### dict sort by key

```python
dd = {'b':2, 'a':5, 'c':1}

# get a dict whose keys are in ascending order
sorted_by_key = {k: dd[k] for k in sorted(dd)}
# → {'a':5, 'b':2, 'c':1}

# reverse order
sorted_by_key_desc = {k: dd[k] for k in sorted(dd, reverse=True)}
# → {'c':1, 'b':2, 'a':5}
```

##### dict sort by value

```python
from collections import defaultdict
dd = defaultdict(int)
sorted_lst_of_items = sorted(dd.items(), key=lambda item: item[1], reverse=True)  # item is a tuple
```

```python
sorted_dict_by_value = {
    k: v 
    for k, v in sorted(dd.items(), key=lambda kv: kv[1])
}
```

## common tools

### dict

- defaultdict

```python
from collections import defaultdict

dd = defaultdict(int)
# defaultdict(<class 'int'>, {
#     'apple': 3, 
#     'banana': 2, 
#     'orange': 1
# })

dd = defaultdict(list)
# defaultdict(<class 'list'>, {
#     0: [0, 3, 6],
#     1: [1, 4, 7],
#     2: [2, 5, 8]
# })

dd = defaultdict(dict)
# defaultdict(<class 'dict'>, {
#     'Alice': {'math': 90, 'eng': 85},
#     'Bob':   {'math': 75, 'eng': 82}
# })
```
