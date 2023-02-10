# Façade Coding

- A magic square is a square matrix whose rows, columns and diagonals add up to the same value.
- I have built a system that helps us construct magic squares, but it's a little bit complicated. At the moment, it is composed of three classes:
  - **Generator** makes an array of random digits (suitably constrained) of a particular length.
    - You can use this generator several times to build a square matrix of required size.
  - **Splitter** splits a 2D square matrix into several lists containing all rows, all columns and all diagonals.
  - **Verifier** ensures that, given a list of lists, every single list adds up to the same value.
- Using all of the above, please implement a MagicSquareGenerator façade that uses all these three components to generate a valid magic square of the required size.
