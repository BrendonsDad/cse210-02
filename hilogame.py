from card import Card
from player import Player

card = Card()
class Director:
    def __init__(self):
        self.player_luck = 0
        self.play = ''
    def playgame(self):
        ## Makes a new player so we can keep their score
        player = Player()
        player_score = player.score
        ## Calls the card class so we can generate the 
        ## first card
        card1 = Card()
        card1num = card1.card1num
        gamespecs = Director()
        player_luck = gamespecs.player_luck
        play = gamespecs.play
        def generate_scores(card1num, card2num, hilochoice, player_score, player_luck):
            ## This function will check their answers, and
             ## see if they guessed correctly. If they did,
             ## it will reward them with 100 points. If not, 
             ## they lose 75 points. Also include code for 
             ## the easter egg which will tallies each time
             ## they guess wrong but resets when they guess 
             ## right
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
            ## Returns a list of all needed answers
            return cardsandscores
        while play != 'done':
            print()
            print(f'The card is: {card.card1num_card_suit}{card1num}')
            hilochoice = input('Higher or lower? [h/l] ')
            card2 = Card()
            card.draw_card()
            card2num = card2.card2num
            print(f'Next card: {card.card1num_card_suit}{card2num}')
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






# class Director:

#     def __init__(self):
        
#         self.player_luck = 0
#         self.play = ''

#     def playgame(self):

#         ## Makes a new player so we can keep their score
#         player = Player()
#         player_score = player.score

#         ## Calls the card class so we can generate the 
#         ## first card
#         card1 = Card()
#         card1num = card1.card1num
#         ## Calls the Director class so we can have some
#         ## variables needed to start the game
#         gamespecs = Director()
#         player_luck = gamespecs.player_luck
#         play = gamespecs.play

#         def generate_scores(card1num, card2num, hilochoice, player_score, player_luck):
#             ## This function will check their answers, and
#             ## see if they guessed correctly. If they did,
#             ## it will reward them with 100 points. If not, 
#             ## they lose 75 points. Also include code for 
#             ## the easter egg which will tallies each time
#             ## they guess wrong but resets when they guess 
#             ## right
#             if card1num > card2num:
#                 if hilochoice.lower() == 'l':
#                     player_score = player_score + 100
#                     player_luck = 0
#                 else:
#                     player_score = player_score - 75
#                     player_luck = player_luck + 1

            
#             elif card1num < card2num:
#                 if hilochoice.lower() == 'h':
#                     player_score = player_score + 100
#                     player_luck = 0
#                 else:
#                     player_score = player_score - 75
#                     player_luck = player_luck +1

            
#             else:
#                 player_score = player_score + 0

#             ## Returns a list of all needed answers
#             cardsandscores = [card1num, card2num, hilochoice, player_score, player_luck]
#             return cardsandscores



#         while play != 'done':
#             print()
            
#             print(f'The card is: {card1num}')
#             hilochoice = input('Higher or lower? [h/l] ')
#             card2 = Card()
#             card2num = card2.cardnumber
#             print(f'Next card: {card2num}')

#             cardsandscores = generate_scores(card1num, card2num, hilochoice, player_score, player_luck)
#             card1num = cardsandscores[0]
#             card2num = cardsandscores[1]
#             hilochoice = cardsandscores[2]
#             player_score = cardsandscores[3]
#             player_luck = cardsandscores[4]
            

#             print(f'Your score is: {player_score}')
#             if player_luck == 3:
#                 print('You have horrible luck...')
#             else:
#                 bob = 'bob'

#             if player_score > 0:
#                 play_again = input('Play again? [y/n] ')
#                 if play_again.lower() == 'y':
#                     card1num = card2num
#                 else:
#                     play = 'done'
#             else:
#                 play = 'done'
        

    

