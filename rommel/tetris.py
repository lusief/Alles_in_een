import pygame, sys, random

# Very simple tetris implementation
# 
# Control keys:
# Down - Drop stone faster
# Left/Right - Move stone
# Up - Rotate Stone clockwise
# Escape - Quit game
# P - Pause game
#
# Have fun!

CONFIG = {
		'cell_size': 40,
		'cols': 9,
		'rows':	16,
		'delay': 750,
		'maxfps': 60,
		'shapes': [
			[[1, 1, 1],[0, 1, 0]],
			[[0, 2, 2],[2, 2, 0]],
			[[3, 3, 0],[0, 3, 3]],
			[[4, 0, 0],[4, 4, 4]],
			[[0, 0, 5],[5, 5, 5]],
			[[6, 6, 6, 6]],
			[[7, 7],[7, 7]]
		],
		'colors':[
			(0,0,0),
			(255,0,0),
			(0,150,0),
			(0,0,255),
			(255,120,0),
			(255,255,0),
			(180,0,255),
			(0,220,220),
			(150,150,150)
		]
	}

class Tetris(object):
	def __init__(self, config:dict) -> None:
		pygame.init()
		pygame.key.set_repeat(250,25)

		self._config = config
		self.width = config['cell_size']*config['cols']
		self.height = config['cell_size']*config['rows']
		self.gameover = True
		
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.event.set_blocked(pygame.MOUSEMOTION) # We do not need mouse movement

		self.start_game()

	def start_game(self) -> None:
		if self.gameover:
			self.new_board()
			self.new_stone()
			self.gameover = False

	def new_board(self) -> list:
		self.board = [ [ 0 for x in range(self._config['cols']) ]
				for y in range(self._config['rows']) ]
		self.board += [[ 1 for x in range(self._config['cols'])]]
	
	def new_stone(self) -> None:
		self.stone = random.choice(self._config['shapes'])
		self.stone_x = int(self._config['cols'] / 2 - len(self.stone[0])/2)
		self.stone_y = 0
		
		if self.check_collision(self.board, self.stone, (self.stone_x, self.stone_y)):
			self.gameover = True
	
	def move(self, move_to:int) -> None:
		if not self.gameover and not self.paused:
			new_x = self.stone_x + move_to
			if new_x < 0:
				new_x = 0
			if new_x > self._config['cols'] - len(self.stone[0]):
				new_x = self._config['cols'] - len(self.stone[0])
			if not self.check_collision(self.board, self.stone, (new_x, self.stone_y)):
				self.stone_x = new_x

	def drop(self) -> None:
		if not self.gameover and not self.paused:
			self.stone_y += 1
			if self.check_collision(self.board, self.stone, (self.stone_x, self.stone_y)):
				self.board = self.join_matrixes(self.board, self.stone,(self.stone_x, self.stone_y))
				self.new_stone()
				
				while True:
					for i, row in enumerate(self.board[:-1]):
						if 0 not in row:
							self.board = self.remove_row(i)
							break
					else:
						break
	
	def rotate_stone(self) -> None:
		if not self.gameover and not self.paused:
			new_stone = []

			for x in range(len(self.stone[0]) - 1, -1, -1):
				stone_line = []
				for y in range(len(self.stone)):
					stone_line.append(self.stone[y][x])
				
				new_stone.append(stone_line)

			if not self.check_collision(self.board, new_stone, (self.stone_x, self.stone_y)):
				self.stone = new_stone
	
	def quit(self) -> None:
		self.center_msg("Exiting...")
		pygame.display.update()
		sys.exit()

	def join_matrixes(self, matrix1:list, matrix2:list, matrix2_off:list) -> list:
		off_x, off_y = matrix2_off
		for cy, row in enumerate(matrix2):
			for cx, val in enumerate(row):
				matrix1[cy+off_y-1][cx+off_x] += val
		return matrix1
	
	def draw_matrix(self, matrix:list, offset:list) -> None:
		off_x, off_y  = offset
		for y, row in enumerate(matrix):
			for x, val in enumerate(row):
				if val:
					rect = pygame.Rect(
						(off_x+x) * self._config['cell_size'],
						(off_y+y) * self._config['cell_size'], 
						self._config['cell_size'],
						self._config['cell_size']
					)
					pygame.draw.rect(self.screen,self._config['colors'][val],rect,0)

	def check_collision(self, board:list, shape:list, offset:tuple) -> bool:
		off_x, off_y = offset
		for cy, row in enumerate(shape):
			for cx, cell in enumerate(row):
				try:
					if cell and board[ cy + off_y ][ cx + off_x ]:
						return True
				except IndexError:
					return True
		return False
	
	def remove_row(self, row:int) -> list:
		del self.board[row]
		return [[0 for i in range(self._config['cols'])]] + self.board
	
	def toggle_pause(self) -> None:
		self.paused = not self.paused
	
	def center_msg(self, msg) -> None:
		for i, line in enumerate(msg.splitlines()):
			font = pygame.font.Font(pygame.font.get_default_font(), 12)
			msg_image = font.render(line, False, (255,255,255), (0,0,0))
		
			msgim_center_x, msgim_center_y = msg_image.get_size()
			msgim_center_x //= 2
			msgim_center_y //= 2
		
			self.screen.blit(msg_image, (self.width // 2-msgim_center_x, self.height // 2-msgim_center_y+i*22))
	
	def run(self) -> None:
		key_actions = {
			'ESCAPE':	self.quit,
			'LEFT':		lambda:self.move(-1),
			'RIGHT':	lambda:self.move(+1),
			'DOWN':		self.drop,
			'UP':		self.rotate_stone,
			'p':		self.toggle_pause,
			'SPACE':	self.start_game
		}
		
		self.gameover = False
		self.paused = False
		
		pygame.time.set_timer(pygame.USEREVENT+1, self._config['delay'])
		dont_burn_my_cpu = pygame.time.Clock()
		while 1:
			self.screen.fill((0,0,0))
			if self.gameover:
				self.center_msg("Game Over!\nPress space to continue")
			else:
				if self.paused:
					self.center_msg("Paused")
				else:
					self.draw_matrix(self.board, (0,0))
					self.draw_matrix(self.stone,(self.stone_x,self.stone_y))
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.USEREVENT+1:
					self.drop()
				elif event.type == pygame.QUIT:
					self.quit()
				elif event.type == pygame.KEYDOWN:
					for key in key_actions:
						if event.key == eval("pygame.K_"+key):
							key_actions[key]()
					
			dont_burn_my_cpu.tick(self._config['maxfps'])

if __name__ == '__main__':
	app = Tetris(CONFIG)
	app.run()