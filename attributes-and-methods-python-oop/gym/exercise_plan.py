class ExercisePlan:
    excerciseplan_id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        duration = hours * 60
        return cls(trainer_id, equipment_id, duration)

    @staticmethod
    def get_next_id():
        ExercisePlan.excerciseplan_id += 1
        return ExercisePlan.excerciseplan_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
