import os
import time
from pyfiglet import Figlet

import game

correct = ['Moscow','Yuan','Tiger','1024','Asia']

def display(msg,style):
	f = Figlet(font=style)
	print('\n'*10)
	print(f.renderText(msg))

def getScore(solutions,userSolution):
	score = 0
	for s,u in zip(solutions,userSolution):
		if s == u:
			score += 1

	return score

# ------------------------- Game start -----------------------------
while True:
	os.system('cls')
	display("     Quiz Game","slant")
	print('\n'*5)
	print('\t\t Press Space to start the game, q to exit ')

	ch = input('')

	if ch == ' ':
		os.system('cls')

		# ------------------------- Game Play ------------------------------
		print('\n'*2)
		print('    X ------------- Quiz Game ------------- X')
		print('\n'*2)

		userAnswers = game.main()
		time.sleep(1)

		# -------------------------- Game End ------------------------------
		user = [j for j in userAnswers.values()]
		score = getScore(correct,user)
		os.system('cls')
		display(f"     Your      Score : {score}","banner3-D")
		time.sleep(4)

	elif ch == 'q':
		break