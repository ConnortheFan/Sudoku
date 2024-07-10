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
    fixed: bool
        If the cell is immutable
    """

    row: int
    col: int
    box: int
    number: int
    candidates: List[int]
    filled: bool
    fixed: bool

    def __init__(self, row: int, col: int, number: int = 0) -> None:
        """Initialize cell

        Args:
            row (int): row
            col (int): column
            number (int, optional): number to fill cell. Defaults to empty cell
        """
        self.row = row
        self.col = col
        self.box = 3 * ((row - 1) // 3) + ((col - 1) // 3) + 1
        self.number = number
        self.candidates = []
        if number == 0:
            self.filled = False
            self.fixed = False
        else:
            self.filled = True
            self.fixed = True

    def fill(self, number: int) -> None:
        """Place a solid number into the cell

        Args:
            number (int): Number to place into the cell

        Returns:
            bool: If the placement was successful
        """
        self.number = number
        self.filled = True
    
    def empty(self) -> None:
        """Removes filled number from cell if filled
        """
        self.number = 0
        self.filled = False
    
    def addCandidate(self, number: int) -> None:
        """Adds a candidate to the cell

        Args:
            number (int): Candidate to add
        """
        self.candidates.append(number)
        self.candidates = list(set(self.candidates))
    
    def removeCandidate(self, number: int) -> None:
        """Remove a candidate from the cell

        Args:
            number (int): Candidate to remove
        """
        if number in self.candidates:
            self.candidates.remove(number)
    
    def clear(self) -> None:
        """Clears cell to basic state
        """
        self.number = 0
        self.candidates = []
        self.filled = False
    
    def setCandidates(self, candidates: List[int]) -> None:
        """Sets candidates to the cell

        Args:
            candidates (List[int]): List of candidates
        """
        self.candidates = candidates