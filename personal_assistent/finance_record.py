import csv
import json


from datetime import datetime

from tornado.util import import_object

from utils import export_json, import_json


# class FinanceRecord(object):
#     def __init__(self, fr_id, amount, category, date, description):
#         self.fr_id = fr_id
#         self.amount = amount
#         self.category = category
#         self.date = date
#         self.description = description


class FinanceRecordStorage(object):
    def __init__(self):
        self.storage_file = "storage/finance_records.json"
        self.id_template = 'finance_record_'

        self.cur_records_cnt = len(import_json(self.storage_file))

    def add_record(self, amount, category, date, description):
        current_records = import_json(self.storage_file)

        current_records[self.id_template + str(self.cur_records_cnt + 1)] = {
            'amount': amount,
            'category': category,
            'date': date,
            'description': description,
        }
        self.cur_records_cnt += 1

        print(f"Запись успешно создана с id {self.id_template + str(self.cur_tasks_cnt)}")

        export_json(self.storage_file, current_records)

    def get_all_records(self):
        current_records = import_json(self.storage_file)

        for fr_id in current_records:
            record_data = current_records[fr_id]

            amount = record_data['amount']
            category = record_data['category']
            date = record_data['date']
            description = record_data['description']

            print(f"****** Запись о финансах {fr_id} ******")
            print(f"\tСумма: {amount}")
            print(f"\tКатегория: {category}")
            print(f"\tДата записи: {date}")
            print(f"\tОписание: {description}")
            print("\n")

    def period_report(self):
        pass

    def import_records_from_csv(self) -> None:
        pass

    def export_records_to_csv(self) -> None:
        pass
