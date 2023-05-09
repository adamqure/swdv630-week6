class Employee:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

class LineWorker(Employee):
    def __init__(self, name):
        super().__init__(name, "LineWorker")

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, "Manager")


class EmployeeFactory(object):
    @classmethod
    def create(self, name: str, position: str) -> Employee:
        match position:
            case "Manager":
                return Manager(name)
            case "LineWorker":
                return LineWorker(name)

def main():
    manager = EmployeeFactory.create("Test Manager", "Manager")
    lineWorker = EmployeeFactory.create("Test Line Worker", "LineWorker")

    assert(isinstance(manager, Manager))
    assert(isinstance(lineWorker, LineWorker))

    print("Employee factory works!")

main()