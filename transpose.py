x = [[i for j in range(10)] for i in range(4)]

xt = [[*t] for t in zip(*x)]

print("\nx:\n")
for row in x:
    print(row,)

print("\nx transpose:\n")
for row in xt:
    print(row,)
