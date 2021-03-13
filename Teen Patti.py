from src import*


while True:
    currentDeck = freshDeck()
    n = getInt()
    players = []
    for i in range(n):
        cards = giveCards(currentDeck)
        players.append(cards)
        print(f'''
Cards of player {i+1} : 
{cards[0][0]} of {cards[0][1]}
{cards[1][0]} of {cards[1][1]}
{cards[2][0]} of {cards[2][1]} ''')

    convertToNumber(players)

    input('\nPress Enter to Reveal Winner : \n')
    winner = findWinner(players)
    if type(winner) == int:
        print(f'Winner is player {winner}')
    else:
        winner = list(set(winner))
        winner.sort()
        out = 'Draw between'
        for i in winner:
            out += ' player ' + str(i)
        print(out)
    Again = input('\nPlay Again ([y]/n) : ').lower()
    if Again == 'n' or n == 'no':
        break

