import pygame




class Game:
	def __init__(self):

		pygame.display.set_mode((800, 600))

		pygame.display.set_caption("Aventure")


	def run(self):

		 running = True

		 while running:
		 	for event in pygame.event.get():
		 		if event.type == pygame.QUIT:
		 			running = False
		 pygame.quit()




if __name__ == '__main__':
	pygame.init()
	game = Game()
	game.run()
