import json
from task import TaskManager
from ui import UIManager

with open("data.json", mode='r') as json_file:
    data = json.load(json_file)

task_manager = TaskManager()
for task_data in data:
    task_manager.add_task(task_data)

ui = UIManager(task_manager)

# ファイルの書き込み
with open("data.json", mode='w',encoding="utf-8") as json_file:
    updated_data=[]
    for task in task_manager.tasks:
        if not task.deleted:
            updated_data.append({
            "title": task.title,
            "content":task.content
        })
    json.dump(updated_data,json_file,indent=4,ensure_ascii=False)