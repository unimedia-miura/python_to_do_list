class Task:
    def __init__(self, task_data):
        self.deleted = False
        self.title = task_data['title']
        self.content = task_data['content']

    def change_to_deleted(self):
        self.deleted = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_data):
        new_task = Task(task_data)
        self.tasks.append(new_task)

    def delete_task(self, task):
        task.change_to_deleted()
        self.tasks = [task for task in self.tasks if not task.deleted]