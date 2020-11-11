import random, sys
print('ROCK, PAPER, SCISSORS')

# Variables keep track of wins, losses and ties.
wins = 0
losses = 0
ties = 0
yay = 'You win!'

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit() # Quit Program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out the input.
        print('Type one of r, p, s or q.')

    # Display player's choice
    if player_move == 'r':
        print('Rock versus...')
    elif player_move == 'p':
        print('Paper versus...')
    elif player_move == 's':
        print('Scissors versus...')
        
        # Display the computers' choice

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')
    
        # Display and record the win/loss/tie:

    if player_move == computer_move:
        print('It\'s a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print(yay)
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print(yay)
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print(yay)
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif  player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You loss!')
        losses = losses + 1 