# Peg Puzzle Solver
This program performs a state-space search to solve the Peg Puzzle problem.

# Peg Puzzle Game Description
The following description was written by Kurt Eiselt and included in the course materials for ECS 170:

A version of something known as the peg puzzle consists of four pegs
(two blue and two red) and six holes.  Each of the holes may hold one
peg.  Initially the two red pegs are in the left-most holes, and the
two blue pegs are in the right-most holes.  (Note that the example in 
class used only one hole, not two.  That just allows the diagrams to
fit on a single PowerPoint slide better.  Makes no real difference.)

The object of this puzzle (and remember that it's a puzzle with one person
playing, not a game with two opponents), is to put the red pegs in the
right-most holes and the blue pegs in the left-most holes by moving one
peg at a time according to the following rules:

   A peg may be moved into an adjacent empty hole.
   A peg may jump over a single peg of another color into an empty hole.
   The blue pegs may only move or jump to the left.
   The red pegs may only move or jump to the right.

For this problem, we'll represent the current state of the puzzle as
a String, and the pegs by letters representing the color of the peg
B = blue, R = red, and _ = and empty hole

So the initial state described above is "RR__BB"
