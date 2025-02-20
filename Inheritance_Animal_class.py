# Here we are using the Inheritance route 1 in which we do not create new properties and use all the properties of the superClass or we can say parent class.
class Animal:
    def __init__(self,region, animal_type, color,lethal):
        self.region = region
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal

    def animal_bio(self):
        print(f"animal passport")
        print(f"found in : {self.region}")
        print(f"species: {self.animal_type}")
        print(f"color:{self.color}")
        print(f"dangerous: {self.lethal}")

class Clinic(Animal): #Inherited class or child class of the superclass animal
    def animal_info(self):
        print(f"this is a {self.animal_type} from the {self.region}")

    def search(self,animals):
        region= input("enter a region: ").lower()
        for animal in animals:
            if animal.region == region:
                print(f"species: {animal.animal_type}")

animals = []
amt_animals = int(input("enter the numbeer of animals: "))
for i in range(amt_animals):
    region = input("enter a region: ").lower()
    species = input("enter a species: ").lower()
    color = input("enter a color: ").lower()
    lethal = input("It is dangerous ").lower()
    lethal = lethal == 'yes'

animal = Animal(region,species,color,lethal) #object of the Animal class

animals.append(animal)

clinic = Clinic("asia","tiger","orange",True) #object of Clinic class
clinic.animal_info()
clinic.search(animals)








