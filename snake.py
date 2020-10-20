import pygame

pygame.init()

x,y = 400, 300
display = pygame.display.set_mode((x,y))
pygame.display.set_caption('Snakes and Apples - Owen Kornelsen')
pygame.display.update()

game_over = False
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True

pygame.quit()
quit()