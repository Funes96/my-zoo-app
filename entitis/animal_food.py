# from entitis.animal import animal

class animal_food:
    vegi: bool
    dry: bool = False
    kind: int

    def __init__(self, vegi: bool, dry: bool, kind: int):
        self.vegi = vegi
        self.dry = dry
        self.kind = kind

     # def food_kind(self, kind: animal)
     #   print()
