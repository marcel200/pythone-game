import sys
 
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
x, y = 320, 240
 
# Game loop.
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_DOWN:
        y += 10
      if event.key == K_UP:
        y -= 10
      if event.key == K_LEFT:
        x -= 10
      if event.key == K_RIGHT:
        x += 10
  # Update.
 
  # Draw.
  screen.fill((255, 255, 255))
  pygame.draw.circle(
    screen,
    (0, 255, 0),
    (x, y),
    20
  )
 
  pygame.display.flip()
  fpsClock.tick(fps)
