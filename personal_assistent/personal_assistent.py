import csv

from notes import NoteStorage
from tasks import TaskStorage
from contacts import ContactStorage
from finance_record import FinanceRecordStorage
from calculator import Calculator
from datetime import datetime

notes = NoteStorage()
tasks = TaskStorage()
contacts = ContactStorage()
finance_recorder = FinanceRecordStorage()
calculator = Calculator()


def notes_polling():
    while True:
        motion = input(
            '''Управление задачами:\n'''
            '''1. Добавить новую заметку\n'''
            '''2. Просмотреть заметки\n'''
            '''3. Просмотреть подробности заметки'''
            '''4. Редактировать заметку\n'''
            '''5. Удалить заметку\n'''
            '''6. Экспорт задач в CSV\n'''
            '''7. Импорт задач из CSV\n'''
            '''8. Назад\n'''
        )

        if motion == '1':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")

            day = input("Введите день написания заметки: ")
            month = input("Введите месяц написания заметки: ")
            year = input("введите год написания заметки: ")

            try:
                date_object = datetime(int(year), int(month), int(day))
                timestamp = date_object.strftime("%d-%m-%Y")

                notes.add_note(title, content, timestamp)
            except Exception as error:
                print(str(error))

                break
        elif motion == '2':
            notes.get_all_notes()
        elif motion == '3':
            note_id = input("Введите id заметки: ")

            notes.get_note_info(note_id)
        elif motion == '4':
            pass
        elif motion == '5':
            note_id = input("Введите id заметки: ")

            notes.delete_note(note_id)
        elif motion == '6':
            pass
        elif motion == '7':
            pass
        elif motion == '8':
            break
        else:
            print("Дебил бл")


def tasks_polling():
    while True:
        motion = input(
            '''Управление задачами:\n'''
            '''1. Добавить новую задачу\n'''
            '''2. Просмотреть задачи\n'''
            '''3. Отметить задачу как выполненную\n'''
            '''4. Редактировать задачу\n'''
            '''5. Удалить задачу\n'''
            '''6. Экспорт задач в CSV\n'''
            '''7. Импорт задач из CSV\n'''
            '''8. Назад\n'''
        )

        if motion == '1':
            title = input("Введите название задачи: ")
            content = input("Введите описание задачи: ")
            done = True if input(
                '''1. Задача уже выполнена\n'''
                '''2. Задача ещё не выполнена\n'''
            ) == 1 else False
            priority = 1 if input(
                '''1. Задача важная\n'''
                '''2. Задача не такая и важная\n'''
            ) == 1 else 2

            day = input("Введите день дедлайна задачи: ")
            month = input("Введите месяц дедлайна задачи: ")
            year = input("введите год дедлайна задачи: ")

            try:
                date_object = datetime(int(year), int(month), int(day))
                timestamp = date_object.strftime("%d-%m-%Y")

                tasks.add_task(title, content, timestamp)
            except Exception as error:
                print(str(error))

                break
        elif motion == '2':
            tasks.get_all_tasks()
        elif motion == '3':
            task_id = input("Введите id задачи: ")

            tasks.mark_task_done(task_id)
        elif motion == '4':
            pass
        elif motion == '5':
            task_id = input("Введите id задачи: ")

            notes.delete_note(task_id)
        elif motion == '6':
            pass
        elif motion == '7':
            pass
        elif motion == '8':
            break
        else:
            print("Дебил бл")


def contacts_polling():
    while True:
        motion = input(
            '''Управление задачами:\n'''
            '''1. Добавить новый контакт\n'''
            '''2. Поиск контакта по имени или номеру телефона\n'''
            '''3. Редактировать контакт\n'''
            '''4. Удалить контакт\n'''
            '''5. Экспорт контактов в CSV\n'''
            '''6. Импорт контактов из CSV\n'''
            '''7. Назад\n'''
        )

        if motion == '1':
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите эл. почту контакта: ")

            contacts.add_contact(name, phone, email)
        elif motion == '2':
            value = input("Введите имя или номер телефона контакта: ")

            contacts.get_contact(value)
        elif motion == '3':
            pass
        elif motion == '4':
            contact_id = input("Введите id контакта: ")

            contacts.delete_contact(contact_id)
        elif motion == '5':
            pass
        elif motion == '6':
            pass
        elif motion == '7':
            break
        else:
            print("Дебил бл")

def finance_recorder_polling():
    while True:
        motion = input(
            '''Управление задачами:\n'''
            '''1. Добавить новую запись\n'''
            '''2. Просмотреть записи\n'''
            '''3. Генерировать отчет за период\n'''
            '''4. Экспорт задач в CSV\n'''
            '''5. Импорт задач из CSV\n'''
            '''6. Назад\n'''
        )

        if motion == '1':
            amount = input("Введите сумму: ")
            category = input("Введите категорию: ")
            description = input("Введите описание: ")

            day = input("Введите день покупки: ")
            month = input("Введите месяц покупки: ")
            year = input("введите год покупки: ")

            try:
                date_object = datetime(int(year), int(month), int(day))
                timestamp = date_object.strftime("%d-%m-%Y")

                finance_recorder.add_record(amount, category, timestamp, description)
            except Exception as error:
                print(str(error))
        elif motion == '2':
            finance_recorder.get_all_records()
        elif motion == '3':
            pass
        elif motion == '4':
            pass
        elif motion == '5':
            pass
        elif motion == '6':
            break
        else:
            print("Дебил бл")


def calculator_polling():
    while True:
        motion = input(
            '''Управление задачами:\n'''
            '''1. Сложение\n'''
            '''2. Вычитание\n'''
            '''3. Произведение\n'''
            '''4. Частное\n'''
        )

        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        if motion == '1':
            calculator.add(a, b)
        elif motion == '2':
            calculator.subtract(a, b)
        elif motion == '3':
            calculator.multiply(a, b)
        elif motion == '4':
            calculator.divide(a, b)


def main_polling():
    while True:
        motion = input(
            '''Добро пожаловать в Персональный помощник!\n'''
            '''Выберите действие:\n'''
            '''1. Управление заметками\n'''
            '''2. Управление задачами\n'''
            '''3. Управление контактами\n'''
            '''4. Управление финансовыми записями\n'''
            '''5. Калькулятор\n'''
            '''6. Выход'''
        )

        if motion == '1':
            pass
        elif motion == '2':
            pass
        elif motion == '3':
            pass
        elif motion == '4':
            pass
        elif motion == '5':
            pass
        elif motion == '6':
            break


if __name__ == '__main__':
    main_polling()
