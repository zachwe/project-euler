
class Node:
    def __init__(self, weight, adj=None):
        self.parents = []
        self.visited = False
        self.maxParent = None
        self.weight = weight
        self.pathWeight = weight
        if adj:
            self.adjacencyList = adj
        else:
            self.adjacencyList = []

    def markVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.weight) + " " + str(self.adjacencyList)
   
def buildGraph():
    with open("p067_triangle.txt", "rb") as f:
        first = int(next(f).split()[0])
        source = Node(first)
        curr = [source]
        while True:
            try:
                nextrow = [Node(int(i)) for i in next(f).split()]
                for i, node in enumerate(curr):
                    if node == source:
                        print True
                    node.adjacencyList.append(nextrow[i])
                    node.adjacencyList.append(nextrow[i + 1])
                    nextrow[i].parents.append(node)
                    nextrow[i + 1].parents.append(node)
                curr = nextrow
            except StopIteration:
                break
    print len(source.parents)
    for adj in source.adjacencyList:
        print len(adj.parents)
    return source

def dijkstra(source):
    q = [source]
    maxSink = source
    print source.pathWeight
    while q:
        node = q.pop(0)
        q.extend(filter(lambda x: not x.visited, node.adjacencyList))
        if node.parents:
            maxParent = max(node.parents, key=lambda x: x.pathWeight)
            if maxParent.pathWeight + node.weight > node.pathWeight:
                node.pathWeight = maxParent.pathWeight + node.weight
                node.maxParent = maxParent
        if node.pathWeight > maxSink.pathWeight:
            maxSink = node
        for n in node.adjacencyList:
            n.visited = True
    return (maxSink, maxSink.pathWeight)
         

def Run():
    g = buildGraph()
    res = dijkstra(g)
    print res[1]

if __name__ == "__main__":
    Run()
