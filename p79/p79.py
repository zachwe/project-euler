import collections

fname = "p079_keylog.txt"

class Node:
    def __init__(self, val):
        self.val = val
        self.adj = []
        self.in_degree = 0

nodes = {}

with open(fname, "rb") as f:
    for line in f:
        line = line.strip()
        current_nodes = [nodes[c] if c in nodes else Node(c) for c in line]
        for node in current_nodes:
            if node.val not in nodes:
                nodes[node.val] = node
        i, j, k = current_nodes
        if j not in i.adj:
            i.adj.append(j)
            j.in_degree += 1
        if k not in j.adj:
            j.adj.append(k)
            k.in_degree += 1

stack = collections.deque()
for val, node in nodes.items():
    node.status = 0
    if node.in_degree == 0:
        node.status += 1
        stack.append(node)

# now do dfs.
out = ""
while stack:
    top = stack[-1]
    new_nodes = [node for node in top.adj if node.status == 0]
    if new_nodes:
        new_nodes[0].status += 1
        stack.append(new_nodes[0])
    else:
        top.status += 1
        out = top.val + out
        stack.pop()
print out



