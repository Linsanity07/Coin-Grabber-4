import pygame
from pygame.locals import *
from coin import Coin



pygame.display.init()

screen = pygame.display.set_mode((800,600))
player = pygame.Rect(400,300,15,15)
speed_x = 0
speed_y = 0

# Define colors for the game
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
RED = pygame.Color(255,0,0)
BLUE = pygame.Color(0,255,255)
YELLOW = pygame.Color(150,150,150)

#
clock = pygame.time.Clock()

def movement_loop():
  global speed_x, speed_y, player
  player.centerx += speed_x
  player.centery -=speed_y
  speed_x= 0
  speed_y =0

#Add Movements
def move_up():
  global speed_y
  speed_y = 5

#Add Movements
def move_down():
  global speed_y
  speed_y = -5

#Movement
def move_right():
  global speed_x
  speed_x = 5

def move_left():
  global speed_x
  speed_x = -5

score = 0

list_of_coins = []
for i in range(100):
  list_of_coins.append(Coin())

# Check Collision For Each Coin
def collision_loop():
  global list_of_coins
  global player
  global score

  # For each coin in game
  for coin in list_of_coins:
    # If collided rectangles and is not already hidden
    if player.colliderect(coin.rect) and coin.isHidden == False:
      # Hide and add 1 to score
      coin.isHidden = True
      score += 1

def render_coin_loop(screen):
  global list_of_coins
  global YELLOW
  
  for coin in list_of_coins:
    if coin.isHidden == False:
      screen.fill(BLUE, coin.rect)

## SHOW TEXT ON SCREEN
pygame.font.init()
FONT = pygame.font.SysFont("freeserif", 36)

def main():
	global FONT,score
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit(0)
		pygame.event.pump()
		key = pygame.key.get_pressed()
		if key[K_UP]:
			move_up()
		if key[K_DOWN]:
			move_down()
		if key[K_LEFT]:
			move_left()
		if key[K_RIGHT]:				
			move_right()
		movement_loop()
		collision_loop()
		clock.tick(60)
		screen.fill(BLACK)
		screen.fill(RED,player)
		# Render Score
		screen.blit(FONT.render("Score: " + str(score), True, YELLOW),
		(20, 80))
    	# Get Time
		seconds = int(pygame.time.get_ticks() / 1000)
		screen.blit(FONT.render("Time: " + str(seconds), True, YELLOW),
		(640, 80))
		render_coin_loop(screen)
		pygame.display.flip()
	

main()


