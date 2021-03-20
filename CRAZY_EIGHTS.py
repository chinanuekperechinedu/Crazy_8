# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:02:21 2020

@author: Chinanu
"""
from random import shuffle
from random import choice
import time


ranks = list(map(str, range(2, 11))) + ["A", "J", "Q", "K"]

suits = {'Spades':'\u2660', 'Club':'\u2663', 'Heart':'\u2665', 'Diamond':'\u2666'}
    
def create_deck():
    deck = []        
    for rank in ranks:
        for suit in suits:
            deck.append(rank + suits[suit])

    shuffle(deck)
    return deck

def distribute_card(deck):    
    card = []
    for i in range(5):
        card.append(deck.pop())
    return card


def gameInstruction():
    
    instruction = ("\nRULES OF CRAZY EIGHTS\nAt each turn, a player has to do one of the following:\n"+
    
    "1. Play a card that matches the rank or suit of the card at the top of the discard pile.\n"+
    
    "2. If a player plays an 8, he can 'call a suit', which means he gets to choose the suit that the next player is trying to match.\n"+

    "3. If a player cannot play any of his cards, he must pick up a card from the deck and add it to his hand.\n"+

    "4. If a player gets rid of all his cards, he wins the game\n"+

    "5. If the deck runs out and no one can make a play, the game is over. In that case, the player whose cards have the lesser number of points win.\n"+

    "6. If both players have the same number of points, it is a draw.\n" +
    
    "7. To review the instruction at any point in the game enter '--help'\n")
    
    print(instruction)


def getTopCard(deck):
    card = deck.pop()
    
    while '8' in card.strip():
        deck.append(card)
        shuffle(deck)
        card = deck.pop()
    return card

def availableCards(playerCards, selection, name):
    crd = []
    print(name + ": " + selection.format("card") + "\nEnter:")
    count = 1
    for card in playerCards:
        options = "\t{} to play -> {}".format(count, card)
        print(options)
        count += 1
        crd.append(options)
                
    return crd
    
def getCard(selected_card, options):
    sCard = ""
    for option in options:
        if selected_card == option.split()[0]:
            sCard = option.split()[-1]
            break
    return sCard.strip()

def computer_choice(player_hand, tp_card):
    selected_card = ""
    matched_card = []
    cardz = []
    for hand in player_hand:
        for rs in tp_card:
            if rs in hand:
                matched_card.append(hand)
                
    for card in matched_card:
        if '8' in card or 'K' in card or 'J' in card or 'Q' in card or '10' in card:
            selected_card = card
            return selected_card
        elif 'A' not in card:
            cardz.append(card)
        else:
            selected_card = card
            return selected_card
    
    selected_card = max(cardz)
    return selected_card

#\n
class Player:
    
    choice_object = "Choose your preferred {}."    
    
    def __init__(self, name, hand = []):
        self.name = name
        self.hand = hand        
        self.score = self.setScore()
#        self.requestSuit = self.request_suit(suits)
        
#        print("score: {}".format(self.score))
#        self.money = 
        
    def __str__(self):
        currentHand = ""        
        for card in self.hand:
            currentHand += str(card) + " "  
        return currentHand  
    
    def setScore(self):
        self.score = 0
        
        faceCardsDict = {"A": 1, "J":10, "Q":10, "K":10}
        
        for card in self.hand:
            if card[0].isdigit():
                if int(card[0]) == 8:
                    self.score  += 50
                else:
                    self.score += int(card[0])
            else:
                self.score += faceCardsDict[card[0]]
        return self.score
    
    def playCard(self, card, t_card):
        print(self.name, "played", card)
        t_card = card
        self.hand.remove(card)
        return t_card

    def drawCard(self, deck):
        card = deck.pop()
        if self.name == 'Computer':
            print(self.name, 'picked card'+ "\n")
        else:
            print(self.name, "picked", card)
        self.hand.append(card)
        
    def request_suit(self, suits):        
        suit_choice = ""

        suit_list = []      
        
        if self.name == 'Computer':
            print(self.choice_object.format("suit"))
            suit_choice = choice([s + "(" + suits[s] + ")" for s in suits ])
        else:
            print(self.choice_object.format("suit") + "\nEnter:")
            count = 1
            for suit in suits:
                options = "\t{} to play -> {}({})".format(count, suit, suits[suit])
                print(options)
                count += 1
                suit_list.append(options)
            while suit_choice.isdigit() == False or suit_choice > str(len(suits)) or suit_choice <= '0':
                suit_choice = input('Enter Choice: ').strip()
                
                if suit_choice == '--help':
                    gameInstruction()
                    continue

            suit_choice = [suit.split()[-1]  for suit in suit_list if suit_choice == suit.split()[0]][0]
        
        top_card = suit_choice[suit_choice.find("(") + 1 : suit_choice.find(")")]

        return top_card            


def crazyEightGame(player, tcard_msg, top_card):  
        
    print(player.name + "'s", "turn")
    
    suit_request = ''
    
    if player.name is not 'Computer':
        print(player.name + ": " + player.__str__())
        
    if player.name is'Computer':
        print(player.name + " is thinking...." )
        time.sleep(4)
    
    selected_card = 'XX'

    if any(c in cd for c in top_card  for cd in player.hand):       
        
        pick = ''
        
        while pick.lower().strip() != 'y' and pick.lower().strip() != 'n':
            
#            print(tcard_msg, top_card)
            
            if player.name == 'Computer': 
                pick = 'n'
            else:                
                pick = input('Would you like to draw from Card Deck (y/n)? ')
                
                if pick.strip() == '--help':
                    gameInstruction()
                    continue
                
            
        if pick.lower().strip() == 'y':
            player.drawCard(card_deck)
#            print(tcard_msg, top_card)
        else:            
            availableOptions = []
            while selected_card not in availableOptions:
                try:             
                    
                    if player.name == 'Computer':                        
                        selected_option = computer_choice(player.hand, top_card)
                        top_card = player.playCard(selected_option, top_card)
                        
                        if len(player.hand) == 1:
                            print("\n"+ player.name + ": LAST CARD................")
                        
                        if len(player.hand) == 0:                            
                            top_card = '0'
                            return top_card
                            
                        if '8' in top_card:
                            suit_request = player.request_suit(suits)
                            top_card = suit_request
                            break

                        break
                    else:
                        availableOptions = availableCards(player.hand, player.choice_object, player.name)
                        selected_option = input("Enter Choice: ").strip()
                        
                        if selected_option == '--help':
                            gameInstruction()
                            continue
                                            
                        if any(selected_option == option.split()[0] for option in availableOptions):
                            selected_card = getCard(selected_option.strip(), availableOptions)
                        else:
                            print("\nInvalid Choice.")
                            continue
                    
                        if any(tc in sc for tc in top_card for sc in selected_card):                        
                            top_card = player.playCard(selected_card, top_card)
                            
                            if len(player.hand) == 1:
                                print("\n"+ player.name + ": LAST CARD................")
                            
                            if len(player.hand) == 0:
                                top_card = '0'
                                return top_card
                            
                            print(tcard_msg, top_card)
                            if '8' in selected_card:
                                suit_request = player.request_suit(suits)
                                top_card = suit_request
                                
                            break
                        else:     
                            print(tcard_msg, top_card)
                            print("\nInvalid choice: Card choice does not match face up card on dischard pile.\n")
                            selected_card = ""
                except:
                    continue
                
    else:        
        while selected_card != 'y':
            if player.name == 'Computer':
                selected_card = 'y'
            else:
                selected_card = input(player.name +", you do not have any matching card.\nKindly enter 'y' to draw from Card Deck: ")
                if selected_card == '--help':
                    gameInstruction()
                    continue
                
            if (selected_card.lower().strip() == 'y'):
                player.drawCard(card_deck)
   
    if len(player.hand) != 0:           
        if player.name is not 'Computer':
            print(player.name + ": " + player.__str__())
        
        if suit_request != "":        
            print( '\n' + player.name,"requests for:", suit_request, '\n')
        else:
            print( '\n' + "Top Card on discard pile:", top_card, '\n')
    
    return top_card
    

if __name__ == '__main__':
    
    print("\nGAME: CRAZY EIGHTS")
    time.sleep(3)
    
    gameInstruction()
    
    player_name = ''
    
    while player_name.strip() == "" or player_name.strip() == '--help':
        if player_name.strip() == '--help':
            gameInstruction()
        player_name = input("Enter name: ")
    
    Computer = "Computer"
    
    card_deck = create_deck()
    
    print("\n" + player_name, "vs", Computer)

    firstHand = distribute_card(card_deck)
#    firstHand = firstHand.append('10♣')
    
    secondHand = distribute_card(card_deck)

    top_card = getTopCard(card_deck)    
    
    tcard_msg = '\nTop card on discard Pile:'
    
    print(tcard_msg, top_card + '\n')   
    
    player1 = Player(player_name, firstHand)
    
    computer = Player(Computer, secondHand)
    
    turn = 0
    
    while True:
        
        if turn % 2 == 0:
            player = player1
        else:
            player = computer
        turn += 1
        top_card = crazyEightGame(player, tcard_msg, top_card)
        
        if top_card == '0':
            print("\nGame over\n" + "\n"+player.name,"WON!!!\n")
            break
        
        if len(card_deck) == 0 and top_card != 0:
            p1 = player1.setScore()
            com = computer.setScore()
            
            print(player1.name + ": " + str(p1))
            print(computer.name + ": " + str(com))
            
            if p1 > com:
                print("\nGame over\n" + "\n"+computer.name,"WON!!!\n")
            elif p1 == com:
                print("\nGame over\n" + "\nThis is a draw, nobody WON!!!\n")
            else:
                print("\nGame over\n" + "\n"+p1.name,"WON!!!\n")                
            break
    time.sleep(15)
    input("Press ENTER to exit")
       
    
    


