from OOP.ClassesAndObjects.project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        if task_name in self.tasks:
            self.tasks[task_name].completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for every_task in self.tasks:
            if every_task.completed:
                self.tasks.remove(every_task)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for every_task in self.tasks:
            result += f"{Task.details(every_task)}\n"
        return result


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())


