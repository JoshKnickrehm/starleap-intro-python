def rps():
    player_1 = input('Player 1: ')
    print(player_1)
    print(type(player_1))
    player_2 = input('Player 2: ')
    print(player_2)
    print(type(player_2))
    if player_1 == 'r' and player_2 == 's':
        print('Player 1 wins!')
    elif player_1 == 'r' and player_2 == 'p':
        print('Player 2 wins!')
    elif player_1 == 'p' and player_2 == 'r':
        print('Player 1 wins!')
    elif player_1 == 'p' and player_2 == 's':
        print('Player 2 wins!')
    elif player_1 == 's' and  player_2 == 'p':
        print('Player 1 wins!')
    elif player_1 == 's' and player_2 == 'r':
        print('Player 2 wins!')
    else:
        print('It is a tie!')

rps()