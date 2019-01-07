from random import randint

num1 = randint(0, 9)
num2 = randint(0, 9)
num3 = randint(0, 9)
num4 = randint(0, 9)
num5 = randint(0, 9)
num6 = randint(0, 9)
tries = 1
play = "yes"

print("What is your name?")
name = raw_input(">")
print("Welcome to Mastermind, " + name + ".")

while "y" in play:
	print("           MENU            ")
	print("[1] EASY")
	print("[2] MEDIUM")
	print("[3] HARD")
	print("[4] HIGH SCORES")
	print("[5] EXIT")

	choice = raw_input(">")

	#easy difficulty
	if "1" in choice:

		hiscore = open("mmhiscore.txt", "a")

		#4 numbers to guess
		nums = [num1, num2, num3, num4]
		print("Guess the 4 numbers in as few tries as possible. Numbers could be used twice.")

		while True:
			stars = ""
			remaining_nums = nums[:]
			guess = raw_input(">")
			tries += 1
			if len(guess) != 4:
				print("You must guess 4 digits. Try again.")
			else:
				guess = [int(guess[0]), int(guess[1]), int(guess[2]), int(guess[3])]
				if nums == guess:
					print("You guessed all the numbers in the correct order in " + str(tries) + "tries!")
					hiscore.write(str(tries) + "	" + name)
					hiscore.write("\n")
					hiscore.close()
					print("Play again? (y/n)")
					play = raw_input(">")
					break

				if (guess[0] in nums) or (guess[1] in nums) or (guess[2] in nums) or (guess[3] in nums):
					if guess[0] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[0])
					if guess[1] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[1])
					if guess[2] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[2])
					if guess[3] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[3])
					print stars

				else:
					print("Wrong guess. Try again.")

			if stars == "****":
				print("You guessed all the numbers in " + str(tries) + " tries!")
				hiscore.write(str(tries) + "	" + name)
				hiscore.write("\n")
				hiscore.close()
				print("Play again? (y/n)")
				play = raw_input(">")
				break

	#medium difficulty
	elif "2" in choice:

		hiscore = open("mmhiscore.txt", "a")

		#5 numbers to guess
		nums = [num1, num2, num3, num4, num5]
		print("Guess the 5 numbers in as few tries as possible. Numbers could be used twice.")

		while True:
			stars = ""
			remaining_nums = nums[:]
			guess = raw_input(">")
			tries += 1
			if len(guess) != 5:
				print("You must guess 5 digits. Try again.")
			else:
				guess = [int(guess[0]), int(guess[1]), int(guess[2]), int(guess[3]), int(guess[4])]
				if nums == guess:
					print("You guessed all the numbers in the correct order in " + str(tries) + "tries!")
					hiscore.write(str(tries) + "	" + name)
					hiscore.write("\n")
					hiscore.close()
					print("Play again? (y/n)")
					play = raw_input(">")
					break

				if (guess[0] in nums) or (guess[1] in nums) or (guess[2] in nums) or (guess[3] in nums) or (guess[4] in nums):
					if guess[0] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[0])
					if guess[1] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[1])
					if guess[2] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[2])
					if guess[3] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[3])
					if guess[4] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[4])
					print stars

				else:
					print("Wrong guess. Try again.")

			if stars == "*****":
				print("You guessed all the numbers in " + str(tries) + " tries!")
				hiscore.write(str(tries) + "	" + name)
				hiscore.write("\n")
				hiscore.close()
				print("Play again? (y/n)")
				play = raw_input(">")
				break

	#hard difficulty
	elif "3" in choice:

		hiscore = open("mmhiscore.txt", "a")

		#6 numbers to guess
		nums = [num1, num2, num3, num4, num5, num6]
		print("Guess the 6 numbers in as few tries as possible. Numbers could be used twice.")

		while True:
			stars = ""
			remaining_nums = nums[:]
			guess = raw_input(">")
			tries += 1
			if len(guess) != 6:
				print("You must guess 6 digits. Try again.")
			else:
				guess = [int(guess[0]), int(guess[1]), int(guess[2]), int(guess[3]), int(guess[4]), int(guess[5])]
				if nums == guess:
					print("You guessed all the numbers in the correct order in " + str(tries) + "tries!")
					hiscore.write(str(tries) + "	" + name)
					hiscore.write("\n")
					hiscore.close()
					print("Play again? (y/n)")
					play = raw_input(">")
					break

				if (guess[0] in nums) or (guess[1] in nums) or (guess[2] in nums) or (guess[3] in nums) or (guess[4] in nums) or (guess[5] in nums):
					if guess[0] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[0])
					if guess[1] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[1])
					if guess[2] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[2])
					if guess[3] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[3])
					if guess[4] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[4])
					if guess[5] in remaining_nums:
						stars += "*"
						remaining_nums.remove(guess[5])
					print stars

				else:
					print("Wrong guess. Try again.")

			if stars == "******":
				print("You guessed all the numbers in " + str(tries) + " tries!")
				hiscore.write(str(tries) + "	" + name)
				hiscore.write("\n")
				hiscore.close()
				print("Play again? (y/n)")
				play = raw_input(">")
				break

	#high score
	elif "4" in choice:
		hiscore = open("mmhiscore.txt", "r")
		hiscore = hiscore.read()
		print hiscore

	elif "5" in choice:
		break

	else:
		print("Invalid input. Try again.")

print("Thank you for playing Mastermind. See you next time.")
