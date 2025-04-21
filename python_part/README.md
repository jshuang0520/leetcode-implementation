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
