# Tuplet

A Tuplet (unsure if name already exists) is a group of cells in the same row/column/box that also share the same candidates, where the total number of candidates is the same as the number of cells in the group.

It is also referred to as twins when there are 2 cells, triplets for 3 cells, and so on, hence the name Tuplet to account for all sized groups.

A Tuplet is used to remove the shared candidates from all cells in the same row/column/box not in the Tuplet.

For example, consider 4 empty cells in a row with the following candidates:

1. 1,2
2. 1,2
3. 1,2,3,4
4. 1,2,4

Cells 1 and 2 are a Tuplet (Twins) since they are 2 cells sharing 2 candidates (1 and 2). Due to this, cells 3 and 4 cannot contain the candidates 1 or 2, making cell 4 a Naked Single of a 4, which then leaves cell 3 as a Naked Single of a 3.

Another interpretation of this is that cells 1, 2, and 4 are a Tuplet (Triplets) since they are 3 cells sharing 3 candidates (1, 2, and 4). Due to this, cell 3 cannot contain the candidates 1, 2, or 4, making cell 3 a Naked Single of a 3.