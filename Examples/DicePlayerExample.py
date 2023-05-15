import DiceGameExample
from .DiceEngine import NumericDieTemplate

class Player:
    def __init__(self):
        self.pool = list()

    def playRound(self, diceCount, dieFaces):
        dieTemplate = NumericDieTemplate(6)

        self.pool = dieTemplate.rollPool(diceCount)

        faceValues = DiceGameExample.countFaces(self.pool, dieFaces)

        faceIndex = 1

        score = 0

        for set in faceValues:
            setScore = DiceGameExample.scoreSet(faceIndex, set)
            score += setScore
            faceIndex += 1
        
        return score    