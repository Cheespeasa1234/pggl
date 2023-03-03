import time
import pygame
import random

from levigl import Graphics2D
from sprite import Player, Enemy, WIDTH, HEIGHT

pygame.init()
pygame.display.set_caption("Dino Game")

FPS = 45

screen = pygame.display.set_mode([WIDTH, HEIGHT])
g2 = Graphics2D(screen, pygame)

enemies, player = [], Player()

fps_clock = pygame.time.Clock()
delta_time = 60 / FPS
running = True
frames_until_new_enemy = 100

def draw():
  screen.fill((255, 255, 255))
  for enemy in enemies:
    enemy.draw(g2)
  player.draw(g2)

def update():

  # update all enemies
  for enemy in enemies:
    if enemy.update(4 * delta_time, player):
      enemies.remove(enemy)

  # update the player
  player.update(4 * delta_time) 

while running:

  frames_until_new_enemy -= 1 * delta_time
  if frames_until_new_enemy <= 0:
    enemies.append(Enemy())
    frames_until_new_enemy = random.randint(50, 120)
    print("New enemy in: ", frames_until_new_enemy / FPS, "seconds")

  # manage events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player.UP_PRESSED(event)
      elif event.key == pygame.K_DOWN:
        player.DOWN_PRESSED(event)
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        player.UP_RELEASED(event)
      elif event.key == pygame.K_DOWN:
        player.DOWN_RELEASED(event)
  
  # draw to the screen
  draw()

  # update sprites
  update()

  pygame.display.flip()
  fps_clock.tick(FPS)

pygame.quit()