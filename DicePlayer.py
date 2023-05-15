import DiceGame

class Player:
    def __init__(self):
        self.pool = list()

    def playRound(self, diceCount, dieFaces):
        self.pool = DiceGame.rollPool(diceCount,dieFaces)

        faceValues = DiceGame.countFaces(self.pool, dieFaces)

        faceIndex = 1

        score = 0

        for set in faceValues:
            setScore = DiceGame.scoreSet(faceIndex, set)
            score += setScore
            faceIndex += 1
        
        return score    