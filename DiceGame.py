import random
import math

def rollDie(faces):
    roll = random.randint(1, faces)
    return roll

def rollPool(count, faces):

    pool = list()

    for i in range(count):
        pool.append(rollDie(faces))

    return pool

def countFaces(pool, faces):
    counts = list()

    for face in range(faces):
        counts.append(0)

    for die in pool:
        counts[die-1] += 1

    return counts

def scoreSet(face, count):
    score = 0
    value = 0

    if face == 1:
        value = 100
    else:
        value = face * 10

    score += math.floor(count / 3) * 10 * value

    if face == 1 or face == 5:
        score += (count % 3) * value

    return score


def scorePool(pool, faces):
    score = 0

    counts = countFaces(pool, faces)
    
    index = 1

    for count in counts:

        score += scoreSet(index, count)
        
        index += 1
    
    return score
