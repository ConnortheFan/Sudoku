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