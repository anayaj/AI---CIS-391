############################################################
# CIS 391: Homework 4
############################################################

student_name = "Arjun Raj Jain"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import copy
import Queue

############################################################
# Section 1: Sudoku
############################################################

def sudoku_cells():
    return [(i,j) for i in range(9) for j in range(9)]

def sudoku_arcs():
    arcs = []
    # return [((i1,j1),(i2,j2)) for i1 in range(9) for j1 in range(9) for i2 in range(9) for j2 in range(9) if not(i1 == i2 and j1 == j2) and ((i1 == i2) or (j1 == j2) or ((i1)/3 == (i2)/3 and (j1)/3 == (j2)/3))]
    for i1 in range(9) :
        for j1 in range(9) :
            for i2 in range(9) :
                for j2 in range(9) :
                    if not(i1 == i2 and j1 == j2) and ((i1 == i2) or (j1 == j2) or ((i1)/3 == (i2)/3 and (j1)/3 == (j2)/3)) :
                        arcs.append(((i1,j1),(i2,j2)))
    return arcs

def read_board(path):
    sudoku_file = open(path, 'r')
    board = {}
    for rows, line in enumerate(sudoku_file):
        for cols, elem in enumerate(line):
            tup = (rows, cols)
            if elem.isdigit() :
                board[tup] = set([int(elem)])
            elif elem == "*":
                board[tup] = set([1,2,3,4,5,6,7,8,9])
    sudoku_file.close()
    return board 

class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()
    SOLVED = 81

    def __init__(self, board):
        self.board = board

    def copy(self):
        return copy.deepcopy(self)

    def get_values(self, cell):
        return self.board[cell]

    def remove_inconsistent_values(self, cell1, cell2):
        if self.cell_solved(cell2) and not self.cell_solved(cell1) :
            for value in self.get_values(cell2) : 
                if value in self.get_values(cell1):
                    self.get_values(cell1).remove(value)
                    return True
        return False

    def get_neighbors(self, cell, xj = {}):
        return [neighbor for neighbor,me in self.ARCS if (me == cell and not xj == neighbor)]

    def cell_solved(self,cell) :
        return len(self.get_values(cell))==1

    def num_solved(self) :
        return reduce(lambda x, y: x + 1 if self.cell_solved(y) else x, self.board,0)

    def get_unsolved_cells(self) :
        return [cell for cell in self.CELLS if not self.cell_solved(cell)]

    def can_solve(self):
        return reduce(lambda x, (cell1,cell2): x and not self.get_values(cell1) == self.get_values(cell2), self.ARCS,True) 
    
    def print_puzzle(self):
        i = 0
        string = "";
        for cell in self.CELLS:
            for val in self.get_values(cell) :
                string += str(val)
            i+=1
            if(i == 9) :
                print string
                string = ""
                i = 0
            

    def infer_cells(self) :
        for cell1 in self.get_unsolved_cells():
            arcCells = self.get_neighbors(cell1)
            curValues= self.get_values(cell1)

            difSetBox = curValues - reduce(lambda x,y: x.union(self.get_values(y)), [cell2 for cell2 in arcCells if ((cell1[0])/3 == (cell2[0])/3 and (cell1[1])/3 == (cell2[1])/3)],set())
            difSetRow = curValues - reduce(lambda x,y: x.union(self.get_values(y)), [cell2 for cell2 in arcCells if (cell1[0] == cell2[0])],set())
            difSetCol = curValues - reduce(lambda x,y: x.union(self.get_values(y)), [cell2 for cell2 in arcCells if (cell1[1] == cell2[1])],set())

            if len(difSetBox) == 1 :
                self.board[cell1] = difSetBox
            elif len(difSetCol) == 1 : 
                self.board[cell1] = difSetCol
            elif len(difSetRow) == 1 :
                self.board[cell1] = difSetRow


    def infer_ac3(self):
        q = Queue.Queue()
        for arcs in self.ARCS:
            q.put(arcs) 
        while not q.empty():
            (xi, xj) = q.get()
            if self.remove_inconsistent_values(xi, xj):
                for xk in self.get_neighbors(xi, xj):
                    q.put((xk, xi))

    def infer_improved(self):
        oldSolved = self.num_solved()
        while oldSolved < self.SOLVED :
            self.infer_ac3()
            self.infer_cells()
            newSolved = self.num_solved()
            if(oldSolved == newSolved) :
                return False
            oldSolved = newSolved
        return True

    def infer_with_guessing(self):
        self.infer_improved()
        for cell in self.get_unsolved_cells():
            for value in self.get_values(cell):
                guess = self.copy()
                guess.board[cell] = set([value])
                guess_solved = guess.infer_improved()
                if guess.can_solve():
                    self.board = guess.board
                    if guess_solved:
                        return True
                    else:
                        self.infer_with_guessing()

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
15 hours
"""

feedback_question_2 = """
I found finding small edge cases to be the most difficult part,
small things like line 63 tricked me up for awhile, causing everything 
to work but infer_with_guessing, and then after a lot of print statements
i realized I had to add " and not self.cell_solved(cell1)"
"""

feedback_question_3 = """
I think this assignment was fantastic. It was awesome to actually implement
a very intuitive way of solving Sudoku in the form of Constraint Satisfaction.
I'm also starting to really like all forms of list manipulation functions.
I honestly spent a good two hours just cleaning up code to read more intuitively.
"""
