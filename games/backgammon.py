s = """
     A  B  C  D  E  F   G  H  I  J  K  L
   ┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
   ┃ ●  ·  ·  ·  ○  · ┃ ○  ·  ·  ·  ·  ● ┃
   ┃ ●  ·  ·  ·  ○  · ┃ ○  ·  ·  ·  ·  ● ┃
   ┃ ●  ·  ·  ·  ○  · ┃ ○  ·  ·  ·  ·  · ┃
   ┃ ●  ·  ·  ·  ·  · ┃ ○  ·  ·  ·  ·  · ┃
   ┃ ●  ·  ·  ·  ·  · ┃ ○  ·  ·  ·  ·  · ┃
   ┃                  ┃                  ┃
   ┃                  ┃                  ┃
   ┃ ○  ·  ·  ·  ·  · ┃ ●  ·  ·  ·  ·  · ┃
   ┃ ○  ·  ·  ·  ·  · ┃ ●  ·  ·  ·  ·  · ┃
   ┃ ○  ·  ·  ·  ●  · ┃ ●  ·  ·  ·  ·  · ┃
   ┃ ○  ·  ·  ·  ●  · ┃ ●  ·  ·  ·  ·  ○ ┃
   ┃ ○  ·  ·  ·  ●  · ┃ ●  ·  ·  ·  ·  ○ ┃
   ┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛
     M  N  O  P  Q  R   S  T  U  V  W  X
"""

bg_help = """
○ - Black (moves clockwise)
● - White (moves anti-clockwise)

Enter a move as <from><to>, for example:
  * 'IC' moves White from point I to point C.
  * 'IC' is an invalid move for Black.
  * 'UN' moves Black from point U to point N.

To move multiple pieces, separate by commas:
  * 'IC, EA' moves one White piece from I to C
    and another White piece from E to A.

To bear-off:
  * 'J-' moves Black from point J off the board.
  * 'R-' is an invalid move.

To auto bear-off:
  * You can't. Finish the game you lazy fuck.

For help on how to play Backgammon, use the internet.
"""

print(f"\n{s}\n")
print(bg_help)
