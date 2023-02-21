class ExercisePlan:

    _counter = 0

    def __init__(self, trainer_id, equipment_id, duration):
        ExercisePlan._counter += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan._counter

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        hours = hours * 60
        return cls(trainer_id, equipment_id, hours)

    @staticmethod
    def get_next_id():
        return ExercisePlan._counter + 1

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
