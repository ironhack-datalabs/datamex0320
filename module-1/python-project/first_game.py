


# Initiate pygame and create window



monkey_mr = pygame.image.load('images/monkey_r.png')
monkey_mr = pygame.transform.rotozoom(monkey_mr, 0 , 1/5)

monkey_ml = pygame.image.load('images/monkey_l.png')
monkey_ml = pygame.transform.rotozoom(monkey_ml, 0 , 1/5)

player_image = monkey_mr


player_location = [0,0]
vertical_momentum = 0
player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())


moving_right = False
moving_left = False 
true_scroll = [0,0]



while True: 

	window.blit(player_image, player_location)

	true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
	true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
	scroll = true_scroll.copy()
	scroll[0] = int(scroll[0])
	scroll[1] = int(scroll[1])

	if player_location[1] > WINDOW_SIZE[1] - player_image.get_height():
		vertical_momentum = -vertical_momentum
	else:
		vertical_momentum += 0.01



	if moving_right == True:
		player_location[0] += 2
	if moving_left == True:
		player_location[0] -= 2
	player_location[1] += vertical_momentum
	vertical_momentum += 0.0
	if vertical_momentum > 3:
		vertical_momentum = 3


	player_rect.x = player_location[0]
	player_rect.y = player_location[1]





	pygame.display.update() # Update display
