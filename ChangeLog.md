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