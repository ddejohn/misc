# class Tree:
#     def __init__(self, label):
#         self.label = label
#         self.nodes = []

#     def __str__(self):
#         return self.label + "\n  -> ".join(map(str, self.nodes))
        # str_out = self.label

        # if not self.nodes:
        #     return str_out
        
        # for branch in self.nodes:
        #     str_out += f"\n  {branch}"
        
        # return str_out

    # def flatten(self):
    #     if not self.nodes:
    #         return self.label
        
    #     path = [self.label]
    #     for branch in self.nodes:



# def get_key(d, v):
#     return list(d.keys())[list(d.values()).index(v)]


def duplets(triplets):
    dups = []
    for tup in triplets:
        for i in [0,1]:
            dup = [tup[i], tup[i+1]]
            if dup not in dups:
                dups.append(dup)
    return dups


def recoverSecret(triplets):
    tree = {}
    roots, nodes = set(), set()
    for root, node in duplets(triplets):
        roots.add(root)
        nodes.add(node)
        tree[root] = tree.get(root, []) + [node]

    a, b = roots ^ nodes
    start, end = (a, b) if a in tree else (b, a)
    tree[end] = []

    return top_sort(tree)
    # print(tree)

def top_sort(graph):
    path = []
    visited = []
    temp = []
    nodes = [*graph.keys()]
    
    def visit(n):
        if n in visited:
            return

        temp.append(n)
        for m in graph[n]:
            visit(m)

        temp.remove(n)
        visited.append(n)
        path = [n] + path

    while nodes:
        n = nodes.pop()
        visit(n)
    
    return path


triplets = [
    ['w','h','i'],
    ['t','u','p'],
    ['h','a','p'],
    ['t','s','u'],
    ['t','i','s'],
    ['a','t','s'],
    ['w','h','s']
]



print(recoverSecret(triplets))