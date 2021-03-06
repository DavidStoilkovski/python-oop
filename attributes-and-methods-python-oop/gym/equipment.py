class Equipment:
    equipment_id = 0

    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment.equipment_id += 1
        return Equipment.equipment_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"