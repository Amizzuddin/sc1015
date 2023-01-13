from dataclasses import dataclass

@dataclass 
class person:
    name: str
    age: int

if __name__ == "__main__":
    print("Hello World!")

    first_person = person(name="Amizzuddin", age=35)
    print(first_person)
