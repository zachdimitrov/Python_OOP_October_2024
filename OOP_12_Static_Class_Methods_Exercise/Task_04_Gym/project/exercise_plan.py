class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.duration = duration
        self.equipment_id = equipment_id
        self.trainer_id = trainer_id
        self.id = self.get_next_id()
        ExercisePlan.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
