import sys
from copy import deepcopy

players = []
sys.stdin.readline()
deck = []
for line in sys.stdin:
    if (line == '\n'):
        players.append(deck)
        deck = []
        sys.stdin.readline()
    else:
        deck.append(int(line))

def combat(players, verbose=False):
    while(len(players[0]) and len(players[1])):
        if (verbose):
            print("Player1 deck: ", players[0])
            print("Player2 deck: ", players[1])
        p1 = players[0].pop(0)
        p2 = players[1].pop(0)
        if (verbose):
            print("Player1 play: ", p1)
            print("Player2 play: ", p2)
        if (p1 > p2):
            if (verbose):
                print("Player1 wins!\n")
            players[0].append(p1)
            players[0].append(p2)
        else:
            if (verbose):
                print("Player2 wins!\n")
            players[1].append(p2)
            players[1].append(p1)

    deck = players[0] + players[1]
    print("Part one")
    score = 0
    for i, val in enumerate(reversed(deck)):
        score += (i + 1) * val
    print("Score: ", score)

combat(deepcopy(players))

def recurscombat(players):
    cache = set()
    while(len(players[0]) and len(players[1])):
        configuration = (*players[0], 0, *players[1])
        if (configuration in cache):
            return 1, players[0]
        else:
            cache.add(configuration)
            p1 = players[0].pop(0)
            p2 = players[1].pop(0)
            if (len(players[0]) < p1 or len(players[1]) < p2):
                if (p1 > p2):
                    players[0].append(p1)
                    players[0].append(p2)
                else:
                    players[1].append(p2)
                    players[1].append(p1)
            else:
                subgame = [deepcopy(players[0][:p1]), deepcopy(players[1][:p2])]
                winner, deck = recurscombat(subgame)
                if (winner == 1):
                    players[0].append(p1)
                    players[0].append(p2)
                else:
                    players[1].append(p2)
                    players[1].append(p1)

    if (len(players[0]) == 0):
        return 2, players[1]
    else:
        return 1, players[0]

winner, deck = recurscombat(deepcopy(players))
print("Part two: ", "Player ", winner, " wins!")
score = 0
for i, val in enumerate(reversed(deck)):
    score += (i + 1) * val
print("Score: ", score)
