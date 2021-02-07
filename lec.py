import os
import time


def countdown(minutes):
    seconds = int(minutes * 60)
    for i in range(1, seconds + 1):
        out = f"{seconds - i} seconds remaining".rjust(23)
        print(out, end="\r", flush=True)
        time.sleep(1)
    print("\n\n    TIME'S UP!")


def cls():
    os.system("cls")
