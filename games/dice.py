import re
from random import randint


def get_dice() -> str:
    print("Input dice roll as <num dice>d<num sides>\ne.g.: 2d6 to roll a six-sided die twice.")
    while True:
        roll = input("\n > ").strip()
        if re.match("^0d0$", roll):
            print("That's not how that works! That's not how any of this works!")
            continue
        elif re.match(r"0{1}d\d*", roll):
            print("You rolled zero dice. Outstanding move!")
            continue
        elif re.match(r"\d*d[01]{1}$", roll):
            _, d = roll.split("d")
            print(f"There's no such thing as a {d}-sided die, you absolute walnut.")
            continue
        elif not re.match(r"[1-9]+\d*d[1-9]+\d*", roll):
            print("Invalid roll! Must be of the form <num dice>d<num sides>, like 5d20, or 1d6.")
            continue
        return roll


def dice_roller():
    roll = get_dice()
    n, d = map(int, roll.split("d"))
    if d == 2:
        total = sum(randint(1, d) - 1 for _ in range(n))
        coin_coins = "coin" if n == 1 else "coins"
        print(f"\nYou flipped {n} {coin_coins}\nHeads: {total}\nTails: {n - total}")
    else:
        total = sum(randint(1, d) for _ in range(n))
        die_dice = "die" if n == 1 else "dice"
        print(f"\nYou rolled {n} {d}-sided {die_dice}\nTotal: {total}")
    return total
