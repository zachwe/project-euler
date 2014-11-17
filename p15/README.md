Here is the problem statement for Project Euler problem 15:

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?


The solution, which does not require any programming apart from the ability to compute (n choose m), is to see that a path is of length exactly (n + m), and exactly m slots will be rightwards moves.

Therefore, the solution for an n x m rectangle is (n+m) choose m.
