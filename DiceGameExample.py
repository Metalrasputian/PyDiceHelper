import math
from DiceEngine import DiceHelper, DieTemplate, NumericDieTemplate

def countFaces(pool, faces):
    counts = list()

    for face in range(faces):
        counts.append(0)

    for die in pool:
        counts[int(die)-1] += 1

    return counts

def scoreSet(face, count):
    score = 0
    value = 0

    face_int = int(face)

    if face_int == 1:
        value = 100
    else:
        value = face_int * 10

    score += math.floor(count / 3) * 10 * value

    if face_int == 1 or face_int == 5:
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

def play_five_dice():
    diceCount = 5
    dieFaces = 6

    dieTemplate = NumericDieTemplate(dieFaces)

    pool = dieTemplate.rollPool(diceCount)

    faceValues = countFaces(pool, dieFaces)

    faceIndex = 1

    score = 0

    for set in faceValues:
        setScore = scoreSet(faceIndex, set)
        score += setScore
        faceIndex += 1

    print("Five Dice Score")
    print("===============")
    print(pool)
    print(score)
    print("===============")

def determine_hits(pool):

    hits = 0
    misses = 0
    crits = 0

    for die in pool:
        if die == "*":
            hits +=1
        elif die == "**":
            hits += 2
        elif die == "$":
            crits += 1
        else:
            misses += 1

    return (hits, misses, crits)

def roll_symbol_dice():
    faces = [("*", 2), ("$", 3), (" ", 2), ("**", 1)]
    dieTemplate = DieTemplate(faces)

    pool = dieTemplate.rollPool(5)

    result = determine_hits(pool)

    print("Symbol Die Pool")
    print("===============")
    print(pool)
    print("Hits: {}, misses: {}, crits: {}".format(result[0], result[1], result[2]))
    print("===============")

def roll_explode_dice():
    faces = [("*", 2), ("$", 3), (" ", 2), ("**", 1)]
    dieTemplate = DieTemplate(faces)

    explodes_on = ["$", "**"]

    

    
if __name__ == "__main__":
    play_five_dice()
    print()
    roll_symbol_dice()
