class Link:
    def __init__(self, label):
        self.label = label
        self.nxt = None
    
    def __str__(self):
        return f"{self.label} -> {self.nxt}"


def duplets(triplets):
    dups = []
    for tup in triplets:
        for i in [0,1]:
            dup = [tup[i], tup[i+1]]
            if dup not in dups:
                dups.append(dup)
    return dups


def recoverSecret(triplets):
    # links = [Link(*dup) for dup in duplets(triplets)]
    links = []
    for dup in duplets(triplets):
        x, y = dup
        link = Link(x)
        link.nxt = Link(y)
        links.append(link)


    for link in links:
        print(link)



triplets = [
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']
]


recoverSecret(triplets)