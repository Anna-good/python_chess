# python_chess
Added annotation and rollback
Implement a program that allows you to play chess on the computer. Interaction with the console (the base case). The playing field is represented as 8
text lines, plus lines with alphabetic columns (see the example in Fig. 1) and
is redrawn with every change of the playing field state. When requesting data from the user
it announces what it expects from the user (e.g., the position of the piece for the next
the target position of the chosen piece) and checks if the
(only moves that respect chess rules are allowed; it supports castling, complex rules for
rules for pawns, and checkmate is given in separate paragraphs). The program has to count
The program must count the number of moves made.
The program itself does NOT make moves: i.e. it does not try to make moves for one of the sides.
to alternately enter moves for White and Black.
Additional tasks:
Chess Notation Reference:
1. general information about chess notation for recording games:
https://ru.wikipedia.org/wiki/Шахматная_нотация
2. Full notation games: free database (to open the games you need
Registration on the resource) records of games in chess notation (full):
http://www.chessebook.com/openings.php?lan=ru&pa=pa (to get files with recordings of
You can get files with records of chess games by copying texts of your favorite games to a text file.
not to be additionally edited and saved into the file).
3. The games in reduced notation are taken from discussions at kasparovchess.crestbook.com,
e.g. from this thread: http://kasparovchess.crestbook.com/threads/8210/ (to get the
(to get the files with the notation of the games, copy the text of the games you like located on the
to the right of the block with the board into a text file.
the copied text in a text file without additional editing (in many nuances it will differ from games from
chessebook.com, it should be) and save the file).
*+Read a chess game entry from a user-selected file in
reduced notation. After reading, it should be possible to move forward and backward through the
of the game record (with a corresponding change on the field). It should be possible in
the selected position to switch from the party view mode to the normal game mode.
Test at least 20 real games from the site.
*+Realize the possibility of "rolling back" moves. Using a special command, you can
Use a special command to go back one move (or a specified number of moves) all the way to the beginning of the game.
