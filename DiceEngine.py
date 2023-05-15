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

    def roll(self):
        """Roll a single die of the template type
        
        Return: a string representing the rolled face
        """
        
        index = random.randint(0, self.faceCount)
        return self.faces[index]
    
    def rollPool(self, diceCount):
        """Roll a pool of the die template
        
        Keyword arguments:
        diceCount -- integer representing the number of dice to be rolled in the pool
        Return: A list of strings representing the faces randomly rolled from the pool
        """
        
        pool = list()

        for die in range(diceCount):            
            pool.append(self.roll())

        return pool
        
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
        
        super().__init__(range(faceCount))

class DiceHelper:
    def roll(pool):
        result = list()

        for die in pool:
            result.append(die.roll)
