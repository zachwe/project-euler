import Queue

class BNode:
    def __init__(self, left=None, right=None):
        if left:
            self.left = left
        else:
            self.left = None
        if right:
            self.right = right
        else:
            self.right = None


with open("p081_matrix.txt", "rb") as f:
    matrix = []
    for line in f:
        matrix.append([int(s) for s in line.strip().split(',')])

    shortest_paths = [[matrix[0][0] if (not i and not j) else -1 for j in range(80)] for i in
                      range(80)]
    for i in range(80):
        for j in range(80):
            if i < 79:
                if (shortest_paths[i + 1][j] < 0 or shortest_paths[i + 1][j] >
                        shortest_paths[i][j] + matrix[i + 1][j]):
                    shortest_paths[i + 1][j] = shortest_paths[i][j] + matrix[i + 1][j]
            if j < 79:
                if (shortest_paths[i][j + 1] < 0 or shortest_paths[i][j + 1] >
                        shortest_paths[i][j] + matrix[i][j + 1]):
                    shortest_paths[i][j + 1] = shortest_paths[i][j] + matrix[i][j + 1]
    print shortest_paths[79][79]


