from random import choice

global Sequence, flag
Sequence = [[i, i + 1, i + 2] for i in range(2, 15)]


def freshDeck():
    index = ['Ace'] + [i for i in range(2, 11)] + ['Jack', 'Queen', 'King']
    suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    cards = [[i, j] for i in index for j in suit]
    return cards


def getInt():
    while True:
        try:
            n = int(input('\nEnter number of players(2-17) : '))
            if 1 < n < 18:
                break
        except ValueError:
            pass
    return n


def giveCards(cards):
    card1 = choice(cards)
    cards.remove(card1)

    card2 = choice(cards)
    cards.remove(card2)

    card3 = choice(cards)
    cards.remove(card3)

    give = [card1, card2, card3]
    return give


def convertToNumber(players):
    for j in players:
        for i in j:
            if type(i[0]) == str:
                if i[0] == 'Ace':
                    i[0] = 14
                elif i[0] == 'Jack':
                    i[0] = 11
                elif i[0] == 'Queen':
                    i[0] = 12
                elif i[0] == 'King':
                    i[0] = 13


def findDoubleSingle(player):
    cardIndex = [i[0] for i in player]
    if cardIndex[0] == cardIndex[1]:
        return [cardIndex[0], cardIndex[2]]
    elif cardIndex[0] == cardIndex[2]:
        return [cardIndex[2], cardIndex[1]]
    else:
        return [cardIndex[2], cardIndex[0]]


def draw(players, drawPlayers):
    if flag == 1:
        playerIndex = drawPlayers[0]
        winner = players[playerIndex]
        for i in drawPlayers:
            if winner[0][0] < players[i][0][0]:
                winner = players[i]
                playerIndex = i
        return playerIndex + 1

    elif flag == 2 or flag == 3:
        playerIndex = drawPlayers[0]
        winner = players[playerIndex]
        highest = [j[0] for j in winner]
        highest.sort()
        highest = highest[0]
        ans = [playerIndex]
        for i in drawPlayers[1:]:
            cardIndex = [j[0] for j in players[i]]
            cardIndex.sort()
            if cardIndex[0] > highest:
                highest = cardIndex[0]
                ans = [i]
            elif cardIndex[0] == highest:
                ans.append(i)
        if len(ans) == 1:
            return ans[0] + 1
        else:
            ans = [i+1 for i in ans]
            return ans

    #Same as isHigh()
    elif flag == 4:
        cards = {}
        for i in drawPlayers:
            cardIndex = [players[i][0][0], players[i][1][0], players[i][2][0]]
            cardIndex.sort(reverse=True)
            cards[i] = cardIndex
        allIndex = [(cards[i]) for i in cards]
        for i in range(3):
            allIndex = checkHighest(allIndex, i)
            if len(allIndex) == 1:
                for j in cards:
                    if cards[j] == allIndex[0]:
                        return j + 1
        ans = []
        for i in allIndex:
            for j in cards:
                if i == cards[j]:
                    ans.append(j + 1)
        return ans

    elif flag == 5:
        winnerIndex = [drawPlayers[0]]
        doubleSingle = findDoubleSingle(players[drawPlayers[0]])
        for i in drawPlayers[1:]:
            d = findDoubleSingle(players[i])
            if d[0] > doubleSingle[0] or (d[0] == doubleSingle[0] and d[1] > doubleSingle[1]):
                winnerIndex = [i]
                doubleSingle = d
            elif d[0] == doubleSingle[0] and d[1] == doubleSingle[1]:
                winnerIndex.append(i)
        if len(winnerIndex) == 1:
            return winnerIndex[0] + 1
        else:
            winnerIndex = [i+1 for i in winnerIndex]
            return winnerIndex


def isWinner(players, score):
    scores = [score[i] for i in score]
    maxScore = max(scores)
    x = scores.count(maxScore)
    if x == 1:
        for i in score:
            if score[i] == maxScore:
                return i + 1
    elif maxScore != 0:
        drawPlayers = []
        for i in score:
            if score[i] == maxScore:
                drawPlayers.append(i)
        return draw(players, drawPlayers)


def isTrio(players, score):
    for i in range(len(players)):
        if players[i][0][0] == players[i][1][0] == players[i][2][0]:
            score[i] += 1


def isPureSequence(players, score):
    for i in range(len(players)):
        x = players[i][0][1] == players[i][1][1] == players[i][2][1]
        if x:
            seq = [players[i][0][0], players[i][1][0], players[i][2][0]]
            seq.sort()
            y = False
            if seq in Sequence:
                y = True
            if y:
                score[i] += 1


def isSequence(players, score):
    for i in range(len(players)):
        seq = [players[i][0][0], players[i][1][0], players[i][2][0]]
        seq.sort()
        y = False
        if seq in Sequence:
            y = True
            break
        if y:
            score[i] += 1


def isColour(players, score):
    for i in range(len(players)):
        if players[i][0][1] == players[i][1][1] == players[i][2][1]:
            score[i] += 1


def isDouble(players, score):
    for i in range(len(players)):
        if players[i][0][0] == players[i][1][0] \
                or players[i][1][0] == players[i][2][0] \
                or players[i][0][0] == players[i][2][0]:
            score[i] += 1


def checkHighest(allIndex, n):
    highest = allIndex[0][n]
    for i in allIndex:
        if i[n] > highest:
            highest = i[n]
    for i in allIndex.copy():
        if i[n] < highest:
            allIndex.remove(i)
    return allIndex


def isHigh(players):
    cards = {}
    for i in range(len(players)):
        cardIndex = [players[i][0][0], players[i][1][0], players[i][2][0]]
        cardIndex.sort(reverse=True)
        cards[i] = cardIndex
    allIndex = [(cards[i]) for i in cards]
    for i in range(3):
        allIndex = checkHighest(allIndex, i)
        if len(allIndex) == 1:
            for j in cards:
                if cards[j] == allIndex[0]:
                    return j + 1
    ans = []
    for i in allIndex:
        for j in cards:
            if i == cards[j]:
                ans.append(j + 1)
    return ans


def findWinner(players):
    global flag
    score = {i: 0 for i in range(len(players))}

    flag = 1
    isTrio(players, score)
    ans = isWinner(players, score)
    if ans:
        print('Type of hand : Trio')
        return ans

    flag = 2
    isPureSequence(players, score)
    ans = isWinner(players, score)
    if ans:
        print('Type of hand : PureSequence')
        return ans

    flag = 3
    isSequence(players, score)
    ans = isWinner(players, score)
    if ans:
        print('Type of hand : Sequence')
        return ans

    flag = 4
    isColour(players, score)
    ans = isWinner(players, score)
    if ans:
        print('Type of hand : Colour')
        return ans

    flag = 5
    isDouble(players, score)
    ans = isWinner(players, score)
    if ans:
        print('Type of hand : Double')
        return ans

    ans = isHigh(players)
    if type(ans) == int:
        print('Type of hand : High')
        return ans
    else:
        print('Draw')
        return ans
