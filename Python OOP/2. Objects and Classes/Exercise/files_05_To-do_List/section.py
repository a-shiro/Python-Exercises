class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name):
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        removed = 0

        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                removed += 1

        return f'Cleared {removed} tasks.'

    def view_section(self):
        result = f'Section {self.name}:\n'
        for t in self.tasks:
            result += f'{t.details()}\n'
        return result