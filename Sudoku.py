from typing import List
from Cell import Cell
from Move import Move

class Sudoku:
    """
    A class used to represent a Sudoku board.
    
    Uses 9x9 Cells to construct the board.
    Uses Moves to record changes
    """
    
    def __init__(self) -> None:
        pass
    
    def fill(self, row: int, col: int, number: int) -> bool:
        pass   
    
    def remove(self, row: int, col: int) -> bool:
        pass
    
    def removeCandidate(self, row: int, col: int, number: int) -> bool:
        pass
    
    def addCandidate(self, row: int, col: int, number: int) -> bool:
        pass
    
    def getRow(self, row: int) -> List[Cell]:
        pass
    
    def getCol(self, col: int) -> List[Cell]:
        pass
    
    def getBox(self, box: int) -> List[Cell]:
        pass
    
    def getRelated(self, row: int, col: int) -> List[Cell]:
        pass
    