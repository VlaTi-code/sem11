import csv
import json


from datetime import datetime
from utils import export_json, import_json


def contact_search(value, data):
    for key, item in data.items():
        if value in item:
            return key

# class Contact(object):
#     def __init__(self, contact_id, name, phone, email):
#         self.id = contact_id
#         self.name = name
#         self.phone = phone
#         self.email = email


class ContactStorage(object):
    def __init__(self):
        self.storage_file = "storage/contacts.json"
        self.id_template = 'contact_'

        self.cur_contacts_cnt = len(import_json(self.storage_file))

    def add_contact(self, name, phone, email):
        current_contacts = import_json(self.storage_file)

        current_contacts[self.id_template + str(self.cur_contacts_cnt + 1)] = {
            'name': name,
            'phone': phone,
            'email': email,
        }
        self.cur_contacts_cnt += 1

        print(f"Контакт успешно создан с id {self.id_template + str(self.cur_contacts_cnt)}")

        export_json(self.storage_file, current_contacts)

    def get_contact(self, value):
        current_contacts = import_json(self.storage_file)

        contact_id = contact_search(value, current_contacts)

        if not contact_id:
            print("такого контакта нет")

            return

        contact_data = current_contacts[contact_id]

        name = contact_data.get('title')
        phone = contact_data.get('content')
        email = contact_data.get('timestamp')

        print(f"****** Контакт {contact_id} ******")
        print(f"\tИмя: {name}")
        print(f"\tНомер телефона: {phone}")
        print(f"\tЭл. почта: {email}")
        print("\n")

    def edit_contact(self):
        pass

    def delete_contact(self, contact_id):
        current_contacts = import_json(self.storage_file)

        if contact_id not in current_contacts:
            print("такого контакта нет")

            return

        del current_contacts[contact_id]

        export_json(self.storage_file, current_contacts)

    def import_contacts_from_csv(self) -> None:
        pass

    def export_contacts_to_csv(self) -> None:
        pass
