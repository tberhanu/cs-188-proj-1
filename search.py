
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    s = util.Stack()
    visited_nodes = set()
    start = problem.getStartState()
    visited_nodes.add(start)
    for neighbor in problem.getSuccessors(start):
        s.push((neighbor[0], neighbor[1], [neighbor[1]]))
    while s.isEmpty() == False:
        curr = s.pop()
        if curr[0] not in visited_nodes:
            visited_nodes.add(curr[0])
            if problem.isGoalState(curr[0]):
                return curr[2]
            else:
                for neighbor in problem.getSuccessors(curr[0]):
                    if neighbor[0] not in visited_nodes:
                        updated = curr[2] + [neighbor[1]]
                        s.push((neighbor[0], neighbor[1], updated))
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    s = util.Queue()
    visited_nodes = set()
    start = problem.getStartState()
    visited_nodes.add(start)
    for neighbor in problem.getSuccessors(start):
        s.push((neighbor[0], neighbor[1], [neighbor[1]]))
    while s.isEmpty() == False:
        curr = s.pop()
        if curr[0] not in visited_nodes:
            visited_nodes.add(curr[0])
            if problem.isGoalState(curr[0]):
                return curr[2]
            else:
                for neighbor in problem.getSuccessors(curr[0]):
                    if neighbor[0] not in visited_nodes:
                        updated = curr[2] + [neighbor[1]]
                        s.push((neighbor[0], neighbor[1], updated))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    s = util.PriorityQueue()
    visited_nodes = set()
    dist = {}
    start = problem.getStartState()
    dist[start] = 0
    s.push((start, None, []), 0)
    while s.isEmpty() == False:
        curr = s.pop()
        if problem.isGoalState(curr[0]):
            return curr[2]
        if curr[0] not in visited_nodes:
            visited_nodes.add(curr[0])
            for neighbor in problem.getSuccessors(curr[0]):
                if neighbor[0] not in visited_nodes:
                    updated = curr[2] + [neighbor[1]]
                    h = dist[curr[0]] + neighbor[2]
                    dist[neighbor[0]] = h
                    s.push((neighbor[0], neighbor[1], updated), h)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    s = util.PriorityQueue()
    visited_nodes = set()
    dist = {}
    start = problem.getStartState()
    dist[start] = 0
    s.push((start, None, []), (0 + heuristic(start, problem)))
    while s.isEmpty() == False:
        curr = s.pop()
        if problem.isGoalState(curr[0]):
            return curr[2]
        if curr[0] not in visited_nodes:
            visited_nodes.add(curr[0])
            for neighbor in problem.getSuccessors(curr[0]):
                if neighbor[0] not in visited_nodes:
                    updated = curr[2] + [neighbor[1]]
                    dist[neighbor[0]] = dist[curr[0]] + neighbor[2]
                    h = heuristic(neighbor[0], problem) + dist[neighbor[0]]
                    s.push((neighbor[0], neighbor[1], updated), h)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch





##############################################################################################################

# # search.py
# # ---------
# # Licensing Information:  You are free to use or extend these projects for
# # educational purposes provided that (1) you do not distribute or publish
# # solutions, (2) you retain this notice, and (3) you provide clear
# # attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# #
# # Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# # The core projects and autograders were primarily created by John DeNero
# # (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# # Student side autograding was added by Brad Miller, Nick Hay, and
# # Pieter Abbeel (pabbeel@cs.berkeley.edu).
#
#
# """
# In search.py, you will implement generic search algorithms which are called by
# Pacman agents (in searchAgents.py).
# """
#
# import util
#
# class SearchProblem:
#     """
#     This class outlines the structure of a search problem, but doesn't implement
#     any of the methods (in object-oriented terminology: an abstract class).
#
#     You do not need to change anything in this class, ever.
#     """
#
#     def getStartState(self):
#         """
#         Returns the start state for the search problem.
#         """
#         util.raiseNotDefined()
#
#     def isGoalState(self, state):
#         """
#           state: Search state
#
#         Returns True if and only if the state is a valid goal state.
#         """
#         util.raiseNotDefined()
#
#     def getSuccessors(self, state):
#         """
#           state: Search state
#
#         For a given state, this should return a list of triples, (successor,
#         action, stepCost), where 'successor' is a successor to the current
#         state, 'action' is the action required to get there, and 'stepCost' is
#         the incremental cost of expanding to that successor.
#         """
#         util.raiseNotDefined()
#
#     def getCostOfActions(self, actions):
#         """
#          actions: A list of actions to take
#
#         This method returns the total cost of a particular sequence of actions.
#         The sequence must be composed of legal moves.
#         """
#         util.raiseNotDefined()
#
#
# def tinyMazeSearch(problem):
#     """
#     Returns a sequence of moves that solves tinyMaze.  For any other maze, the
#     sequence of moves will be incorrect, so only use this for tinyMaze.
#     """
#     from game import Directions
#     s = Directions.SOUTH
#     w = Directions.WEST
#     return  [s, s, w, s, w, w, s, w]
#
# def depthFirstSearch(problem):
#     """
#     Search the deepest nodes in the search tree first.
#
#     Your search algorithm needs to return a list of actions that reaches the
#     goal. Make sure to implement a graph search algorithm.
#
#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:
#
#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())
#     """
#     "*** YOUR CODE HERE ***" ################################
#
#     fringe = util.Stack()
#     return search_for(problem, fringe)
#
# def search_for(problem, fringe):
#     closed = set()
#     starting_state = (problem.getStartState(), 0, [])  # (node, cost, path)
#     fringe.push(starting_state)
#
#     while not fringe.isEmpty():
#         (node, cost, path) = fringe.pop()
#
#         if problem.isGoalState(node):
#             return path
#
#         if not node in closed:
#             closed.add(node)
#
#             for child_node, child_action, child_cost in problem.getSuccessors(node):
#                 if child_node not in closed:
#                     new_cost = cost + child_cost
#                     new_path = path + [child_action]
#                     new_state = (child_node, new_cost, new_path)
#                     fringe.push(new_state)
#
#     return []
#     # util.raiseNotDefined()
#
# def uniform_cost_search(problem, fringe):
#     closed = set()
#     starting_state = (problem.getStartState(), 0, [])  # (node, cost, path)
#     fringe.push(starting_state, starting_state[1])
#
#     while not fringe.isEmpty():
#         (node, cost, path) = fringe.pop()
#
#         if problem.isGoalState(node):
#             return path
#
#         if not node in closed:
#             closed.add(node)
#
#             for child_node, child_action, child_cost in problem.getSuccessors(node):
#                 if child_node not in closed:
#                     new_cost = cost + child_cost
#                     new_path = path + [child_action]
#                     new_state = (child_node, new_cost, new_path)
#                     fringe.push(new_state, new_state[1])
#
#     return []
#
# def astar_search(problem, fringe, heuristic):
#     closed = set()
#     starting_state = (problem.getStartState(), 0, [])  # (node, cost, path)
#     new_cost = starting_state[1] + heuristic(starting_state[0], problem)
#     fringe.push(starting_state, new_cost)
#
#     while not fringe.isEmpty():
#         (node, cost, path) = fringe.pop()
#
#         if problem.isGoalState(node):
#             return path
#
#         if not node in closed:
#             closed.add(node)
#
#             for child_node, child_action, child_cost in problem.getSuccessors(node):
#                 if child_node not in closed:
#                     new_cost = cost + child_cost
#                     new_path = path + [child_action]
#                     new_state = (child_node, new_cost, new_path)
#                     updated_cost = new_state[1] + heuristic(new_state[0], problem)
#                     fringe.push(new_state, updated_cost)
#
#     return []
#
# def breadthFirstSearch(problem):
#     """Search the shallowest nodes in the search tree first."""
#     "*** YOUR CODE HERE ***" ##################################
#
#     fringe = util.Queue()
#     return search_for(problem, fringe)
#
#     # util.raiseNotDefined()
#
# def uniformCostSearch(problem):
#     """Search the node of least total cost first."""
#     "*** YOUR CODE HERE ***" ############################
#
#     fringe = util.PriorityQueue()
#     return uniform_cost_search(problem, fringe)
#
#
#     # util.raiseNotDefined()
#
# def nullHeuristic(state, problem=None):
#     """
#     A heuristic function estimates the cost from the current state to the nearest
#     goal in the provided SearchProblem.  This heuristic is trivial.
#     """
#     return 0
#
# def aStarSearch(problem, heuristic=nullHeuristic):
#     """Search the node that has the lowest combined cost and heuristic first."""
#     "*** YOUR CODE HERE ***" #########################################
#
#     fringe = util.PriorityQueue()
#     return astar_search(problem, fringe, heuristic)
#
#     # util.raiseNotDefined()
#
# # Abbreviations
# bfs = breadthFirstSearch
# dfs = depthFirstSearch
# astar = aStarSearch
# ucs = uniformCostSearch

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
