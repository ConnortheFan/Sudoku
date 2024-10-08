from typing import List
from Cell import Cell
from Move import Move

class Sudoku:
    """
    A class used to represent a Sudoku board.
    
    Uses 9x9 Cells to construct the board.
    Uses Moves to record changes
    
    Params:
        board (List[List[Cell]]): 2D Array to represent Sudoku board
        startMove (Move): head of moves linked list
        currMove (Move): current move
    """
    
    board: List[List[Cell]]
    startMove: Move
    currMove: Move
    
    
    def __init__(self, filename: str = "") -> None:
        """Creates a Sudoku board.
        
        If no board is given, creates an empty board.

        Args:
            filename (str, optional): filename of Sudoku board to create. Defaults to None.
        """
        
        self.board = []
        self.startMove = Move()
        self.currMove = self.startMove
        if filename == "":
            for row in range(1,10):
                self.board.append([])
                for col in range(1,10):
                    self.board[row-1].append(Cell(row, col))
                    
        else:
            f = open(filename, "r")
            for row in range(1,10):
                nums = f.readline().split(" ")
                self.board.append([])
                for col in range(1,10):
                    self.board[row-1].append(Cell(row, col, int(nums[col-1])))
            f.close()
                

    def getCell(self, row: int, col: int) -> Cell:
        return self.board[row-1][col-1]
    
    def fill(self, cell, number: int) -> None:
        """Fills Cell with number and makes Move

        Args:
            cell (Cell or (int, int)): Either the Cell object or (row, col) tuple
            number (int): number
        """
        
        if isinstance(cell, tuple):
            cell = self.getCell(cell[0], cell[1])
        if not cell.fixed:
            move = Move(self.currMove)
            move.addChange(cell, "fill", [cell.number, number])
            cell.fill(number)
            for related in self.getRelatedUnfilled(cell):
                if number in related.candidates:
                    related.removeCandidate(number)
                    move.addChange(related, "removeCandidate", number)
            self.currMove = move
    
    def empty(self, cell) -> None:
        """Empty Cell by removing filled number

        Args:
            cell (Cell or (int, int)): Cell object or tuple (row, col)
        """
        if isinstance(cell, tuple):
            cell = self.getCell(cell[0],cell[1])
        if not cell.fixed and cell.filled:
            move = Move(self.currMove)
            move.addChange(cell, "empty", [cell.number, 0])
            cell.empty()
            self.currMove = move
    
    def clear(self, cell) -> None:
        """Clear all data in a Cell unless its fixed

        Args:
            cell (Cell or (int, int)): Cell object or tuple (row, col)
        """
        if isinstance(cell, tuple):
            cell = self.getCell(cell[0],cell[1])
        if not cell.fixed:
            move = Move(self.currMove)
            move.addChange(cell, "clear", [cell.candidates, []])
            cell.clear()
            self.currMove = move
    
    def removeCandidate(self, cells, numbers: int) -> None:
        """Removes candidate from Cells

        Args:
            cells (Cell or (int, int) or List[Cell, (int,int)]): Cell object, tuple (row, col), or List of Cells and tuples
            numbers (int or List[int]): candidate(s) to remove
        """
        
        # Check for multiple cells selected
        if isinstance(cells, List):
            move = Move(self.currMove)
            for cell in cells:
                if isinstance(cell, tuple):
                    cell = self.getCell(cell[0], cell[1])
                if isinstance(numbers, List):
                    for number in numbers:
                        if not cell.fixed and not cell.filled and number in cell.candidates:
                            move.addChange(cell, "removeCandidate", number)
                            cell.removeCandidate(number)
                else:
                    if not cell.fixed and not cell.filled and numbers in cell.candidates:
                            move.addChange(cell, "removeCandidate", numbers)
                            cell.removeCandidate(numbers)
            self.currMove = move
            return
        else:
            # Single cell
            if isinstance(cells, tuple):
                cells = self.getCell(cells[0], cells[1])
            if isinstance(numbers, List):
                    for number in numbers:
                        if not cells.fixed and not cells.filled and number in cells.candidates:
                            move.addChange(cells, "removeCandidate", number)
                            cells.removeCandidate(number)
            else:
                if not cells.fixed and not cells.filled and numbers in cells.candidates:
                        move.addChange(cells, "removeCandidate", numbers)
                        cells.removeCandidate(numbers)
            self.currMove = move
                
    def addCandidate(self, cells, number: int) -> None:
        """Adds a candidate to Cell

        Args:
            cells (Cell or (int, int) or List[Cell, (int,int)]): Cell object, tuple (row, col), or List of Cells and tuples
            number (int): candidate
        """
        # Check for multiple cells selected
        if isinstance(cells, List):
            move = Move(self.currMove)
            for cell in cells:
                if isinstance(cell, tuple):
                    cell = self.getCell(cell[0], cell[1])
                if not cell.fixed and not cell.filled and number not in cell.candidates:
                    move.addChange(cell, "addCandidate", number)
                    cell.addCandidate(number)
            self.currMove = move
            return
        else:
            # Single cell
            if isinstance(cells, tuple):
                cells = self.getCell(cells[0], cells[1])
            if not cells.fixed and not cells.filled and number not in cells.candidates:
                move = Move(self.currMove)
                move.addChange(cells, "addCandidate", number)
                cells.addCandidate(number)
                self.currMove = move
    
    def getRow(self, row: int) -> List[Cell]:
        """Gets row of Cells

        Args:
            row (int): row

        Returns:
            List[Cell]: list of Cells in row
        """
        return self.board[row-1]
    
    def getCol(self, col: int) -> List[Cell]:
        """Gets column of Cells

        Args:
            col (int): column

        Returns:
            List[Cell]: list of Cells in column
        """
        cells: List[Cell] = []
        for row in self.board:
            cells.append(row[col-1])
        return cells
    
    def getBox(self, box: int) -> List[Cell]:
        """Gets box of Cells

        Args:
            box (int): box

        Returns:
            List[Cell]: list of Cells in box
        """
        cells: List[Cell] = []
        rows = ((box-1)//3) * 3 + 1
        cols = ((box-1) % 3) * 3 + 1
        for row in range(rows, rows+3):
            for col in range(cols, cols+3):
                cells.append(self.getCell(row,col))
        return cells
    
    def getRelated(self, cell) -> List[Cell]:
        """Gets all related Cells to a given Cell, not including given Cell

        Args:
            cell (Cell or (int, int)): Cell object or tuple (row, col)

        Returns:
            List[Cell]: list of related Cells
        """
        
        if isinstance(cell, tuple):
            cell = self.getCell(cell[0],cell[1])
        
        cells: List[Cell] = []
        cells.extend(self.getBox(cell.box))
        cells.extend(self.getRow(cell.row))
        cells.extend(self.getCol(cell.col))
        cells.remove(cell)
        
        cells = sorted(list(set(cells)))
        return cells
    
    def getRelatedUnfilled(self, cell) -> List[Cell]:
        """Gets all related Cells that are unfilled to a given Cell

        Args:
            cell (Cell or (int, int)): Cell object or tuple (row, col)

        Returns:
            List[Cell]: list of unfilled related Cells
        """
        related = self.getRelated(cell)
        return [cells for cells in related if cells.filled is False]
    
    def getRelatedFilled(self, cell) -> List[Cell]:
        """Gets all related Cells that are filled to a given Cell

        Args:
            cell (Cell or (int, int)): Cell object or tuple (row, col)

        Returns:
            List[Cell]: list of filled related Cells
        """
        related = self.getRelated(cell)
        return [cells for cells in related if cells.filled is True]
    
    def show(self) -> None:
        """Prints Sudoku board representation
        """
        for row, cells in enumerate(self.board):
            string = ""
            for col, cell in enumerate(cells):
                string += str(cell)
                if (col == 2 or col == 5):
                    string += "|"
                else:
                    string += " "
            print(string)
            if (row == 2 or row == 5):
                print("-----+-----+-----")
        print("")
    
    def isValid(self) -> bool:
        """Checks if current Sudoku board is valid
        
        A board is valid if in each row/col/box the numbers 1-9 do not repeat

        Returns:
            bool: if valid
        """
        filled = [cell for row in self.board for cell in row if cell.filled is True]
        for cell in filled:
            relatedCells = self.getRelatedFilled(cell)
            relatedCells.remove(cell)
            for related in relatedCells:
                if cell.number == related.number:
                    return False
        return True
        
    def undo(self) -> None:
        """Undos the last move made
        """
        
        if self.currMove == self.startMove:
            return
        
        move = self.currMove
        self.currMove = self.currMove.prev
        
        for change in move.changes:
            cell: Cell = change[0]
            changeType = change[1]
            number = change[2]
            if changeType == "fill":
                # Change cell number back to prev and fix the filled bool
                cell.number = number[0]
                if number[0] == 0:
                    cell.filled = False
            elif changeType == "addCandidate":
                # Remove candidate
                cell.removeCandidate(number)
            elif changeType == "removeCandidate":
                # Add candidate
                cell.addCandidate(number)
            elif changeType == "empty":
                # Fill cell
                cell.fill(number[0])
            elif changeType == "clear":
                # Set candidates
                cell.candidates = number[0]
    
    def redo(self) -> None:
        """Redos the last undone move
        
        Undos the undo
        """
        
        if self.currMove.next == None:
            return
        
        move = self.currMove.next
        self.currMove = self.currMove.next

        for change in move.changes:
            cell: Cell = change[0]
            changeType = change[1]
            number = change[2]
            if changeType == "fill":
                # Change cell number back to new and fix the filled bool
                cell.number = number[1]
                cell.filled = True
            elif changeType == "addCandidate":
                # Add candidate
                cell.addCandidate(number)
            elif changeType == "removeCandidate":
                # Remove candidate
                cell.removeCandidate(number)
            elif changeType == "empty":
                # Empty cell
                cell.empty()
            elif changeType == "clear":
                # Clear cell
                cell.clear()
                
    def copy(self):
        """Creates deep copy of Sudoku object

        Returns:
            Sudoku: deep copy of Sudoku object, with Cells copied as well
        """
        newBoard: Sudoku = Sudoku()
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                newCell: Cell = newBoard.getCell(i+1,j+1)
                newCell.number = cell.number
                newCell.filled = cell.filled
                newCell.fixed = cell.fixed
        return newBoard
    
    def setAllCandidates(self) -> None:
        """Sets all candidates for all valid cells using only basic Sudoku rules
        """
        emptyCells = [cell for row in self.board for cell in row if cell.filled is False]
        for cell in emptyCells:
            cell.clear()
            relatedFilledCells = self.getRelatedFilled(cell)
            cell.candidates = [1,2,3,4,5,6,7,8,9]
            for filledCell in relatedFilledCells:
                cell.removeCandidate(filledCell.number)
    
    def printMoves(self):
        move = self.startMove
        while move.next != None:
            move = move.next
            move.show() 
            print()
    
    def __eq__(self, other):
        equal = True
        for row in range(1,10):
            for col in range(1,10):
                equal = equal and self.getCell(row,col).number == other.getCell(row,col).number
        return equal
    
def main() -> None:
    date = "puzzles/8-22-24/"
    boards = ["easy", "med", "hard"]
    sols = ["easysol", "medsol", "hardsol"]
    
    sudoku = Sudoku(date+boards[0])
    sudoku.setAllCandidates()
    
    
    sudoku.show()
    for row in sudoku.board:
        for cell in row:
            if cell.filled is False:
                print(f'({cell.row}, {cell.col}): {cell.candidates}')

if __name__ == "__main__":
    main()