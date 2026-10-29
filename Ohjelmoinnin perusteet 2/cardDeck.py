cardDeck = []
for color in ("Red", "Black"):
    if color == "Red":      
        for land in ("heart", "diamond"):
            for rank in range(1,14):
                card = (color, land, rank)
                cardDeck.append(card)
    else:
        for land in ("spade", "club"):
            for rank in range(1,14):
                card = (color, land, rank)
                cardDeck.append(card)
print(cardDeck)