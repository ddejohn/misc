# returns an iterable of the indices
# of the first row and first column
# of an nxn matrix


def row1_col1(n):
    x = set()
    for i in range(n):
        x.add((0, i))
        x.add((i, 0))
    return x
# end


def diags(lst):
    diag_list = []
    n = len(lst)
    for tup in row1_col1(n):
        i, j = tup
        diag = []
        for k in range(n-(i+j)):
            diag.append(lst[i+k][j+k])
        diag_list.append(diag)
    return sorted(diag_list)
# end

# lst =[
#     ["a", "b", "c"],
#     ["d", "e", "f"],
#     ["g", "h", "i"]
# ]


lst = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["i", "j", "k", "l"],
    ["m", "n", "o", "p"]
]

for row in diags(lst):
    print(row,)
# end
