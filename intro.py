import pgzrun
import os

WIDTH = 1024
HEIGHT = 768 

enemy = Actor('enemy-128')
enemy.topright = 0, 10

player = Actor('player-128')
player.topright = 200,200

os.environ['SDL_VIDEO_CENTERED'] = '1'

def draw():
    screen.clear()
    screen.fill((145, 160, 125))
    enemy.draw()
    player.draw()

def update():
    enemy.left += 2
    if enemy.left > WIDTH:
        enemy.right = 0
    if keyboard.up:
        player.y -= 2
    if keyboard.down:
        player.y += 2
    if keyboard.right:
        player.x += 2
    if keyboard.left:
        player.x -= 2
 
pgzrun.go()
