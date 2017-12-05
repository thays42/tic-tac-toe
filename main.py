from random import choice

class TicTacToe:
	def __init__(self, board=None):
		if board is None:
			self.board = [str(x) for x in range(1, 10)]
		else:
			self.board = board

	def __repr__(self):
		horizontal = '---|---|---'
		return '\n'.join([
			' ' + ' | '.join(self.board[:3]),
			horizontal,
			' ' + ' | '.join(self.board[3:6]),
			horizontal,
			' ' + ' | '.join(self.board[6:9])
		])

	def check_for_win(self, xo):
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
		i = int(i) - 1
		if self.board[i] not in {'X', 'O'}:
			self.board[i] = xo
			return True
		else:
			return False

	def get_empty(self):
		return {str(idx + 1) for idx, value in enumerate(self.board) if value not in {'X', 'O'}}

def player_move(game, xo):
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
	computer_input = choice(list(game.get_empty()))
	game.mark(computer_input, xo)
	if game.check_for_win(xo):
		print('\n')
		print(game)
		print("Computer Wins!")
		return True
	return False

def main():
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
