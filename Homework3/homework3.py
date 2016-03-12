############################################################
# CIS 391: Homework 3
############################################################

student_name = "Arjun Raj Jain"

############################################################
# Imports
############################################################
import math
import itertools
import random  
import copy
import Queue
from collections import deque
# Include your imports here, if any are used.



############################################################
# Section 1: Tile Puzzle
############################################################

def create_tile_puzzle(rows, cols):
    board = [ [ row*cols+col+1 for col in xrange(cols) ] for row in xrange(rows) ]
    board[rows-1][cols-1] = 0
    return TilePuzzle(board)

class TilePuzzle(object):
    
    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        for i in range(self.rows) :
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    self.empty = [i,j]

    def get_board(self):
        return list(self.board)

    def perform_move(self, direction):
        if direction == "up" :
            if self.empty[0] > 0  :
                num = self.board[self.empty[0]-1][self.empty[1]]
                self.board[self.empty[0]-1][self.empty[1]] = 0
                self.board[self.empty[0]][self.empty[1]] = num
                self.empty[0] = self.empty[0]-1;
                return True

        elif direction == "down" : 
            if self.empty[0] < self.rows-1 :
                num = self.board[self.empty[0]+1][self.empty[1]]
                self.board[self.empty[0]+1][self.empty[1]] = 0
                self.board[self.empty[0]][self.empty[1]] = num
                self.empty[0] = self.empty[0]+1;
                return True 

        elif direction == "left" :
            if self.empty[1] > 0 :
                num = self.board[self.empty[0]][self.empty[1]-1]
                self.board[self.empty[0]][self.empty[1]-1] = 0
                self.board[self.empty[0]][self.empty[1]] = num
                self.empty[1] = self.empty[1]-1;
                return True

        elif direction == "right" :
            if self.empty[1] < self.cols-1 : 
                num = self.board[self.empty[0]][self.empty[1]+1]
                self.board[self.empty[0]][self.empty[1]+1] = 0
                self.board[self.empty[0]][self.empty[1]] = num
                self.empty[1] = self.empty[1]+1;
                return True   
        return False

    def scramble(self, num_moves):
        for i in range(num_moves):
            self.perform_move(random.choice(['up','down','left','right']))

    def is_solved(self):
        solution = [ [ row*self.cols+col+1 for col in xrange(self.cols) ] for row in xrange(self.rows) ]
        solution[self.rows-1][self.cols-1] = 0
        if self.board == solution :
            return True
        else :
            return False

    def copy(self):
        return copy.deepcopy(self)

    def successors(self):
        for direction in ['up','down','left','right']:
            new_board = self.copy()
            valid  = new_board.perform_move(direction)
            if valid:
                yield direction, new_board  

    # Required
    def find_solutions_iddfs(self):
        done = False
        for limit in itertools.count() :
            if(done) : 
                break;
            solution = self.iddfs_helper(limit)
            if solution :
                for sol in solution :
                    yield sol
                    done = True

    def iddfs_helper(self,depth):
        stack = [];
        stack.append((0,self))

        explored = set()

        parent = {}
        parent[self] = None

        moves = {}
        moves[self] = None

        solution = [];

        while stack:
            obj = stack.pop()
            board = obj[1]
            explored.add(board.toTup())
            if board.is_solved():
                node = board
                sol = []
                while not parent[node] == None:
                    sol.append((moves[node]))
                    node = parent[node]
                solution.append(list(reversed(sol)))
            if obj[0] < depth:
                for move, nextBoard in board.successors():
                    if nextBoard.toTup() not in explored:
                        moves[nextBoard] = move
                        parent[nextBoard] = board
                        stack.append((obj[0]+1,nextBoard))
        return solution

    def toTup(self):
        return tuple(tuple(row) for row in self.get_board())

    def heuristic(self):
        H = 0
        for r1 in range(self.rows):
            for c1 in range(self.cols):
                if self.board[r1][c1] == 0:
                    r2 = self.rows - 1
                    c2 = self.cols - 1
                else :
                    r2 = self.board[r1][c1] / self.rows
                    c2 = self.board[r1][c1] % self.cols
                H = H + abs(c1-c2) + abs(r1-r2)
        return H

    # Required
    def find_solution_a_star(self):
        q = Queue.PriorityQueue();
        q.put((0,0,self))

        explored = set()

        parent = {}
        parent[self] = None

        moves = {}
        moves[self] = None

        while not q.empty() :
            obj = q.get()
            board = obj[2]
            explored.add(board.toTup())
            if board.is_solved():
                node = board
                sol = []
                while not parent[node] == None:
                    sol.append((moves[node]))
                    node = parent[node]
                return (list(reversed(sol)))
            else :
                for move, nextBoard in board.successors() :
                    if nextBoard.toTup() not in explored: 
                        G = obj[1] + 1
                        H = nextBoard.heuristic()
                        F = H + G
                        moves[nextBoard] = move
                        parent[nextBoard] = board
                        q.put((F,G,nextBoard))

############################################################
# Section 2: Grid Navigation
############################################################
def get_successors(row,col,scene):
    rows = len(scene);
    cols = len(scene[0])
    if row > 0 and not scene[row-1][col]:
        yield((row-1,col))
    if row < rows -1 and not scene[row+1][col]:
        yield((row+1,col))
    if col > 0 and not scene[row][col-1]:
        yield((row,col-1))
    if col < cols -1 and not scene[row][col+1]:
        yield((row,col+1))
    if row > 0 and col > 0 and not scene[row-1][col-1]:
        yield((row-1,col-1))
    if row > 0 and col < cols - 1 and not scene[row-1][col+1]:
        yield((row-1,col+1))
    if row < rows -1 and col > 0 and not scene[row+1][col-1]:
        yield((row+1, col-1))
    if row < rows -1 and col < cols -1 and not scene[row+1][col+1]:
        yield((row+1,col+1))

def find_path(start, goal, scene):
    q = Queue.PriorityQueue();
    q.put((0,0,start))

    explored = set()

    parent = {}
    parent[start] = None

    if scene[start[0]][start[1]] or scene[goal[0]][goal[1]] :
        return None

    while not q.empty() :
        obj = q.get()
        place = obj[2]
        explored.add(place)
        if place == goal:
            node = place
            sol = [place]
            while not parent[node] == None:
                sol.append((parent[node]))
                node = parent[node]
            return (list(reversed(sol)))
        else :
            for nextMove in get_successors(place[0],place[1],scene) :
                if nextMove not in explored: 
                    G = obj[1] + 1
                    H = grid_heuristic(nextMove,goal)
                    F = H + G
                    parent[nextMove] = place
                    q.put((F,G,nextMove))
    return None


def grid_heuristic(cur,goal):
    return math.sqrt((goal[0]-cur[0])**2 + (goal[1]-cur[1])**2)

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################
class LinearDiskMovement(object):
    def __init__(self, length, n):
        self.length = length
        self.n = n
        self.cells =  [i+1 if i < n else 0 for i in xrange(length)]

    def perform_move(self,fromIndex,toIndex) :
        self.cells[toIndex] = self.cells[fromIndex]
        self.cells[fromIndex] = 0

    def copy(self):
        return copy.deepcopy(self)

    def successors(self):
        for i in range(self.length):
            if self.cells[i]:
                if i + 1 < self.length and self.cells[i+1] == 0:
                    newLinearDisk = self.copy()
                    newLinearDisk.perform_move(i,i+1)
                    yield(tuple((i, i+1)), newLinearDisk)
                if i + 2 < self.length and self.cells[i+2] == 0 and self.cells[i+1] !=0:
                    newLinearDisk = self.copy()
                    newLinearDisk.perform_move(i,i+2)
                    yield(tuple((i, i+2)), newLinearDisk)
                if i-1 >= 0 and self.cells[i-1] == 0:
                    newLinearDisk = self.copy()
                    newLinearDisk.perform_move(i,i-1)
                    yield(tuple((i, i-1)), newLinearDisk)
                if i - 2 >= 0 and self.cells[i-2] == 0 and self.cells[i-1] !=0:
                    newLinearDisk = self.copy()
                    newLinearDisk.perform_move(i,i-2)
                    yield(tuple((i, i-2)), newLinearDisk)

    def is_solved_distinct(self) :
        return list(reversed([i+1 if i < self.n else 0 for i in xrange(self.length)])) == self.cells

    def solve_cells(self) :
        q = Queue.PriorityQueue()
        q.put( (0,0,self) )

        explored = set()
        explored.add(tuple(self.cells));

        parent = {}
        parent[self] = None

        moves = {}
        moves[self] = None

        solution = [];

        while not q.empty() :
            obj = q.get()
            board = obj[-1]
            if board.is_solved_distinct():
                    node = board
                    while not parent[node] == None:
                        solution.append(moves[node])
                        node = parent[node]
                    return list(reversed(solution))
            else :
                for move, nextBoard in board.successors() :
                    if tuple(nextBoard.cells) not in explored :
                        explored.add(tuple(nextBoard.cells));
                        G = obj[1] + 1
                        H = nextBoard.disk_heuristic()
                        F = H + G
                        q.put((F,G,nextBoard))
                        moves[nextBoard] = move
                        parent[nextBoard] = board
        return None

    def disk_heuristic(self):
        H = 0
        for i in range(self.length):
            if(self.cells[i]!=0) :
                if self.cells[i] != self.cells[-1*self.cells[i]] :
                    H+=abs(self.length - self.cells[i] - i)
        return H

def solve_distinct_disks(length, n):
    return LinearDiskMovement(length,n).solve_cells()

############################################################
# Section 4: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    return DominoesGame([[False for col in range(cols)] for row in range(rows)])

leaf = 0;

class DominoesGame(object):
    # Required

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])


    def get_board(self):
        return self.board

    def reset(self):
        self.board = [[False for j in range(self.cols)] for i in range(self.rows)]

    def is_legal_move(self, row, col, vertical):
        if row >= 0 and col >=0 and not self.board[row][col] : 
            if vertical and row +1 < self.rows and not self.board[row+1][col]:
                return True
            elif not vertical and col +1 < self.cols and not self.board[row][col+1]:
                return True
        return False    

    def legal_moves(self, vertical):
        return [(row,col) for row in range(self.rows) for col in range(self.cols) if self.is_legal_move(row,col,vertical)]

    def perform_move(self, row, col, vertical):
        if vertical :
            self.board[row][col] = True
            self.board[row+1][col] = True
        else :
            self.board[row][col] = True
            self.board[row][col+1] = True

    def game_over(self, vertical):
        return len(self.legal_moves(vertical)) == 0

    def copy(self):
        return copy.deepcopy(self)

    def successors(self, vertical):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_legal_move(row,col,vertical):
                    new = self.copy()
                    new.perform_move(row,col,vertical)
                    yield ((row,col),DominoesGame(new.board))

    def get_random_move(self, vertical):
        return random.choice(self.legal_moves(vertical))

    # Required
    def get_best_move(self, vertical, limit):
        global leaf
        leaf = 0;
        #format Error , had to break down return from minmaxval into two objects
        bestMove, value = minmaxval(self,float('-inf'),float('inf'),vertical,limit,vertical,True,domino_heuristic)
        return (bestMove,value, leaf)


def minmaxval(node,alpha,beta,vertical,limit,originalUser,isMax,heuristicFn):
    global leaf
    value = float('-inf') if isMax else float('inf')
    bestMove = ()
    if limit == 0 or node.game_over(vertical):
        leaf = leaf +1
        return (bestMove, heuristicFn(node,originalUser))
    for move, nextBoard in node.successors(vertical):
        m, v = minmaxval(nextBoard,alpha, beta, not vertical,limit-1,originalUser,not isMax,heuristicFn)
        if (v > value and isMax) or (v < value and not isMax):
            bestMove = move
            value = max(value, v) if isMax else min(value,v)
            if isMax :
                alpha = max(value,alpha)
            else :
                beta = min(beta,value)
            if beta <= alpha:
                break
    return (bestMove, value)

def domino_heuristic(node,vertical):
    return len(node.legal_moves(vertical)) - len(node.legal_moves(not vertical))
############################################################
# Section 5: Feedback
############################################################


feedback_question_1 = """
About 15 hours
"""

feedback_question_2 = """
I didn't find this assignment heavily challenging as it built off of
Homework 2 a lot. Nevertheless, I should have started earlier as I 
had to take a late day on this.
"""

feedback_question_3 = """
I liked the simplicity of A* and implementing it in actual code. I also liked
trying to optimize the beta/alpha method of finding the best move by creating my
minmax function that is independent of Dominoes. This will hopefully help me
in further assignments.
"""
