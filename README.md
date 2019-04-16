# tic-tac-toe
Simple tic tac toe game by using Breadth-First-Search algorithm

# Starting the Game
$ python3 play.py

# User Input
Matrix index from 0,0 to 1,1

# Known Issue
When utilizing BFS, algorithm should return next step when:
1: All losing branches were dropped, and only one in process branch remaining
2: Only one winning branch found at same layer

Current algorithm returns the first branch when multiple winning branch exists at same layer. Therefore, may result in a computer lose situation. Ideally, computer will never lose
