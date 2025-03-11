class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅ Виконано" if self.completed else "❌ Не виконано"
        return f"{self.title} ({self.deadline}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def show_tasks(self):
        for task in self.tasks:
            print(task)


# Приклад використання
manager = TaskManager()
task1 = Task("Купити молоко", "Не забути про знижку", "12.03.2025")
manager.add_task(task1)
manager.show_tasks()