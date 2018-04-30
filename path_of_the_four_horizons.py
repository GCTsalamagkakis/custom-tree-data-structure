import pygame
import json

pygame.init()

screenx = 1100
screeny = 750

gameDisplay = pygame.display.set_mode((screenx, screeny))

white = (255, 255, 255)
purple = (183, 166, 173)
light_purple = (211, 201, 206)

pygame.display.set_caption("Path Of The Four Horizons")

def text_objects(text, font):
	textSurface = font.render(text, True, (0, 0, 0))
	return textSurface, textSurface.get_rect()

def message_display(text):
	message = pygame.font.SysFont('gabriola', 35)

	pos1 = len(text)//3
	if text[pos1] != " ":
		while text[pos1] != " ":
			pos1 += 1

	pos2 = pos1 + len(text)//3
	try:
		if text[pos2] != " ":
			while text[pos2] != " ":
				pos2 += 1
	except BaseException:
		pass

	textSurf, textRect = text_objects(text[:pos1], message)
	textRect.center = (screenx/2, screeny/(2+0.4))
	gameDisplay.blit(textSurf, textRect)

	textSurf, textRect = text_objects(text[pos1:pos2], message)
	textRect.center = (screenx/2, screeny/(2+0.2))
	gameDisplay.blit(textSurf, textRect)

	try:
		textSurf, textRect = text_objects(text[pos2:], message)
		textRect.center = (screenx/2, screeny/2)
		gameDisplay.blit(textSurf, textRect)
	except BaseException:
		pass

def button(msg, buttonx, width, buttony, height, nrm_color, light_color, action=None, current_state=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if buttonx+width > mouse[0] > buttonx and buttony+height > mouse[1] > buttony:
		pygame.draw.rect(gameDisplay, light_color, (buttonx, buttony, width, height))
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if current_state == 'quit':
						pygame.quit()
						quit()
					else:
						action(current_state)
	else:
		pygame.draw.rect(gameDisplay, nrm_color, (buttonx, buttony, width, height))

	smallText = pygame.font.SysFont("gabriola", 25)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = (buttonx+width/2, buttony+height/2)
	gameDisplay.blit(textSurf, textRect)


def main_menuTXT(current=None):
	
	while True:
		gameDisplay.fill(white)

		if current is None:
			global story
			story = {}

			with open('storif_testing.txt') as f:
				for i, line in enumerate(f):
					line = line.strip()
					if line:
						info = line.split('\\t')
						story[info[0]] = [part for part in info]

			for key in story:

				if story[key][-2] == 'True':
					current = key

		message = story[current][2]
			
		message_display(message)
		
		for i in range(int(story[current][1])):
			button(story[current][4+int(story[current][1])+i], (screenx/int(story[current][1]))*(i+1)-(screenx/(2*int(story[current][1])))-50, 100, 550, 50, purple, light_purple, main_menuTXT, story[current][4+i])

		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

def main_menuJSON(current=None):
	while True:
		gameDisplay.fill(white)

		if current is None:
			global data
			data = json.load(open('json.json'))
			for block in data:
				if data[block]["isStarting"]:
					current = data[block]["id"]
		
		message = data[current]["text"]
		message_display(message)

		for i in range(len(data[current]["children"])):
			button(data[current]["buttonText"][i], (screenx/len(data[current]["children"]))*(i+1)-(screenx/(2*len(data[current]["children"])))-50, 100, 550, 50, purple, light_purple, main_menuJSON, data[current]["children"][i])

		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

def main_menuDB(current=None):
	pass

def dataImport():
	while True:
		gameDisplay.fill(white)

		message = "Before You Dive Into Your Adventure, Tell Me Traveler, Where Will I Get Your Story From?"
		buttons = [".txt", ".json", "Database"]
		choices = [main_menuTXT, main_menuJSON, main_menuDB]

		message_display(message)

		for i in range(len(buttons)):
			button(buttons[i], ((screenx)/len(buttons))*(i+1)-(screenx/(2*len(buttons)))-50, 100, 550, 50, purple, light_purple, choices[i], None)

		pygame.display.update()
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

dataImport()
