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

    def getCell(self, row: int, col: int) -> Cell:
        return self.board[row-1][col-1]
    
    def fill(self, row: int, col: int, number: int) -> None:
        """Fills Cell with number

        Args:
            row (int): row
            col (int): column
            number (int): number
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed:
            cell.fill(number)
    
    def empty(self, row: int, col: int) -> None:
        """Empty Cell by removing filled number

        Args:
            row (int): row
            col (int): column
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed and cell.filled:
            cell.empty()
    
    def clear(self, row: int, col: int) -> None:
        """Clear all data in a Cell unless its fixed

        Args:
            row (int): row
            col (int): column
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed:
            cell.clear()
    
    def removeCandidate(self, row: int, col: int, number: int) -> None:
        """Removes candidate from Cell

        Args:
            row (int): row
            col (int): column
            number (int): candidate
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed and not cell.filled:
            cell.removeCandidate(number)
    
    def addCandidate(self, row: int, col: int, number: int) -> None:
        """Adds a candidate to Cell

        Args:
            row (int): row
            col (int): column
            number (int): candidate
        """
        cell: Cell = self.getCell(row,col)
        if not cell.fixed and not cell.filled:
            cell.addCandidate(number)
    
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

        Returns:
            bool: if valid
        """
        
    
def main() -> None:
    board = Sudoku()
    board.show()
    
    board.fill(5,5,5)
    board.fill(2,3,9)
    board.show()
    
    board.fill(5,5,9)
    board.empty(2,3)
    board.show()
    
    board.addCandidate(1,2,2)
    board.addCandidate(1,2,1)
    print(board.getRow(1))
    print(board.getCell(1,2).candidates)
    board.addCandidate(1,2,2)
    print(board.getCell(1,2).candidates)
    board.clear(1,2)
    print(board.getCell(1,2).candidates)

    board.fill(4,4,3)
    board.fill(5,6,6)
    print(board.getBox(5))
    board.show()
    
    for i in range(1,10):
        board.fill(i,5,i)
        board.fill(5,i,i)
    board.fill(4,4,1)
    board.fill(4,5,2)
    board.fill(4,6,3)
    board.fill(5,4,4)
    board.fill(5,5,5)
    board.fill(5,6,6)
    board.fill(6,4,7)
    board.fill(6,5,8)
    board.fill(6,6,9)
    board.show()
    print(board.getRelated(5,5))
    
if __name__ == "__main__":
    main()