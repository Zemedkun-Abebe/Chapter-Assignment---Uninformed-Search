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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    visited = set()  # To keep track of visited states
    stack = util.Stack()  # Stack to implement DFS
    stack.push((problem.getStartState(), [], 0))  # Start state, actions, and cost

    while not stack.isEmpty():
        state, actions, cost = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            for successor, action, stepCost in successors:
                if successor not in visited:
                    stack.push((successor, actions + [action], cost + stepCost))

    return []  # Return empty list if no solution found

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    # Create a queue for BFS
    frontier = util.Queue()
    # Add the initial state of the problem to the frontier
    frontier.push((problem.getStartState(), []))
    # Create a set to keep track of visited states
    visited = set()
    
    while not frontier.isEmpty():
        state, actions = frontier.pop()  # Get the next state and actions from the frontier
        if problem.isGoalState(state):  # Check if the current state is the goal state
            return actions  # Return the actions taken to reach the goal state
        
        if state not in visited:  # If the current state has not been visited before
            visited.add(state)  # Add the current state to the visited set
            successors = problem.getSuccessors(state)  # Get the successors of the current state
            for successor in successors:
                next_state, action, cost = successor
                if next_state not in visited:  # Only add unvisited successors to the frontier
                    frontier.push((next_state, actions + [action]))  # Add the successor to the frontier with updated actions
    
    return []  # Return empty actions list if no solution is found


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    # Create a priority queue for UCS
    frontier = util.PriorityQueue()
    # Add the initial state of the problem to the frontier with a cost of 0
    frontier.push((problem.getStartState(), []), 0)
    # Create a dictionary to keep track of the cost to reach each state
    costs = {problem.getStartState(): 0}
    # Create a set to keep track of visited states
    visited = set()

    while not frontier.isEmpty():
        state, actions = frontier.pop()  # Get the next state and actions from the frontier
        if problem.isGoalState(state):  # Check if the current state is the goal state
            return actions  # Return the actions taken to reach the goal state

        if state not in visited:  # If the current state has not been visited before
            visited.add(state)  # Add the current state to the visited set
            successors = problem.getSuccessors(state)  # Get the successors of the current state
            for successor in successors:
                next_state, action, cost = successor
                new_cost = costs[state] + cost  # Calculate the total cost to reach the successor
                if next_state not in costs or new_cost < costs[next_state]:
                    # Update the cost to reach the successor if it's lower than the current cost
                    costs[next_state] = new_cost
                    frontier.push((next_state, actions + [action]), new_cost)  # Add the successor to the frontier with updated actions and cost

    return []  # Return empty actions list if no solution is found


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
