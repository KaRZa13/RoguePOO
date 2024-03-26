from random import randint


class Dice:
    def __init__(self, nb_faces) -> None:
        self.nb_faces = nb_faces
        

    def __str__(self) -> str:
        return f"Dice {self.nb_faces}"
    
    def roll(self) -> int:
        return randint(1, self.nb_faces)
    