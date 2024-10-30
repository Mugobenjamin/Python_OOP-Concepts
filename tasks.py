class Task:
    def __init__(self, title, description, cost):
        self.title = title
        self.description = description
        self.cost = cost

    def print_task(self):
        print(f"Task title: {self.title} : {self.description} : {self.cost} ")

task1 = Task("Buy Groceries", "Apples, Kales and Bananas", '100, 50, 90')
task1.print_task()