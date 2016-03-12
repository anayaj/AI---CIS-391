p = create_tile_puzzle(3, 3)
p2 = p.copy()
p.get_board() == p2.get_board()

p = create_tile_puzzle(3, 3)
p2 = p.copy()
p.perform_move("left")
p.get_board() == p2.get_board()


p = create_tile_puzzle(3, 3)
for move, new_p in p.successors():
	print move, new_p.get_board()


b = [[1,2,3], [4,0,5], [6,7,8]]
p = TilePuzzle(b)
for move, new_p in p.successors():
	print move, new_p.get_board()


b = [[4,1,2], [0,5,3], [7,8,6]]
p = TilePuzzle(b)
solutions = p.find_solutions_iddfs()
next(solutions)

b = [[1,2,3], [4,0,8], [7,6,5]]
p = TilePuzzle(b)
list(p.find_solutions_iddfs())

b = [[4,1,2], [0,5,3], [7,8,6]]
p = TilePuzzle(b)
p.find_solution_a_star()

b = [[1,2,3], [4,0,5], [6,7,8]]
p = TilePuzzle(b)
p.find_solution_a_star()

scene = [[False, False, False],[False, True , False],[False, False, False]]
find_path((0, 0), (2, 1), scene)

scene = [[False, True, False],[False, True, False],[False, True, False]]
print find_path((0, 0), (0, 2), scene)

b = [[False] * 3 for i in range(3)]
g = DominoesGame(b)
g.get_best_move(True, 1)
g.get_best_move(True, 2)
b = [[False] * 3 for i in range(3)]
g = DominoesGame(b)
g.perform_move(0, 1, True)
g.get_best_move(False, 1)
g.get_best_move(False, 2)