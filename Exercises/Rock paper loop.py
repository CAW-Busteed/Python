def compare(player1, player2):
    if player1 == player2:
        #return is recommended here, but whats the difference witht hat and print?
        return("Tie!")
    elif player1 == 'rock':
        if player2 == 'scissors':
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    elif player1 == 'paper':
        if player2 == 'rock':
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    elif player1 == 'scissors':
        if player2 == 'paper':
            return('Player 1 wins!')
        else:
            return("Player 2 wins!")
    elif player1 == 'gun' or player1 == 'shoot':
        return('Nice try, but no.')
    elif player2 == 'gun' or player2 == 'shoot':
        return('Nice try, but no.')
    else:
        return('Choose rock, paper, or scissors. Try again.')

def validate(x):
    #.split seperates string into elements
    if x in "gun shoot rock paper scissors quit".split():
        return x

CHOICES = "rock, paper, or scissors"

while True:
    #.strip removes open spaces from input.
    # p1 = validate(input("Player One: " + CHOICES + "? ").strip())
    # p2 = validate(input("Player Two: " + CHOICES + "? ").strip())
    #f-string can simplify the process
    p1 = validate(input(f"Player One {CHOICES}? ").strip())
    p2 = validate(input(f"Player Two {CHOICES}? ").strip())
    if p1 == 'quit' or p2 == 'quit':
        break
    elif p1 == None or p2 == None:
        print("invalid input")
        continue
    else:
        print(compare(p1, p2))