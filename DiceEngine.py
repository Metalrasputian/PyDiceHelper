import random

class DieTemplate:
    """A data object to represent a die with its faces and the ability to roll it

    Attributes
    ----------
    faces : list()
        A list of faces on the die, represented by a string
    
    faceCount : int
        A int representing the number of faces on the die

    Methods
    -------
    roll()
        returns a random face of a single die roll
    
    rollPool(diceCount)
        returns a list of random faces from the number of dice provided
    """
    

    def __init__(self, faces):
        """Creates a Die Template using the provided list of Touples in faces
        
        Keyword arguments:
        faces -- A list of Touples with a string representing a 'face' and an int representing the number of those faces on the die
        Return: returns a DieTemplate object
        """
        
        self.faces = list()

        for face in faces:
            for count in range(face[1]):
                self.faces.append(str(face[0]))
        
        self.faceCount = len(self.faces)

    def roll(self, count=1):
        """Roll a single die of the template type
        
        Return: a string representing the rolled face
        """
        
        pool = list()

        for die in range(count):            
            pool.append(index = random.randint(0, self.faceCount - 1))

        return pool
    
    def explode(self, pool, targets, recursive=False, recursion_depth=1):

        result = list()

        for die in pool:
            result.append(self.roll())
        
        if recursive and (recursion_depth > 0 or recursion_depth == -1):
            result.append(self.explode(result, targets, recursive, recursion_depth - 1))
        
        return result

        
class NumericDieTemplate(DieTemplate):
    """A simplified version of DieTemplate used for purely numeric dice (no special faces)
    See DieTemplate for methods and attributes
    """
    
    def __init__(self, faceCount):
        """Initializes a sequential, numerical die
        
        Keyword arguments:
        faceCount -- the number of faces on the die
        Return: a DieTemplate with iterated numeric faces
        """
        faces = list()

        for face in range(1, faceCount + 1):
            faces.append((str(face), 1))

        super().__init__(faces)

class DiePool:
    def __init__(self, template, count, explodes=False, targets=[], recursive=False):
        self.template = template
        self.count = count
        self.explodes = explodes
        self.targets = targets
        self.recursive = recursive
    
    def roll(self):
        result = list()

        result.append(self.template.roll(self.count))

        if self.explodes:
            result.append(self.explode(result, self.recursive))


class DiceHelper:
    def rollMixedPool(mixed_pool):
        result = list()

        for pool in mixed_pool:
            result.append(pool.roll())

        