class Employee: 
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def serialize(self):
        return {
            "name": self.name,
            "age": self.age }
