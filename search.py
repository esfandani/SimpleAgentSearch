# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    stack = util.Stack()
    state = problem.getStartState();
    closed = set();
    if problem.isGoalState(state):
        return []
    stack.push((state, []))
    for suc_state, direction, cost in problem.getSuccessors(state):
        if not suc_state in closed:
            stack.push((suc_state, [direction]))
        closed.add(state)
    while not stack.isEmpty():
        state, actions = stack.pop()
        if problem.isGoalState(state):
            return actions
        if(state in closed):
            continue;
        for suc_state, direction, cost in problem.getSuccessors(state):
            if not suc_state in closed:
                stack.push((suc_state, actions + [direction]))
            closed.add(state)
    return None

def breadthFirstSearch(problem):
    q = util.Queue()
    state = problem.getStartState();
    closed = set();
    if problem.isGoalState(state):
        return []
    q.push((state, []))
    for suc_state, direction, cost in problem.getSuccessors(state):
        if not suc_state in closed:
            q.push((suc_state, [direction]))
        closed.add(state)
    while not q.isEmpty():
        state, actions = q.pop()
        if problem.isGoalState(state):
            return actions
        if(state in closed):
            continue;
        for suc_state, direction, cost in problem.getSuccessors(state):
            if not suc_state in closed:
                q.push((suc_state, actions + [direction]))
            closed.add(state)
    return None

def uniformCostSearch(problem):
    pq = util.PriorityQueue()
    state = problem.getStartState();
    closed = set();
    if problem.isGoalState(state):
        return []
    pq.push((state, []),0)
    for suc_state, direction, cost in problem.getSuccessors(state):
        if not suc_state in closed:
            t = [direction]
            pq.push((suc_state,t),problem.getCostOfActions(t))
        closed.add(state)
    while not pq.isEmpty():
        state, actions = pq.pop()
        if problem.isGoalState(state):
            return actions
        if(state in closed):
            continue;
        for suc_state, direction, cost in problem.getSuccessors(state):
            if not suc_state in closed:
                temp = actions + [direction]
                pq.push((suc_state, temp),problem.getCostOfActions(temp))
            closed.add(state)
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    pq = util.PriorityQueue()
    state = problem.getStartState();
    closed = set();
    if problem.isGoalState(state):
        return []
    pq.push((state, []),heuristic(state,problem))
    for suc_state, direction, cost in problem.getSuccessors(state):
        if not suc_state in closed:
            t = [direction]
            pq.push((suc_state,t),problem.getCostOfActions(t)+heuristic(suc_state,problem))
        closed.add(state)
    while not pq.isEmpty():
        state, actions = pq.pop()
        if problem.isGoalState(state):
            return actions
        if(state in closed):
            continue;
        for suc_state, direction, cost in problem.getSuccessors(state):
            if not suc_state in closed:
                temp = actions + [direction]
                pq.push((suc_state, temp),problem.getCostOfActions(temp)+heuristic(suc_state,problem))
            closed.add(state)
    return None



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
