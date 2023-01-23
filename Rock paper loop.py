player1 = input("Player One: rock, paper, or scissors?")
player2 = input("Player Two: rock, paper, or scissors?")

def compare(player1, player2):
    if player1 == player2:
        #return is recommended here, but whats the difference witht hat and print?
        return("Tie!")
    elif player1 == 'rock':
        if player2 == 'scissors':
            return("Rock wins!")
        else:
            return("Player 2 wins!")
    elif player1 == 'paper':
        if player2 == 'rock':
            return("Paper wins!")
        else:
            return("Player 2 wins!")
    elif player1 == 'scissors':
        if player2 == 'paper':
            return('Scissors winsr!')
        else:
            return("Player 2 wins!")
    elif player1 or player2 == 'gun' or 'shoot':
        return('Nice try, but no.')
    else:
        return('Choose rock, paper, or scissors. Try again.')

print(compare(player1, player2))