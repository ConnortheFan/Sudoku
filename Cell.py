from typing import List


class Cell:
    """
    A class used to represent a cell in Sudoku.

    Attributes
    ----------
    row: int
        Row of the cell
    col: int
        Column of the cell
    box: int
        Box of the cell
    number: int
        Solid number of the cell
    candidates: list
        List of candidates for the cell
    filled: bool
        If the cell should be displayed as the number or the candidates
    immutable: bool
        If the cell is immutable
    """

    def __init__(self, row: int, col: int, box: int, number: int = 0, filled: bool = False) -> None:
        self.row: int = row
        self.col: int = col
        self.box: int = box
        self.number: int = number
        self.candidates: List[int] = [1,2,3,4,5,6,7,8,9]
        self.filled: bool = filled
        self.immutable: bool = filled

    def fill(self, number: int) -> bool:
        """Place a solid number into the cell

        Args:
            number (int): Number to place into the cell

        Returns:
            bool: If the placement was successful
        """

        

        return True
    
    def removeCandidate(self, number: int) -> bool:
        """Remove a candidate from the cell

        Args:
            number (int): Candidate number to remove

        Returns:
            bool: If the removal was successful
        """
        
        return True
    