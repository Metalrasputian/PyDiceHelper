import DiceGame
from DicePlayer import Player 

average = 0

poolCount = 5

faces = 6

player = Player()

score = player.playRound(poolCount,faces)

print(player.pool)
print("Score: " + str(score))