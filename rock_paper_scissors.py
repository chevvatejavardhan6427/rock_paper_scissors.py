import random
options=["rock","paper","scissors"]
for e in options:
	print(e,end=" ")
print()
no_option=0
won=0
while True:
	computer=random.choice(options)
	option=input("choose any one of the option from above options(q to quit) : ").lower()
	no_option+=1
	if option in options:
		if (option == "rock" and computer == "scissors") or (option == "paper" and computer == "rock") or (option == "scissors" and computer == "paper"):
			print('"CONGRATULATIONS!" YOU WON!')
			won += 1

		elif option==computer:
			print('DRAW!')
		else:
			print("sorry! you have lost the game")
	elif option.lower()=="q":
		break
	else:
		print("you have chosen invalid option")
		continue
		
print(f"you have won {won} times out of {no_option-1}")
print(f"your win percentage = {(won/(no_option-1)*100):.2f}%")
