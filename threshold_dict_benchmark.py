from random import seed, random
import numpy as np
import timeit


def py_thresh(x, thresh):
    d = {
       f"<= {thresh}": 0,
       f"> {thresh}": 0
    }
    for flt in x:
        if flt < thresh:
            d[f"<= {thresh}"] += 1
        else:
            d[f"> {thresh}"] += 1
    return d


def better_py_thresh(x, thresh):
    d = {}
    d[f"<= {thresh}"] = sum(1 if val <= thresh else 0 for val in x)
    d[f"> {thresh}"] = len(x) - d[f"<= {thresh}"]
    return d


def np_thresh(x, thresh):
    d = {}
    mask = x <= thresh
    d[f"<= {thresh}"] = len(mask[mask])
    d[f"> {thresh}"] = len(x) - d[f"<= {thresh}"]
    return d


x = np.array([random() for _ in range(100000)])
thresh = round(random(), 3)

t1 = timeit.timeit(
    "py_thresh(x, thresh)",
    number=1000,
    globals=globals()
)


t2 = timeit.timeit(
    "better_py_thresh(x, thresh)",
    number=1000,
    globals=globals()
)


t3 = timeit.timeit(
    "np_thresh(x, thresh)",
    number=1000,
    globals=globals()
)


print(py_thresh(x, thresh) == better_py_thresh(x, thresh) == np_thresh(x, thresh))
print(f"py_thresh: {round(t1, 2)} s")
print(f"better_py_thresh: {round(t2, 2)} s")
print(f"np_thresh: {round(t3, 2)} s")
