# A simple class to represent a learner

class Learner:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")


first_learner = Learner("Niharika", [78, 84, 91])
first_learner.show_details()
