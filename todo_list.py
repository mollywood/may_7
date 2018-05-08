#You are responsible for creating a TODO list app. Here are the requested features for the TODO list app:

#- User should be able to add task by adding the title of the task

#- User should be able to view all the tasks

#- User should be able to remove the tasks

#- User should be able to quit the app when "q" is pressed



#HARD MODE:

#- User should be able to enter priority of the task

#- User should be able to sort the tasks based on priority


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
