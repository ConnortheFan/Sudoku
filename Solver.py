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
        
    def fill(self, cell, number: int) -> None:
        """Similar to Sudoku fill function, but removes cell from emptyCells list

        Args:
            cell (Cell or (int, int)): Either the Cell object or (row, col) tuple
            number (int): number
        """
        super().fill(cell, number)
        self.emptyCells.remove(cell)
        
        
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
                return True
        return False
        
    def clothedSingle(self) -> bool:
        """Finds Clothed Singles and makes first move

        If no Clothed Singles found, returns False

        Returns:
            bool: if any changes were made
        """
        for cell in self.emptyCells:
            # Need to check against row, col, and box
            relatedRow = [related for related in self.getRow(cell.row) if related.filled is False]
            relatedRow.remove(cell)
            relatedRow = list(set([candidates for cells in relatedRow for candidates in cells.candidates]))
            
            relatedCol = [related for related in self.getCol(cell.col) if related.filled is False]
            relatedCol.remove(cell)
            relatedCol = list(set([candidates for cells in relatedCol for candidates in cells.candidates]))

            relatedBox = [related for related in self.getBox(cell.box) if related.filled is False]
            relatedBox.remove(cell)
            relatedBox = list(set([candidates for cells in relatedBox for candidates in cells.candidates]))
            
            # print(f'{cell.row}, {cell.col}: {cell.candidates}')
            # print(f'     row: {relatedRow}')
            # print(f'     col: {relatedCol}')
            # print(f'     box: {relatedBox}')

            for candidate in cell.candidates:
                if candidate not in relatedRow:
                    self.fill(cell, candidate)
                    self.currMove.setDesc("Clothed Single (Row)")
                    return True
                if candidate not in relatedCol:
                    self.fill(cell, candidate)
                    self.currMove.setDesc("Clothed Single (Col)")
                    return True
                if candidate not in relatedBox:
                    self.fill(cell, candidate)
                    self.currMove.setDesc("Clothed Single (Box)")
                    return True
        return False
       
    def twins(self) -> bool:
        """Finds twins and removes candidates
        
        If no change, returns false

        Returns:
            bool: If any changes were made
        """
        # Go through 27 sets of 9 cells
        # Rows, Cols, and Boxes
        cellgroups: List[List[Cell]] = []
        for i in range(1,10):
            cellgroups.append(self.getRow(i))
            cellgroups.append(self.getCol(i))
            cellgroups.append(self.getBox(i))
        for cellgroup in cellgroups:
            emptyCells = [cell for cell in cellgroup if cell.filled is False]
            possibleTwins = [cell for cell in emptyCells if len(cell.candidates) == 2]
            if len(possibleTwins) < 2:
                continue
            for i, possibleTwin in enumerate(possibleTwins):
                for j in range(i+1, len(possibleTwins)):
                    if possibleTwin.candidates == possibleTwins[j].candidates:
                        # These are twins
                        twin1 = possibleTwin
                        twin2 = possibleTwins[j]
                        emptyCells.remove(twin1)
                        emptyCells.remove(twin2)
                        for emptyCell in emptyCells:
                            if twin1.candidates[0] in emptyCell.candidates or twin1.candidates[1] in emptyCell.candidates:       
                                self.removeCandidate(emptyCells, twin1.candidates)
                                self.currMove.setDesc(f"Twins at ({twin1.row}, {twin1.col}) ({twin2.row}, {twin2.col})")
                                return True
        return False 
    
    def intersect(self) -> bool:
        """Finds intersect between row/col and box candidates and adjusts accordingly

        Returns:
            bool: If any changes were made
        """
        # Box eliminates Row/Col
        for i in range(1,10):
            boxCells = [cell for cell in self.getBox(i) if cell.filled is False]
            boxCandidates = list(set([candidate for cell in boxCells for candidate in cell.candidates]))
            for boxCandidate in boxCandidates:
                possibleIntersectCells = [boxCell for boxCell in boxCells if boxCandidate in boxCell.candidates]
                if len(possibleIntersectCells) > 3 or len(possibleIntersectCells) < 1:
                    continue
                # Check Row
                row = possibleIntersectCells[0].row
                sameRow = True
                for possibleIntersectCell in possibleIntersectCells:
                    if row != possibleIntersectCell.row:
                        sameRow = False
                if sameRow:
                    # Check for changes
                    otherRowCells = [cell for cell in self.getRow(row) if cell not in possibleIntersectCells]
                    for otherRowCell in otherRowCells:
                        if boxCandidate in otherRowCell.candidates:
                            self.removeCandidate(otherRowCells, boxCandidate)
                            cellCoords = []
                            for possibleIntersectCell in possibleIntersectCells:
                                cellCoords.append((possibleIntersectCell.row, possibleIntersectCell.col))
                            self.currMove.setDesc(f"Box {i} intersect row {row} on candidate {boxCandidate} in cells {cellCoords}")
                            return True
                # Check Col
                col = possibleIntersectCells[0].col
                sameCol = True
                for possibleIntersectCell in possibleIntersectCells:
                    if col != possibleIntersectCell.col:
                        sameCol = False
                if sameCol:
                    # Check for changes
                    otherColCells = [cell for cell in self.getCol(col) if cell not in possibleIntersectCells]
                    for otherColCell in otherColCells:
                        if boxCandidate in otherColCell.candidates:
                            self.removeCandidate(otherColCells, boxCandidate)
                            cellCoords = []
                            for possibleIntersectCell in possibleIntersectCells:
                                cellCoords.append((possibleIntersectCell.row, possibleIntersectCell.col))
                            self.currMove.setDesc(f"Box {i} intersect col {col} on candidate {boxCandidate} in cells {cellCoords}")
                            return True
        
        # Row eliminates Box
        for i in range(1, 10):
            rowCells = [cell for cell in self.getRow(i) if cell.filled is False]
            rowCandidates = list(set([candidate for cell in rowCells for candidate in cell.candidates]))
            for rowCandidate in rowCandidates:
                possibleIntersectCells = [rowCell for rowCell in rowCells if rowCandidate in rowCell.candidates]
                if len(possibleIntersectCells) > 3 or len(possibleIntersectCells) < 1:
                    continue
                # Check Box
                box = possibleIntersectCells[0].box
                sameBox = True
                for possibleIntersectCell in possibleIntersectCells:
                    if box != possibleIntersectCell.box:
                        sameBox = False
                if sameBox:
                    # Check for changes
                    otherBoxCells = [cell for cell in self.getBox(box) if cell not in possibleIntersectCells]
                    for otherBoxCell in otherBoxCells:
                        if rowCandidate in otherBoxCell.candidates:
                            self.removeCandidate(otherBoxCells, rowCandidate)
                            cellCoords = []
                            for possibleIntersectCell in possibleIntersectCells:
                                cellCoords.append((possibleIntersectCell.row, possibleIntersectCell.col))
                            self.currMove.setDesc(f"Row {i} intersect box {box} on candidate {rowCandidate} in cells {cellCoords}")
                            return True
        
        # Col eliminates Box
        for i in range(1, 10):
            colCells = [cell for cell in self.getCol(i) if cell.filled is False]
            colCandidates = list(set([candidate for cell in colCells for candidate in cell.candidates]))
            for colCandidate in colCandidates:
                possibleIntersectCells = [colCell for colCell in colCells if colCandidate in colCell.candidates]
                if len(possibleIntersectCells) > 3 or len(possibleIntersectCells) < 1:
                    continue
                # Check Box
                box = possibleIntersectCells[0].box
                sameBox = True
                for possibleIntersectCell in possibleIntersectCells:
                    if box != possibleIntersectCell.box:
                        sameBox = False
                if sameBox:
                    # Check for changes
                    otherBoxCells = [cell for cell in self.getBox(box) if cell not in possibleIntersectCells]
                    for otherBoxCell in otherBoxCells:
                        if colCandidate in otherBoxCell.candidates:
                            self.removeCandidate(otherBoxCells, colCandidate)
                            cellCoords = []
                            for possibleIntersectCell in possibleIntersectCells:
                                cellCoords.append((possibleIntersectCell.row, possibleIntersectCell.col))
                            self.currMove.setDesc(f"Col {i} intersect box {box} on candidate {rowCandidate} in cells {cellCoords}")
                            return True
        return False

def test():
    board = "puzzles/9-27-24/med"
    s = Sudoku(board)
    solver = Solver(s)
    change = True
    while change:
        change = solver.nakedSingle()
        if not change:
            change = solver.clothedSingle()
        if not change:
            change = solver.twins()
        if not change:
            change = solver.intersect()
    
    
    solver.printMoves()
    s.show()
    solver.show()
    return

def main() -> None:
    dates = ["8-21-24/", "8-22-24/", "9-22-24/"]
    boards = ["easy", "med", "hard"]
    
    # for date in dates:
    #     for board in boards:
    #         print(date+board)   
    #         s = Sudoku("puzzles/" + date + board)
    #         sol = Sudoku("puzzles/" + date + board + "sol")
    #         solver = Solver(s)
            
    #         change = True
    #         while change:    
    #             change = solver.twins()
            
                
    #         solver.printMoves()
    #         print("Original")
    #         s.show()
    #         print("Solver Result")
    #         solver.show()
    #         print("Solution")
    #         sol.show()
    
    
    name = "puzzles/9-27-24/med"
    s = Sudoku(name)
    solver = Solver(s)    
    solver.show()
    change = True
    while change:    
        change = solver.nakedSingle()
        if not change:
            change = solver.clothedSingle()
        if not change:
            change = solver.twins()
    solver.printMoves()
    solver.show()
    solution = ""
    for row in solver.board:
        for j, cell in enumerate(row):
            solution += f'{cell.number}'
            if j == 8:
                solution += f'\n'
            else:
                solution += ' '
    print(solution)
    f = open(name+'sol', 'w')
    f.write(solution)
    f.close()
    
if __name__ == "__main__":
    test()