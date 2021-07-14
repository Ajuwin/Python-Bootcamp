import random

computer_choices = ['Rock', 'Paper', 'Scissor']
target_points = 5
print("Enter 'r' for Rock, 'p' for Paper, 's' for Scissor, 'q' for Quit")
print("Target Point: 10")

computer_points = 0
user_points = 0


while True:
    print(f'\nUser point: {user_points}\nComputer point: {computer_points}')
    if computer_points == target_points:
        print('\nComputer Won!!\n')
        break

    elif user_points == target_points:
        print('\nYou Won!!\n')
        break
    
    else:
        computer_choice = random.choice(computer_choices)
        user_choice = input("Enter your choice: ").lower()         

        if user_choice.lower() == 'q':
            break
        print(f'Computer: {computer_choice}')
            
        if ((computer_choice == 'Rock') and (user_choice == 'r')) or ((computer_choice == 'Scissor') and (user_choice == 's')) or ((computer_choice == 'Paper') and (user_choice == 'p')):
            print('Same choice....')

        elif ((computer_choice == 'Rock') and (user_choice == 's')) or ((computer_choice == 'Scissor') and (user_choice == 'p')) or ((computer_choice == 'Paper') and (user_choice == 'r')):
            computer_points += 1
            print("Computer +1")
            
        elif ((computer_choice == 'Scissor') and (user_choice == 'r')) or ((computer_choice == 'Rock') and (user_choice == 'p')) or ((computer_choice == 'Paper') and (user_choice == 's')):
            user_points += 1
            print("User +1")

        else:
            print('Enter right choice..')

