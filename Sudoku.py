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
    
    def fill(self, row: int, col: int, number: int) -> None:
        """Fills Cell with number and makes Move

        Args:
            row (int): row
            col (int): column
            number (int): number
        """
        
        cell: Cell = self.getCell(row,col)
        if not cell.fixed:
            move = Move(self.currMove)
            move.addChange(cell, "fill", [cell.number, number])
            cell.fill(number)
            for related in self.getRelatedUnfilled(row, col):
                if number in related.candidates:
                    related.removeCandidate(number)
                    move.addChange(related, "removeCandidate", number)
            self.currMove = move
    
    def empty(self, row: int, col: int) -> None:
        """Empty Cell by removing filled number

        Args:
            row (int): row
            col (int): column
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed and cell.filled:
            move = Move(self.currMove)
            move.addChange(cell, "empty", [cell.number, 0])
            cell.empty()
            self.currMove = move
    
    def clear(self, row: int, col: int) -> None:
        """Clear all data in a Cell unless its fixed

        Args:
            row (int): row
            col (int): column
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed:
            move = Move(self.currMove)
            move.addChange(cell, "clear", [cell.candidates, []])
            cell.clear()
            self.currMove = move
    
    def removeCandidate(self, row: int, col: int, number: int) -> None:
        """Removes candidate from Cell

        Args:
            row (int): row
            col (int): column
            number (int): candidate
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed and not cell.filled and number in cell.candidates:
            
            move = Move(self.currMove)
            move.addChange(cell, "removeCandidate", number)
            cell.removeCandidate(number)
            self.currMove = move
                
    def addCandidate(self, row: int, col: int, number: int) -> None:
        """Adds a candidate to Cell

        Args:
            row (int): row
            col (int): column
            number (int): candidate
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed and not cell.filled and number not in cell.candidates:
            move = Move(self.currMove)
            move.addChange(cell, "addCandidate", number)
            cell.addCandidate(number)
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
    
    def getRelated(self, row: int, col: int) -> List[Cell]:
        """Gets all related Cells to a given Cell

        Args:
            row (int): row
            col (int): column

        Returns:
            List[Cell]: list of related Cells
        """
        cell: Cell = self.getCell(row,col)
        
        cells: List[Cell] = []
        cells.extend(self.getBox(cell.box))
        cells.extend(self.getRow(row))
        cells.extend(self.getCol(col))
        
        cells = sorted(list(set(cells)))
        return cells
    
    def getRelatedUnfilled(self, row: int, col: int) -> List[Cell]:
        """Gets all related Cells that are unfilled to a given Cell

        Args:
            row (int): row
            col (int): column

        Returns:
            List[Cell]: list of unfilled related Cells
        """
        related = self.getRelated(row, col)
        return [cell for cell in related if cell.filled is False]
    
    def getRelatedFilled(self, row: int, col: int) -> List[Cell]:
        """Gets all related Cells that are filled to a given Cell

        Args:
            row (int): row
            col (int): column

        Returns:
            List[Cell]: list of filled related Cells
        """
        related = self.getRelated(row, col)
        return [cell for cell in related if cell.filled is True]
    
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
            relatedCells = self.getRelatedFilled(cell.row, cell.col)
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
    
    def printMoves(self):
        move = self.startMove
        while move.next != None:
            move = move.next
            move.show() 
            print()
    
def main() -> None:
    date = "puzzles/8-22-24/"
    boards = ["easy", "med", "hard"]
    sols = ["easysol", "medsol", "hardsol"]
    
    sudoku = Sudoku(date+boards[0])
    sudoku.show()
    
    # Make sure no moves are made when no changes made
    sudoku.removeCandidate(5,6,1)
    sudoku.removeCandidate(1,1,5)
    sudoku.addCandidate(6,5,9)
    sudoku.clear(1,1)
    sudoku.empty(1,1)
    
    # Make sure fill works with Move
    sudoku.addCandidate(4,6,1)
    sudoku.addCandidate(4,6,2)
    sudoku.addCandidate(4,6,1)
    sudoku.removeCandidate(4,6,1)
    sudoku.empty(4,6)
    sudoku.clear(4,6)
    sudoku.addCandidate(4,6,1)
    sudoku.fill(5,6,1)
    
    print("Regular")
    sudoku.show()       
    sudoku.printMoves()
    print(sudoku.getCell(4,6).candidates)
    
     
    print("Undo")   
    sudoku.undo()
    sudoku.show()
    sudoku.printMoves()
    print(sudoku.getCell(4,6).candidates)
    
    print("Redo")
    sudoku.redo()
    sudoku.show()
    sudoku.printMoves()
    print(sudoku.getCell(4,6).candidates)

    print("Break")
    sudoku.undo()
    sudoku.addCandidate(5,6,1)
    sudoku.show()
    sudoku.printMoves()
    print(sudoku.getCell(4,6).candidates)
    print(sudoku.getCell(5,6).candidates)

    
    
if __name__ == "__main__":
    main()