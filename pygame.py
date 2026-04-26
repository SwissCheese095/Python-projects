import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

rect_x = 50
rect_y = 50
pos_x = 0
pos_y = 0
speed = 1

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running.false
  clock.tick(120)
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w] or keys[pygame.K_UP]:
    pos_y = pos_y - speed
  if keys[pygame.K_s] or keys[pygame.K_DOWN]:
    pos_y = pos_y + speed
  if keys[pygame.K_a] or keys[pygame.K_LEFT]:
    pos_x = pos_x - speed
  if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    pos_x = pos_x + speed
  
  screen.fill((0, 0, 125))
  pygame.draw.rect(screen, (255, 255, 0), (pos_x, pos_y, rect_x, rect_y))
  pygame.display.flip()