from random import randint


if __name__ == "__main__":
    print("input dice roll as <num dice>d<num sides>\ne.g.: 2d6 to roll a d6 twice\ntype 'q' to quit.")

    while True:
        roll = input("\n > ")

        if roll.strip() and roll != "q":
            try:
                n, d = map(int, roll.split("d"))
            except (IndexError, ValueError):
                print("Invalid roll! Must be of the form <num dice>d<num sides>, like 5d20, or 1d6.")
                continue

            if (n, d) == (0, 0):
                print("That's not how any of this works.")
            elif n == 0:
                print("You rolled zero dice. Good job.")
            elif d in (0, 1):
                derp = "silly" if d == 1 else "you walnut"
                print(f"There's no such thing as a {d}-sided die, {derp}.")
            elif d == 2:
                total = sum(randint(1, d) - 1 for _ in range(n))
                coin_coins = "coin" if n == 1 else "coins"
                print(f"\nYou flipped {n} {coin_coins}.\nTotal heads: {total}.")
            else:
                total = sum(randint(1, d) for _ in range(n))
                die_dice = "die" if n == 1 else "dice"
                print(f"\nYou rolled {n} {d}-sided {die_dice}.\nTotal: {total}.")

        elif roll == "q":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input, please try again!")
            continue
