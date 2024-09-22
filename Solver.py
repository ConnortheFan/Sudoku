from Cell import Cell
from Sudoku import Sudoku
from typing import List
from Move import Move

class Solver:
    """Create a Solver class that takes a Sudoku board and solves it with step by step instructions.
    """
    
    sudoku: Sudoku
    emptyCells: List[Cell]
    
    def __init__(self, sudoku: Sudoku):
        """Initialize Solver from current board
        
        Solver will make copy of current Sudoku board

        Args:
            sudoku (Sudoku): Sudoku board
        """
        
        self.sudoku = sudoku.copy()
        self.emptyCells = [cell for row in self.sudoku.board for cell in row if cell.filled is False]
        