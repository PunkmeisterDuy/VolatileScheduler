import random

class Task:
    def __init__(self, name = "", importance = -1):
        self.name = name
        self.importance = importance

class Schedule:
    def __init__(self):
        self.tasks=[]
    
    def add_task(self, Task):
        self.tasks.append(Task)

    def ask_task(self):
        ask = True
        while(ask):
            taskName = input("Enter name of task (blank to exit): ")
            if (taskName == ""):
                ask = False
            else:
                importance = int(input("Enter importance (1-10): "))
                self.add_task(Task(taskName, importance))
    
    def volatile_randomizer(self):
        volatileSchedule = Schedule()
        for i in range(len(self.tasks)):
            volatileSchedule.tasks.append(self.tasks[i])
        for i in range(len(volatileSchedule.tasks)):
            volatileSchedule.tasks[i].importance = volatileSchedule.tasks[i].importance + (random.randint(0,100) * .01)
        return volatileSchedule

#FIX THE ""
