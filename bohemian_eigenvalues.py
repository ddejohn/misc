values = np.array([complex(0, 0),
                   complex(0, 0.01),
                   complex(0, -0.01),
                   complex(1, 0),
                   complex(-1, 0)])


par = [1, 0, 1, 0, 1]
mat = np.full((n, n), complex(0,0))
for i in range(1, n):
    mat[i, i-1] = random.choice(values) if par[0] else np.random.beta(0.1, 0.1)*2 - 1
    mat[i-1, i] = random.choice(values) if par[1] else np.random.beta(0.1, 0.1)*2 - 1
    mat[0, 0], mat[n-1, n-1] = 1j, 1
