from typing import List
from Cell import Cell
from Move import Move

class Sudoku:
    """
    A class used to represent a Sudoku board.
    
    Uses 9x9 Cells to construct the board.
    Uses Moves to record changes
    """
    
    board: List[List[Cell]]
    missing: List[int]
    
    
    def __init__(self, filename: str = None) -> None:
        """Creates a Sudoku board.
        
        If no board is given, creates an empty board.

        Args:
            filename (str, optional): filename of Sudoku board to create. Defaults to None.
        """
        
        if filename == None:
            self.board = []
            for row in range(1,10):
                self.board.append([])
                for col in range(1,10):
                    self.board[row-1].append(Cell(row, col))

    
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
    
def main() -> None:
    board = Sudoku()
    print(f'Row 0 {list(range(1,10))}')
    for row in range(9):
        print(f'Row {row+1} {board.board[row]}')
    
if __name__ == "__main__":
    main()