'''
This challenge is about a simple card flipping solitaire game. You're presented
with a sequence of cards, some face up, some face down. You can remove any face 
up card, but you must then flip the adjacent cards (if any). The goal is to 
successfully remove every card. Making the wrong move can get you stuck.

In this challenge, a 1 signifies a face up card and a 0 signifies a face down 
card. We will also use zero-based indexing, starting from the left, to indicate 
specific cards. So, to illustrate a game, consider this starting card set.

0100110
I can choose to remove cards 1, 4, or 5 since these are face up. If I remove 
card 1, the game looks like this (using . to signify an empty spot):

1.10110
I had to flip cards 0 and 2 since they were adjacent. Next I could choose to 
remove cards 0, 2, 4, or 5. I choose card 0:

..10110
Since it has no adjacent cards, there were no cards to flip. I can win this 
game by continuing with: 2, 3, 5, 4, 6.

Supposed instead I started with card 4:

0101.00
This is unsolvable since there's an "island" of zeros, and cards in such 
islands can never be flipped face up.
'''

def flip(card_list):
    
    subresult = []
    result = []
    
    for i in range(len(card_list)):
        
        if (card_list[i] == 0):
            
            subresult = [i] + subresult
            
        else:
            
            if (i+1 < len(card_list)):
                
                card_list[i+1] = (card_list[i+1] + 1) % 2
                
            result = result + [i] + subresult
            subresult = []
            
    if (subresult == []):
        
        print(result)
        
    else:
        
        print("No solution")

def flips(card_input):
    flip([int(num) for num in card_input])

