import numpy as np
import copy
import random
import vertex

# Helper functions
def generate_next_vertex(vertex_class, player):
    """ Input the vertex class """
    this_vertex = vertex_class.get_vertex()
    empty_spots = np.where(this_vertex == 0)        # Get the position of all empty spots remaining on the vertex
    child_vertex_list = []

    for idx in range(0, len(empty_spots[0])):
        this_vertex = vertex_class.get_vertex()
        child_vertex_tmp = copy.copy(this_vertex)   # Copy by content, not reference (python default cp by reference)

        """ Assign new value depending on round, human or computer"""
        if player == 1:
            child_vertex_tmp[empty_spots[0][idx]][empty_spots[1][idx]] = 1      # Generate next vertex by X moves
        elif player == -1:
            child_vertex_tmp[empty_spots[0][idx]][empty_spots[1][idx]] = -1     # Generate next vertex by O moves

        """ Create new vertex class """
        child_vertex = vertex.Vertex(child_vertex_tmp)
        child_vertex_list.append(child_vertex)      # Append vertexes as a list

        """ Set as children to original vertex class """
        vertex_class.set_children(child_vertex)

        """ Return original vertex with added children, and generated possible movement list"""
    return vertex_class, child_vertex_list


def which_computer(vertex):
    """ Find which one is computer and place 1 or -1 next """
    this_vertex_array = vertex.get_vertex()
    this_vertex = copy.copy(this_vertex_array)
    number_x = len((np.where(this_vertex == 1)[0]))
    number_o = len((np.where(this_vertex == -1)[0]))

    """ Assuming x always moves first"""
    if number_x <= number_o:
        next_move = 1
        human = -1
    else:
        next_move = -1
        human = 1

    return next_move, human

# This algorithm was to compute the best optimized move instead of the highest possible win rate move
# It the performance was significantly better than the brute-force in terms of both computational speed
# and result. It uses a semi-Breadth-first search algorithm.

# This algorithm does not lose
def computer_move(vertex):
    """ Find which is computer"""
    computer, human = which_computer(vertex)

    """ Generate first new computer move """
    vertex, child_obj_list = generate_next_vertex(vertex, computer)  # Final output in this step

    for itm in child_obj_list:
        """ One single move wins the game """
        if (itm.get_status() == "X wins" and computer == 1) or (itm.get_status() == "O wins" and computer == -1):
            next_move_result = itm
            print("Return #1")
            return itm

    """ Create list object, each branch has own tree"""
    vertex_tree_lists = [[] for i in range(len(child_obj_list))]
    idx = 0
    for item in vertex_tree_lists:
        item.append(child_obj_list[idx])
        idx = idx + 1

    """ Search for all solutions"""
    iters = 0
    while (1):
        # Check for human movement, delete branch that may cause the game to be lost #
        """ For each list in the vertex tree"""
        branch_idx = 0
        branch_to_select_Human = 99
        branch_to_delete = []
        for branch in vertex_tree_lists:
            """ Go though every node in the tree branch"""
            for node in branch:
                """ Find the children nodes"""
                node, children_nodes = generate_next_vertex(node, human)
                """ Exam each child, if it result the computer to lose, set flag to delete"""
                for child in children_nodes:
                    if (child.get_status() == "X wins" and human == 1) \
                            or (child.get_status() == "O wins" and human == -1):
                        if branch_idx not in branch_to_delete:
                            branch_to_delete.append(branch_idx)
                            """ Preventing everything get deleted"""
                            if len(branch_to_delete) == len(vertex_tree_lists):
                                branch_to_select_Human = branch_idx

            """ Append the children under this branch"""
            for child_node in children_nodes:
                branch.append(child_node)
            branch_idx = branch_idx + 1

        """ Output the only branch"""
        if branch_to_select_Human != 99:
            print("Return #2")
            return vertex_tree_lists[branch_to_select_Human][0]

        """ Delete the target branch"""
        branch_to_delete.reverse()
        for branch_idx in branch_to_delete:
            del vertex_tree_lists[branch_idx]

        """ Check remaining branches. Output when only one left"""
        if len(vertex_tree_lists) == 1:
            print("Return #3")
            return vertex_tree_lists[0][0]

        # Check for computer movement, select branch that may cause the game to be won #
        branch_idx = 0
        branch_to_select = []
        """ For each list in the vertex"""
        for branch in vertex_tree_lists:
            """ Go though every node in the tree branch"""
            for node in branch:
                """ Find the children nodes"""
                node, children_nodes = generate_next_vertex(node, computer)
                """ Exam each child, if it result the computer to won, set flag to pull out"""
                for child in children_nodes:
                    if (child.get_status() == "X wins" and computer == 1) \
                            or (child.get_status() == "O wins" and computer == -1):
                        if branch_idx not in branch_to_select:
                            branch_to_select.append(branch_idx)
            """ Append the children under this branch"""
            for child_node in children_nodes:
                branch.append(child_node)
            branch_idx = branch_idx + 1

            """ Select the target branch when branch to select list is not empty"""
            if not not branch_to_select:
                print("Return #4")
                return vertex_tree_lists[branch_to_select[0]][0]

        iters = iters + 1

        if iters >= 99:
            print("Return #5")
            return vertex_tree_lists[0][0]


# This algorithm was purely based on brute-force approach
# This algorithm takes a lot computing resource on first couple steps due to the nature of trees and 9! results
# It only count for best total probability, not fastest path for winning or prevent lost

# This algorithm always lose when played correctly. Implement only because it was required
def computer_move_simple(vertex):
    """ Find which is computer"""
    computer, human = which_computer(vertex)

    """ Generate first new computer move """
    vertex, child_obj_list = generate_next_vertex(vertex, computer)  # Final output in this step
    # child_obj_list: [child_obj, child_obj, ...]

    """ Create list object, each branch has own tree"""
    vertex_tree_lists = [[] for i in range(len(child_obj_list))]
    idx = 0
    for item in vertex_tree_lists:
        item.append(child_obj_list[idx])
        idx = idx + 1

    for _ in range(4):
        """ Fill in all branch nodes without children, with computer move"""
        for branch in vertex_tree_lists:
            new_node_list = []
            for node in branch:
                """ Only calculate when have no child"""
                if node.get_status() == "in process":
                    node, node_obj_list = generate_next_vertex(node, computer)
                    """ Append new nodes"""
                    for new_node in node_obj_list:
                        new_node_list.append(new_node)
                """ Append all new node to top branch"""
            for new_node in new_node_list:
                branch.append(new_node)

        """ Fill in all branch nodes without children, with human move"""
        for branch in vertex_tree_lists:
            new_node_list = []
            for node in branch:
                """ Only calculate when have no child"""
                if node.get_status() == "in process":
                    node, node_obj_list = generate_next_vertex(node, human)
                    """ Append new nodes"""
                    for new_node in node_obj_list:
                        new_node_list.append(new_node)
                """ Append all new node to top branch"""
            for new_node in new_node_list:
                branch.append(new_node)

    # Starting calculating win rate for each branch
    win_rate_list = []
    for branch in vertex_tree_lists:
        """ For every main branch"""
        count_X_win = 0
        count_O_win = 0
        count_tie = 0
        for node in branch:
            """ For every node in a branch"""
            if node.get_status() == "X wins":
                count_X_win += 1
            elif node.get_status() == "O wins":
                count_O_win += 1
            elif node.get_status() == "tie":
                count_tie += 1

        if computer == 1:
            win_rate = count_X_win / (count_X_win + count_O_win + count_tie)
        elif computer == -1:
            win_rate = count_O_win / (count_X_win + count_O_win + count_tie)

        win_rate_list.append(win_rate)
        index_max = np.argmax(win_rate_list)

    return vertex_tree_lists[index_max][0]
