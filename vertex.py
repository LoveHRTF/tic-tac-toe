import numpy as np
import copy
import random

# Class for vertex
# One vertex repersents a step in the game
class Vertex:
    def __init__(self, vertex):
        """ Initialize vertex class. Require vertex to be 3x3 numpy array"""
        self.adjacent = []
        self.vertex = vertex

    def set_children(self, vertex_class):
        return self.adjacent.append(vertex_class)

    def get_children(self):
        """ Adjacency method of vertex"""
        return self.adjacent

    def get_vertex(self):
        """ Vertex content """
        return self.vertex

    def get_status(self):
        """ Check the status for self.vertex """
        game_status = "in process"
        vertical_sum = self.vertex.sum(axis=0)
        horizontial_sum = self.vertex.sum(axis=1)
        cross_sum_A = self.vertex[0, 0] + self.vertex[1, 1] + self.vertex[2, 2]
        cross_sum_B = self.vertex[0, 2] + self.vertex[1, 1] + self.vertex[2, 0]

        """0 for processing, 1 for X win, -1 for O win, 99 for tie"""
        flag_status = 0

        # For vertical sums
        if flag_status == 0:
            for item in vertical_sum:
                if item == 3:
                    flag_status = 1
                    break
                elif item == -3:
                    flag_status = -1
                    break

        # For horizontial sums
        if flag_status == 0:
            for item in horizontial_sum:
                if item == 3:
                    flag_status = 1
                    break
                elif item == -3:
                    flag_status = -1
                    break

        # For diagonally sums
        if flag_status == 0:
            if cross_sum_A == 3 or cross_sum_B == 3:
                flag_status = 1
            elif cross_sum_A == -3 or cross_sum_B == -3:
                flag_status = -1

        # Check for tie
        flag_still_in_progress = 0
        if flag_status == 0:
            # Check if any empty position remaining, tie if none
            for rows in self.vertex:
                for elements in rows:
                    if elements == 0:
                        flag_still_in_progress = 1

        if flag_still_in_progress == 1 and flag_status == 0:
            flag_status = 0
        elif flag_still_in_progress == 0 and flag_status == 0:
            flag_status = 99

        if flag_status == 0:
            game_status = "in process"
        elif flag_status == 1:
            game_status = "X wins"
        elif flag_status == -1:
            game_status = "O wins"
        elif flag_status == 99:
            game_status = "tie"

        return game_status

