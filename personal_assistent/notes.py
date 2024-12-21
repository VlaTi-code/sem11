import csv
import json


from datetime import datetime
from utils import export_json, import_json


# class Note(object):
#     def __init__(self, note_id, title, content, timestamp) -> None:
#         self.id = note_id
#         self.title = title
#         self.content = content
#         self.timestamp = timestamp


class NoteStorage(object):
    def __init__(self) -> None:
        self.storage_file = "storage/tasks.json"
        self.id_template = 'note_'

        self.cur_notes_cnt = len(import_json(self.storage_file))

    def add_note(self, title: str, content: str, timestamp: datetime.date):
        current_tasks = import_json(self.storage_file)

        current_tasks[self.id_template + str(self.cur_notes_cnt + 1)] = {
            # 'object': Note(...),
            'title': title,
            'content': content,
            'timestamp': timestamp
        }
        self.cur_notes_cnt += 1

        print(f"Заметка успешно создана с id {self.id_template + str(self.cur_notes_cnt)}")

        export_json(self.storage_file, current_tasks)

    def get_all_notes(self):
        current_notes = import_json(self.storage_file)

        for n_id in current_notes:
            note_data = current_notes[n_id]

            title = note_data.get('title')
            content = note_data.get('content')
            timestamp = note_data.get('timestamp')

            print(f"****** Заметка {n_id} ******")
            print(f"\tНазвание: {title}")
            print(f"\tСодержимое: {content}")
            print(f"\tДата написания: {timestamp}")
            print("\n")

    def get_note_info(self, note_id):
        current_notes = import_json(self.storage_file)

        if note_id not in current_notes:
            print("Такой заметки нет.")
            return
        else:
            note_data = current_notes[note_id]

            title = note_data.get('title')
            content = note_data.get('content')
            timestamp = note_data.get('timestamp')

            print(f"****** Заметка {note_id} ******")
            print(f"\tНазвание: {title}")
            print(f"\tСодержимое: {content}")
            print(f"\tДата написания: {timestamp}")
            print("\n")

    def edit_note(self):
        pass

    def delete_note(self, note_id):
        current_notes = import_json(self.storage_file)

        if note_id not in current_notes:
            print("Такой задачи нет.")
            return
        else:
            del current_notes[note_id]

    def import_notes_from_csv(self) -> None:
        pass

    def export_notes_to_csv(self) -> None:
        pass
