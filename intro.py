import pgzrun
import os

WIDTH = 1024
HEIGHT = 768 

enemy = Actor('enemy-128')
enemy.topright = 0, 10

os.environ['SDL_VIDEO_CENTERED'] = '1'

def draw():
    screen.clear()
    screen.fill((145, 160, 125))
    enemy.draw()

def update():
    enemy.left += 2
    if enemy.left > WIDTH:
        enemy.right = 0

pgzrun.go()
