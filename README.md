# Python [Nonogram/Hanjie/Griddler/etc](https://en.wikipedia.org/wiki/Nonogram) Solver

A little project to logically solve Nonograms without use of pure brute-force, enabling efficient solving on larger puzzles.

## Basic logic

The solver infers 'obvious' conclusions from the clues provided - ie if all possible combinations result in a row's element being filled, then this must be filled and the guess is improved.
To improve beyond the initial pass, an improvement must be made in the opposite row/column operation that alters an element of the column/row.
Take Row X for example, in the column phase of the solver, a change must be made to an element of Row X else there will be no additional information for the solver to improve upon.

## Also note

If no further 'obvious' elements can be filled yet the puzzle is not complete the solver will be unable to draw further conclusions.
