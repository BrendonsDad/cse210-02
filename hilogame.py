import random

class Player:
    def __init__(self):
        self.score = 300
    
    
class Card:
    def __init__(self):
        self.cardnumber = random.randint(1, 14)

def main():
    player = Player()
    player_score = player.score

    play = ''
    while play != 'done':
        print()
        card1 = Card()
        card1num = card1.cardnumber
        print(f'The card is: {card1num}')
        hilochoice = input('Higher or lower? [h/l] ')
        card2 = Card()
        card2num = card2.cardnumber
        print(f'Next card: {card2num}')
        if card1num > card2num:
            if hilochoice.lower() == 'l':
                player_score = player_score + 100
            else:
                player_score = player_score - 75
        
        elif card1num < card2num:
            if hilochoice.lower() == 'h':
                player_score = player_score + 100
            else:
                player_score = player_score - 75
        
        else:
            player_score = player_score + 0

        print(f'Your score is: {player_score}')

        if player_score > 0:
            play_again = input('Play again? [y/n] ')
            if play_again.lower() == 'y':
                bob = 'bob'
            else:
                play = 'done'
        else:
            play = 'done'
        

    
main()

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
