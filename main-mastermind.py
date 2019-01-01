print ("---MASTERMIND---")

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)

nums = [num1, num2, num3, num4]
tries = 0

#print nums

print("Guess the 4 numbers in as few tries possible. Numbers could be used twice.")

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
			print("Match!")
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
		break
