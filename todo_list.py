class Todo:
    def __init__(self, user):
        self.user = user
        self.tasks = {}

    def add_task(self, task, priority):
        self.tasks.setdefault(priority, []).append(task)
        print(self.tasks)

    #def rm_task(self, task):



molly = Todo("Molly")
molly.add_task("go to the bank", "high")
molly.add_task("buy frozen lunches at Walmart", "high")
molly.add_task("nail salon", "low")
