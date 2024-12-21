import csv
import json


from datetime import datetime

from tornado.process import task_id

from utils import export_json, import_json


# class Task(object):
#     def __init__(
#             self,
#             task_id: str,
#             title: str,
#             description: str,
#             done: bool,
#             priority: int,
#             due_date: str,
#     ):
#         self.id = task_id
#         self.title = title
#         self.description = description
#         self.done = done
#         self.priority = priority
#         self.due_date = due_date


class TaskStorage(object):
    def __init__(self) -> None:
        self.storage_file = "storage/tasks.json"
        self.id_template = 'task_'

        self.cur_tasks_cnt = len(import_json(self.storage_file))

    def add_task(self, title, description, done, priority, due_date):
        current_tasks = import_json(self.storage_file)

        current_tasks[self.id_template + str(self.cur_tasks_cnt + 1)] = {
            # 'object': Task(
            #     self.id_template + str(self.cur_tasks_cnt + 1),
            #     title,
            #     description,
            #     done,
            #     priority, due_date
            # ),
            'title': title,
            'description': description,
            'done': done,
            'priority': priority,
            'due_date': due_date
        }
        self.cur_tasks_cnt += 1

        print(f"Задача успешно создана с id {self.id_template + str(self.cur_tasks_cnt)}")

        export_json(self.storage_file, current_tasks)

    def get_all_tasks(self):
        current_tasks = import_json(self.storage_file)

        for t_id in current_tasks:
            task_data = current_tasks[t_id]

            title = task_data.get('title')
            description = task_data.get('description')
            done = task_data.get('done')
            priority = task_data.get('priority')
            due_date = task_data.get('due_date')

            print(f"****** Задача {t_id} ******")
            print(f"\tНазвание: {title}")
            print(f"\tОписание: {description}")
            print(f"\tВыполнена: {"Да" if done else "Нет"}")
            print(f"\tПриоритет: {priority}")
            print(f"\tДедлайн: {due_date}")
            print("\n")

    def mark_task_done(self, task_id):
        current_tasks = import_json(self.storage_file)

        if task_id not in current_tasks:
            print("Такой задачи нет.")
            return
        else:
            current_tasks[task_id]['done'] = True

        export_json(self.storage_file, current_tasks)

    def edit_task(self):
        pass

    def delete_task(self, task_id):
        current_tasks = import_json(self.storage_file)

        if task_id not in current_tasks:
            print("Такой задачи нет.")
            return
        else:
            del current_tasks[task_id]

        export_json(self.storage_file, current_tasks)

    def import_task_from_csv(self, task_id):
        pass

    def export_task_to_csv(self, task_id):
        pass
