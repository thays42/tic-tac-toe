from random import choice

class TicTacToe:
	def __init__(self, board=None):
		""" A Tic Tac Toe board is represented by a list of length 9.
		By default, the board is populated by the strings '1', ..., '9'
		"""
		if board is None:
			self.board = [str(x) for x in range(1, 10)]
		else:
			self.board = board

	def __repr__(self):
		""" Print a board representation of Tic Tac Toe
		"""
		horizontal = '---|---|---'
		return '\n'.join([
			' ' + ' | '.join(self.board[:3]),
			horizontal,
			' ' + ' | '.join(self.board[3:6]),
			horizontal,
			' ' + ' | '.join(self.board[6:9])
		])

	def check_for_win(self, xo):
		""" Check for a win in all 8 possible combinations.
		"""
		checks = [
			[0,1,2], [3,4,5], [6,7,8], # horizontals
			[0,3,6], [1,4,7], [2,5,8], # verticals
			[0,4,8], [2,4,6]           # diagonals
		]

		for check in checks:
			if all(self.board[c] == xo for c in check):
				return True
		return False

	def mark(self, i, xo):
		""" Mark the ith cell (1-indexed) with xo
		"""
		i = int(i) - 1
		if self.board[i] not in {'X', 'O'}:
			self.board[i] = xo
			return True
		else:
			return False

	def get_empty(self):
		""" Return a set of cells (1-indexed) for valid input
		"""
		return {str(idx + 1) for idx, value in enumerate(self.board) if value not in {'X', 'O'}}


def player_move(game, xo):
	""" A player's move is composed of:
	1. Print the game and prompt for input
	2. Validate input
	3. Mark game with input
	4. Check for win
	"""
	print(game)
	player_input = input('\nSelect cell to play: ')
	valid_input = game.get_empty()
	while player_input not in valid_input:
		print(game)
		player_input = input('\nSelect cell to play: ')
	game.mark(player_input, xo)
	if game.check_for_win(xo):
		print('\n')
		print(game)
		print("You Win!")
		return True
	return False

def computer_move(game, xo):
	""" A computer's move is composed of:
	1. Randomly pick a valid move
	2. Mark game with input
	3. Check for win
	"""
	computer_input = choice(list(game.get_empty()))
	game.mark(computer_input, xo)
	if game.check_for_win(xo):
		print('\n')
		print(game)
		print("Computer Wins!")
		return True
	return False

def main():
	""" A game is composed of:
	1. Initialize board
	2. Prompt for XO choice
	3. Determine move order
	4. Iterate through moves
	"""
	game = TicTacToe()
	turn = 0

	player_xo = input('X or O (X goes first): ').upper()
	while player_xo not in {'X', 'O'}:
		player_xo = input('X or O (X goes first): ').upper()

	if player_xo == 'X':
		computer_xo = 'O'
		game_order = [(player_move, player_xo),
		              (computer_move, computer_xo)]
	else:
		computer_xo = 'X'
		game_order = [(computer_move, computer_xo),
					  (player_move, player_xo)]

	while turn < 9:
		move, xo = game_order[turn % 2]
		if move(game, xo):
			return
		turn += 1

	print(game)
	print("It's a draw!")

if __name__ == '__main__':
	main()
