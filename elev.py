class Elevator:
    def __init__(self, elev=5, floor=3):
        self.elev = elev
        self.floor = floor

    def up(self):
        if self.floor == self.elev:
            return "Лифт не может подняться выше"
        else:
            self.floor += 1
            return f"Лифт поднимается на {self.floor} этаж"

    def down(self):
        if self.floor == 1:
            return "Лифт не может опуститься ниже"
        else:
            self.floor -= 1
            return f"Лифт опускается на {self.floor} этаж"


fl = Elevator()
fl.down()
fl.down()
fl.down()