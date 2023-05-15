import math

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
