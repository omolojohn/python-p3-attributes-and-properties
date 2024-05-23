import sys

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.", file=sys.stderr)
        if breed not in ["Beagle", "Pug"]:
            print("Breed must be in list of approved breeds.", file=sys.stderr)

if __name__ == "__main__":
    fido = Dog(name="Fido", breed="Pug")
    print(fido.name)
    print(fido.breed)
