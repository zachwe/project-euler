class Node:
    def __init__(self, val, p=None):
        self.val = val
        self.p = p
        self.adj = []
        self.maxparents = val
        self.new = True
    def __repr__(self):
        return str(self.val)

def Run():
    """Run the program"""
    with open('in.txt', 'rb') as inp:
        source = Node(int(next(inp)))
        row = [source]
        for line in inp:
            prevrow, row = row, map(lambda x: Node(int(x)), line.split(" "))
            for i, n in enumerate(prevrow):
                n.adj.append(row[i])
                n.adj.append(row[i + 1])
    maxtotal, maxpathsink = 0, None
    print source.adj
    q = [source]
    while q:
        curr = q.pop(0)
        for n in curr.adj:
            if n.new:
                q.append(n)
                n.new = False
            if n.maxparents < curr.maxparents + n.val:
                n.maxparents = curr.maxparents + n.val
                n.p = curr
            if n.maxparents > maxtotal:
                maxtotal = n.maxparents
                maxpathsink = n
    print maxtotal
    print maxpathsink.p
    path = [maxpathsink]
    while maxpathsink.p:
        path.append(maxpathsink.p)
        maxpathsink = maxpathsink.p
    print path[::-1]
    print sum([x.val for x in path])

if __name__ == '__main__':
    Run()



