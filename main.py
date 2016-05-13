import random
def main():
	win = 0
	loss = 0
	tie = 0
	print ("welcome to RPS")
	print ("Lets Begin!")
	usernum = user()
	compnum = computer()
	results(compnum, usernum, win, loss, tie)


def computer():
	compnum = random.randrange(1,6)
	if compnum == 1:
		print ("computer chooses Rock")
	elif compnum == 2:
		print ("computer chooses Paper")
	elif compnum == 3:
		print ("computer chooses Scissors")
	elif compnum == 4:
		print("computer chooses Lizard")
	elif compnum == 5:
		print("computer chooses Spock")
	return compnum

def user():
	guess = input("Choose 'rock', 'paper', 'scissors', 'lizard', 'spock' by typing the word.")
	if valid(guess):
		if guess == 'rock':
			usernum = 1
		elif guess == 'paper':
			usernum = 2
		elif guess == 'scissors':
			usernum = 3
		elif guess == 'lizard':
			usernum = 4
		elif guess == 'spock':
			usernum = 5
		return usernum
	else:
		print("Invalid choice")
		return user()

def valid(guess):
	if guess in ('rock', 'paper', 'scissors', 'lizard', 'spock'):
		status = True
	else:
		status = False
	return status

def restart(win, tie, loss):
	answer = input("would you like to play again? Y/N: ")
	print (answer)
	if answer.lower() == "y":
		main()
	elif answer.lower() == "n":
		print("Goodbye.")
		print("Total Wins = ", win)
		print("Total Losses = ", loss)
		print("Total Ties = ", tie)
	else:
		print("Invalid, type Y or N")
		restart()

def results(compnum, usernum, win, loss, tie):
	difference = compnum - usernum
	if difference == 0:
		print ("Tie")
		tie += 1
	elif difference % 5 == 2 or difference % 5 == 4:
		print ("Sorry you lose.")
		loss += 1
	elif difference % 5 == 3 or difference % 5 == 1:
		print ("Congratulations you win!")
		win += 1
	restart(win,tie,loss)

main()