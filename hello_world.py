from dataclasses import dataclass


@dataclass
class person:
    name: str
    age: int
    company: str
    nationality: str


if __name__ == "__main__":
    print("Hello World!")

    first_person = person(name="Amizzuddin", age=35, company="Conti", nationality="malaysian")
    print(first_person)
