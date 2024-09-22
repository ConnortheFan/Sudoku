from typing import List
from Cell import Cell


class Move:
    """
    A class used to represent a single move in Sudoku
    
    Also functions as a doubly linked list
        
    A Move will have each change as a tuple in format (Cell, change type, number)
    
    Cell represent which cell is being changed
    
    Change type represents what kind of change is made like "fill", "addCandidate", "removeCandidate"
    
    Number represents which number is being changed
    """
    
    def __init__(self, prevMove = None) -> None:
        self.changes = []
        self.prev: Move = prevMove
        self.next = None
        self.desc: str = ""
        if prevMove != None:
            prevMove.next = self
    
    def addChange(self, cell: Cell, changeType: str, number) -> None:
        """Add change to the Move

        Args:
            cell (Cell): Cell being affected
            changeType (str): "fill", "removeCandidate", "addCandidate", "empty", "clear"
            number (int or List[int]): number(s) being affected. If multiple numbers given, use format [prev, new]
        """
        self.changes.append((cell, changeType, number))
        
    def setDesc(self, description: str) -> None:
        """Adds description to the move, used for the solver.

        Args:
            description (str): Description of move
        """
        self.desc = description
        
    def show(self):
        """Prints move
        """
        
        for change in self.changes:
            print(f"({change[0].row}, {change[0].col}): {change[1]} {change[2]}")