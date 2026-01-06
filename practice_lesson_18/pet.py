class Pet:
    def __init__(self, name, pet_id, pet_type, owner):
        self.name = name
        self.pet_id = pet_id
        self.pet_type = pet_type
        self.owner = owner

    def make_sound(self):
        raise notImplementedError("Subclasses must implement this method")

    def get_info(self):
        return (
            f"Name: {self.name}, "
            f"ID: {self.pet_id}, "
            f"Type: {self.pet_type}, "
            f"Owner: {self.owner}"
        )


