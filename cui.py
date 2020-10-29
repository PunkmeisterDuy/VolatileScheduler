# Import the lib
import py_cui
import scheduler

schedule = scheduler.Schedule()


schedule.ask_task()
dailySchedule = schedule.volatile_randomizer()

# create the CUI object. Will have a 3 by 3 grid with indexes from 0,0 to 2,2

root = py_cui.PyCUI(len(dailySchedule.tasks)+1,3)

# Add a label to the center of the CUI in the 1,1 grid position
#root.add_label('Hello py_cui!!!', 1, 1)
root.add_label("Schedule: ", 0, 0)

for i in range(len(dailySchedule.tasks)):
    root.add_label(dailySchedule.tasks[i].name, i+1, 0)
    root.add_label(str(dailySchedule.tasks[i].importance), i+1, 1)
    root.add_label(str(i),i+1,2)

# Start/Render the CUI
root.start()