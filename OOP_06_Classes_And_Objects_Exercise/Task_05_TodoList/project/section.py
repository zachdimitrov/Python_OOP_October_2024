from project.task import Task


class Section:
    def __init__(self, name: str):
        self.tasks = []
        self.name = name

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for task in self.tasks:
            if task.completed:
                count += 1
                self.tasks.remove(task)
        return f"Cleared {count} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result = result + task.details() + "\n"
        return result
