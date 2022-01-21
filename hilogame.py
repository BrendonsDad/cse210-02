

# import random
# player_score = 300
# play = ''
# while play != 'done':
#     print()
#     cardnum1 = random.randint(1,14)
#     print(f'The card is: {cardnum1}')
#     playernum = input('Higher or lower? [h/l] ')
#     cardnum2 = random.randint(1, 14)
#     print(f'Next card was: {cardnum2}')
#     if cardnum1 > cardnum2:
#         if playernum.lower() == 'l':
#             player_score = player_score + 100
#         else:
#             player_score = player_score - 75
    
#     elif cardnum1 < cardnum2:
#         if playernum.lower() == 'h':
#             player_score = player_score + 100
#         else:
#             player_score = player_score - 75
    
#     else:
#         player_score = player_score + 0

#     print(f'Your score is: {player_score}')

#     if player_score > 0:
#         play_again = input('Play again? [y/n] ')
#         if play_again.lower() == 'y':
#             bob = 'bob'
#         else:
#             play = 'done'
#     else:
#         play = 'done'
