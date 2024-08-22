from Cell import Cell
from Sudoku import Sudoku
from typing import List
from Move import Move

class Solver(Sudoku):
    """Create a Solver class that takes a Sudoku board and solves it with step by step instructions.

    Args:
        Sudoku: base Sudoku board
    """
    
    board: List[List[Cell]]
    empty: List[Cell]
    moves: List[Move]

    
    def __init__(self, filename: str = ""):
        """Initialize Solver from current board
        
        Solver will 

        Args:
            filename (str, optional): filename of board. Defaults to ""
        """
        
        super().__init__(filename)
        self.moves = []
        self.empty = [cell for row in self.board for cell in row if cell.filled is False]