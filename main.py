import random

user_Score = 0
cpu_Score = 0


def validation(user, cpu):
  if user == 'snake' and cpu == 'water':
    return 1, 0
  elif user == 'water' and cpu == 'snake':
    return 0, 1
  elif user == 'snake' and cpu == 'gun':
    return 0, 1
  elif user == 'gun' and cpu == 'snake':
    return 1, 0
  elif user == 'gun' and cpu == 'water':
    return 0, 1
  else:
    return 1, 0


while True:
  user_choice = int(
    input("Enter your choice among\n1. Snake\n2. Water\n3. Gun\n"))
  if user_choice == 1:
    choice = 'snake'
  elif user_choice == 2:
    choice = 'water'
  elif user_choice == 3:
    choice = 'gun'
  else:
    print("Enter from given options:\n")
    continue
  CPU_options = ('snake', 'water', 'gun')
  cpu_choice = random.choice(tuple(CPU_options))
  print(f"User move is {choice}")
  print(f"computer move is {cpu_choice}")
  if choice == cpu_choice:
    print("Round Tied")
    continue
  else:
    user_points, cpu_points = validation(choice, cpu_choice)
    if user_points == 1:
      print("Congrats Player has won, and earned 1 point")
    else:
      print("Sorry! CPU has won, you have earned 0 point")
    user_Score += user_points
    cpu_Score += cpu_points
  print(f"After the round Total points earned by Player is {user_Score}")
  print(f"After the round Total points earned by CPU is {cpu_Score}")
  cont = int(
    input(
      "Do you wish to continue? Enter '1' to continue or '0' to exit:    "))
  if cont == 1:
    continue
  else:
    break
