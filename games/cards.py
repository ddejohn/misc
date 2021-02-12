from random import shuffle


cards = [f"{rank} {suit}" for rank in range(2, 11) for suit in "♠♥♦♣"]
cards.extend([f"{rank} {suit}" for rank in "JQKA" for suit in "♠♥♦♣"])
print(cards)

