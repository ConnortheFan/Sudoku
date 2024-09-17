# 9/16/2024

I'm finally back to work on this. Been busy with roadtrips and housework, so couldn't access my computer or work for some time. I want to have this finished before I get back to school in like a week or so.

Changes:

* Made fill function remove candidates for all related cells
* Created Move class datastructure
    * Using a doubly linked list
* Implemented the Move class into Sudoku functions
* Made the undo() and redo() functions
* Did basic testing. Further testing might be needed later, but for now it works.

The main change here is the move class that works with the undo/redo functions. Moves are stored as a doubly linked list, which allows the redo function to work. When a new branch is made by undoing, then making a change, all moves undone are forgotten thanks to Python's built in object deletion once they no longer have any references. For now, moves are stored by classifying them via strings, which means that any changes are done manually. Hopefully I've already done all cases for this, so it should be fine. Thanks to how I needed to store multiple cell changes from the automatic candidate removal from filling, each move can store multiple changes at once. This means that I could implement candidate functions that work for multiple cells like in Logic Wiz Sudoku.

To-Do:

* Make Candidate functions for multiple cells at once
* Add screen/window to play Sudoku with working buttons (pygame)
* Make Solver

# 8/22/2024

Finally have some time to get back on finishing this project.

Changes:

* Added the 8/22/24 NTY Sudoku puzzles
* Implemented the Sudoku board init from a given file
* Began the Solver class
* Implemented the Sudoku board isValid function

To-do:

* Create a framework for the Move class
* Add an undo and redo function to Sudoku class
* Figure out how to use decorators to manage the Solver functions
* Use pygame to create a window to play Sudoku (import pygame and make a main.py file)
* Think of names for all the solver functions (gotta get creative)

# 8/21/2024

Been away for a while on vacation and just busy with personal life.

Making an update by adding the 8/21/24 NYT Sudoku puzzle to use for my tests and to show that I haven't forgotten or given up this project.

I've also added descriptions of some of the methods I plan to implement in the solver. I want this project to be educational for whoever uses it and for them to be better at Sudoku by the end of it.

Current thoughts:

* Use a decorator in the solver functions to make it easier to implement more methods in the future
* Find something to parse the puzzle files
    * I'm not sure what filetype these are since I didn't explicitly label them. Will have to see if they will work.
* The Move class will only record all changes made to the board in the previous move, like git. This way it will be easy to undo/redo
* I want to use pygame to make a window for the sudoku board, fit with a home screen, a board, a keypad, keyboard integration, hints, a free solver space, and a description area.

# 7/10/2024

Got back to work on this. 

Completed the Cell and Sudoku basic functionality, although I still need to implement making a Sudoku board from some given csv file and making the isValid() method.

The Cell file should be done since I don't anticipate needing to change anything unless necessary to work with the Move class.

I think the next steps are

1. Finish Sudoku init and isValid
2. Begin solver functionality
3. Implement the Move class and try to make an undo/redo function

# 7/3/2024

Created function outlines in the Sudoku, Cell, and Move files.

For now, I'll just focus on created a working Sudoku game and I'll later make the solver functioning.

# 7/2/2024

This is the beginning of my change log for this Sudoku project. I've had this idea last year as a 5am inspiration, but didn't get far with it, so I figured it'd be better to fully restart than continue off that repository. I'm not fully sure what standards there are for change logs, but I'll do my best to record my thoughts, intentions, and actual changes/functionality as I progress. If I've somehow done this extremely off-standard and I learn of this, I'll probably leave this be as a reminder of my growth.

I intend to make this eventually become an app/.exe file that makes a popup window on your computer so you can input your own Sudoku to have it solve it. I'll also try to include some game functionality, (i.e. levels with varying difficulty), but it won't be too extensive. Much of the levels will be from Sudokus I've taken from various sources (the daily NYT Sudoku, random Sudoku apps, etc). I'll try my best to properly say the source since I'm not exactly sure if there are Sudoku copyright laws or something. 

The main difficulty I expect in this will be from programming the solver since I'll only be implementing solver methods that I'm familiar with, not methods purposefully found off the internet. I may have also made up some of the names or taken them from Youtube videos (Cracking the Cryptic). These methods include the Naked Single, Clothed Single, Twins/Triplets/..., Swordfish, and Brute Force (so there will always be a solution).