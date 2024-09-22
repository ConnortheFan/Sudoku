from Cell import Cell
from Sudoku import Sudoku
from typing import List
from Move import Move

class Solver(Sudoku):
    """Create a Solver class that takes a Sudoku board and solves it with step by step instructions.
    
    Params:
        board (List[List[Cell]]): board used
        startMove (Move): head of moves linked list
        currMove (Move): current Solver move
        emptyCells (List[Cell]): list of empty cells
    """
    
    board: List[List[Cell]]
    startMove: Move
    currMove: Move
    emptyCells: List[Cell]
    
    def __init__(self, sudoku: Sudoku):
        """Initialize Solver from current board
        
        Solver will make copy of current Sudoku board and
        set all candidates for empty cells

        Args:
            sudoku (Sudoku): base Sudoku object
        """
        
        super().__init__()
        # Make copy of base board
        for i, row in enumerate(sudoku.board):
            for j, cell in enumerate(row):
                newCell: Cell = self.getCell(i+1,j+1)
                newCell.number = cell.number
                newCell.filled = cell.filled
                newCell.fixed = cell.fixed
        self.setAllCandidates()
        self.emptyCells = [cell for row in self.board for cell in row if cell.filled is False]
        
        
        
    def nakedSingle(self) -> bool:
        """Finds Naked Singles and makes first move

        If no Naked Singles found, returns False

        Returns:
            bool: if any changes were made
        """
        for cell in self.emptyCells:
            if len(cell.candidates) == 1:
                self.fill(cell, cell.candidates[0])
                self.currMove.setDesc("Naked Single")
                self.emptyCells.remove(cell)
                return True
        return False
        
        
def main() -> None:
    s = Sudoku("puzzles/8-21-24/easy")
    sol = Sudoku("puzzles/8-21-24/easysol")
    solver = Solver(s)
    solver.show()
    
    change = True
    while change:    
        change = solver.nakedSingle()
        
    solver.printMoves()
    print("Solver Result")
    solver.show()
    print("Solution")
    sol.show()
    
if __name__ == "__main__":
    main()