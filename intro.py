import pgzrun
import os

WIDTH = 1024
HEIGHT = 768

GROUND_LEVEL = 590

vertical_velocity = 0
jump_strength = -15
gravity = 0.5

enemy = Actor('enemy-128')
enemy.topright = 1000, GROUND_LEVEL
enemy.y = GROUND_LEVEL

player = Actor('player-128')
player.topright = 200, GROUND_LEVEL
player.y = GROUND_LEVEL

background = Actor('level1')

os.environ['SDL_VIDEO_CENTERED'] = '1'

def draw():
    screen.clear()
    screen.fill((145, 160, 125))
    background.draw()
    enemy.draw()
    player.draw()

def on_key_down(key):
    global vertical_velocity
    if key == keys.SPACE and player.y == GROUND_LEVEL:
        vertical_velocity = jump_strength

def update():
    global vertical_velocity
    enemy.left -= 4
    if enemy.left < 0:
        enemy.right = WIDTH

    vertical_velocity += gravity
    player.y += vertical_velocity

    if player.y >= GROUND_LEVEL:
        player.y = GROUND_LEVEL
        vertical_velocity = 0

    if keyboard.right:
        player.x += 4
    if keyboard.left:
        player.x -= 4
 
pgzrun.go()
