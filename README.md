# Sudoku Solver Script

A python script for solving sudokus.
I wanted to make a script that can solve a sudoku puzzle with the help of a recursion function.

## How to use

To use the script correctly you have to put the sudoku you want to solve as a .txt file in the same directory as the script. The file should contain the sudoku where empty spaces are represented as a 0 and each row is separated into a new line, like this:

```
043080007
057090600
000040108
462038501
010704029
000001063
601073042
070406305
530829706
```

Then run the script with `python sudokusolver.py` and enter the filename when prompted and press enter.
When the script is done you should have the solved sudoku rendered into the `out.txt` file in the same directory.

```
╔═╤═╤═╦═╤═╤═╦═╤═╤═╗
║1│4│3║6│8│5║2│9│7║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║8│5│7║1│9│2║6│3│4║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║9│2│6║3│4│7║1│5│8║
╠═╪═╪═╬═╪═╪═╬═╪═╪═╣
║4│6│2║9│3│8║5│7│1║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║3│1│5║7│6│4║8│2│9║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║7│9│8║2│5│1║4│6│3║
╠═╪═╪═╬═╪═╪═╬═╪═╪═╣
║6│8│1║5│7│3║9│4│2║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║2│7│9║4│1│6║3│8│5║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║5│3│4║8│2│9║7│1│6║
╚═╧═╧═╩═╧═╧═╩═╧═╧═╝
```

If you only want to use the render function to render an unsolved sudoku into the `out.txt` file, use the `nosolve` (not case sensitive) argument when you run the script like this: `python sudokusolver.py nosolve`.

```
╔═╤═╤═╦═╤═╤═╦═╤═╤═╗
║0│4│3║0│8│0║0│0│7║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║0│5│7║0│9│0║6│0│0║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║0│0│0║0│4│0║1│0│8║
╠═╪═╪═╬═╪═╪═╬═╪═╪═╣
║4│6│2║0│3│8║5│0│1║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║0│1│0║7│0│4║0│2│9║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║0│0│0║0│0│1║0│6│3║
╠═╪═╪═╬═╪═╪═╬═╪═╪═╣
║6│0│1║0│7│3║0│4│2║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║0│7│0║4│0│6║3│0│5║
╟─┼─┼─╫─┼─┼─╫─┼─┼─╢
║5│3│0║8│2│9║7│0│6║
╚═╧═╧═╩═╧═╧═╩═╧═╧═╝
```
