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

    player_luck = 0
    play = ''
    card1 = Card()
    card1num = card1.cardnumber
    while play != 'done':
        print()
        
        print(f'The card is: {card1num}')
        hilochoice = input('Higher or lower? [h/l] ')
        card2 = Card()
        card2num = card2.cardnumber
        print(f'Next card: {card2num}')
        if card1num > card2num:
            if hilochoice.lower() == 'l':
                player_score = player_score + 100
                player_luck = 0
            else:
                player_score = player_score - 75
                player_luck = player_luck + 1

        
        elif card1num < card2num:
            if hilochoice.lower() == 'h':
                player_score = player_score + 100
                player_luck = 0
            else:
                player_score = player_score - 75
                player_luck = player_luck +1

        
        else:
            player_score = player_score + 0

        print(f'Your score is: {player_score}')
        if player_luck == 3:
            print('You have horrible luck...')
        else:
            bob = 'bob'

        if player_score > 0:
            play_again = input('Play again? [y/n] ')
            if play_again.lower() == 'y':
                card1num = card2num
            else:
                play = 'done'
        else:
            play = 'done'
        

    
main()
