import re

pattern = re.compile(r"(-?\d*)x\^?(\d*)|(-?\d*)")

polys = [
    "3x^4+9x^3+3x-7",
    "-5x^2+10x+4",
    "x+1"
]


for p in polys:
    print([*filter(any, pattern.findall(p))])
