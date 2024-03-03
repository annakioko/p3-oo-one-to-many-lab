class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    def get_type(self):
        return self._pet_type
    
    def set_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception
        
    pet_type = property(get_type, set_type)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception 
           
    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)