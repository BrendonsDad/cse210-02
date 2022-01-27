from card import Card
from player import Player

class Director:

    def __init__(self):
        
        self.player_luck = 0
        self.play = ''

    def playgame(self):

        player = Player()
        player_score = player.score

        card1 = Card()
        card1num = card1.cardnumber
        gamespecs = Director()
        player_luck = gamespecs.player_luck
        play = gamespecs.play

        def generate_scores(card1num, card2num, hilochoice, player_score, player_luck):
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

            cardsandscores = [card1num, card2num, hilochoice, player_score, player_luck]
            return cardsandscores



        while play != 'done':
            print()
            
            print(f'The card is: {card1num}')
            hilochoice = input('Higher or lower? [h/l] ')
            card2 = Card()
            card2num = card2.cardnumber
            print(f'Next card: {card2num}')

            cardsandscores = generate_scores(card1num, card2num, hilochoice, player_score, player_luck)
            card1num = cardsandscores[0]
            card2num = cardsandscores[1]
            hilochoice = cardsandscores[2]
            player_score = cardsandscores[3]
            player_luck = cardsandscores[4]
            

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
        

    

