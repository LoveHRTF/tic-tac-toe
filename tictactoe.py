import numpy as np
import copy
import random
import vertex
from Wrapper import generate_next_vertex
from Wrapper import which_computer
from Wrapper import computer_move
from Wrapper import computer_move_simple


# Main function for BFS algorithm
def tic_tic_toc_BFS():
    """ This Main function was for semi-Breadth-first search algorithm"""

    print("Starting Game w/ Empty Board...")
    print(np.array([[0,0,0], [0,0,0], [0,0,0]]))
    print("")

    """ Randomlly Flip a coin"""
    flip_coin = random.uniform(0, 1)


    if flip_coin > 0.5:
        human_action = 1
        """ Human Start First """
        print("You move first!")
        move = input("Enter Move: ")
        move = np.array(move.split(','), dtype=int)
        initial_matrix = np.array([[0,0,0],\
                                   [0,0,0],\
                                   [0,0,0]])
        initial_matrix[move[0]][move[1]] = 1
        print("You Moved!")
        print(initial_matrix)

    else:
        human_action = -1
        """ Computer Starts First"""
        print("Computer move first!")
        tic_tac_toc = vertex.Vertex(np.array([[0,0,0],\
                                       [0,0,0],\
                                       [0,0,0]]))
        tic_tac_toc = computer_move(tic_tac_toc)
        print(tic_tac_toc.get_vertex())
        print("")
        print("Computer Moved! Your Turn!")

        """ Human Start Second """

        while(1):
            move = input("Enter Move: ")
            move = np.array(move.split(','), dtype=int)

            initial_matrix = tic_tac_toc.get_vertex()
            if initial_matrix[move[0]][move[1]] != 0:
                print("Move invalid! Re-enter!")
            else:
                initial_matrix[move[0]][move[1]] = -1
                print("You Moved!")
                print(initial_matrix)
                break


    while(1):
        tic_tac_toc = vertex.Vertex(initial_matrix)
        if tic_tac_toc.get_status() == "tie" \
        or tic_tac_toc.get_status() == "X wins" \
        or tic_tac_toc.get_status() == "O wins":
            print("Game Over! ", tic_tac_toc.get_status())
            break

        print("")
        print("Computer's Turn!")
        tic_tac_toc = computer_move(tic_tac_toc)
        print(tic_tac_toc.get_vertex())
        if tic_tac_toc.get_status() == "tie" \
        or tic_tac_toc.get_status() == "X wins" \
        or tic_tac_toc.get_status() == "O wins":
            print("Game Over! ", tic_tac_toc.get_status())
            break
        print("")
        print("Computer Moved! Your Turn!")


        while(1):
            move = input("Enter Move: ")
            move = np.array(move.split(','), dtype=int)

            initial_matrix = tic_tac_toc.get_vertex()
            if initial_matrix[move[0]][move[1]] != 0:
                print("Move invalid! Re-enter!")
            else:
                initial_matrix[move[0]][move[1]] = human_action
                print("You Moved!")
                print(initial_matrix)
                break
        print("Status: ", tic_tac_toc.get_status())
    pass


# Main function for Brute Force probability approach
def tic_tic_toc_BruteForce():
    """ This Main function was for Brute-Force probability"""

    print("Starting Game w/ Empty Board...")
    print(np.array([[0,0,0], [0,0,0], [0,0,0]]))
    print("")

    """ Randomlly Flip a coin"""
    flip_coin = random.uniform(0, 1)


    if flip_coin > 0.5:
        human_action = 1
        """ Human Start First """
        print("You move first!")
        move = input("Enter Move: ")
        move = np.array(move.split(','), dtype=int)
        initial_matrix = np.array([[0,0,0],\
                                   [0,0,0],\
                                   [0,0,0]])
        initial_matrix[move[0]][move[1]] = 1
        print("You Moved!")
        print(initial_matrix)

    else:
        human_action = -1
        """ Computer Starts First"""
        print("Computer move first! Computing...")
        print("Computing... This may take a while...")
        tic_tac_toc = vertex.Vertex(np.array([[0,0,0],\
                                       [0,0,0],\
                                       [0,0,0]]))
        tic_tac_toc = computer_move_simple(tic_tac_toc)
        print(tic_tac_toc.get_vertex())
        print("")
        print("Computer Moved! Your Turn!")

        """ Human Start Second """

        while(1):
            move = input("Enter Move: ")
            move = np.array(move.split(','), dtype=int)

            initial_matrix = tic_tac_toc.get_vertex()
            if initial_matrix[move[0]][move[1]] != 0:
                print("Move invalid! Re-enter!")
            else:
                initial_matrix[move[0]][move[1]] = -1
                print("You Moved!")
                print(initial_matrix)
                break

    while(1):
        tic_tac_toc = vertex.Vertex(initial_matrix)
        if tic_tac_toc.get_status() == "tie" \
        or tic_tac_toc.get_status() == "X wins" \
        or tic_tac_toc.get_status() == "O wins":
            print("Game Over! ", tic_tac_toc.get_status())
            break

        print("")
        print("Computer's Turn!")
        print("Computing... This may take a while...")
        tic_tac_toc = computer_move_simple(tic_tac_toc)
        print(tic_tac_toc.get_vertex())
        if tic_tac_toc.get_status() == "tie" \
        or tic_tac_toc.get_status() == "X wins" \
        or tic_tac_toc.get_status() == "O wins":
            print("Game Over! ", tic_tac_toc.get_status())
            break
        print("")
        print("Computer Moved! Your Turn!")

        while(1):
            move = input("Enter Move: ")
            move = np.array(move.split(','), dtype=int)

            initial_matrix = tic_tac_toc.get_vertex()
            if initial_matrix[move[0]][move[1]] != 0:
                print("Move invalid! Re-enter!")
            else:
                initial_matrix[move[0]][move[1]] = human_action
                print("You Moved!")
                print(initial_matrix)

                break
    pass
