import json


def export_json(storage_file: str, data: dict) -> None:
    with open(storage_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def import_json(storage_file: str) -> dict:
    with open(storage_file, 'r', encoding='utf-8') as json_file:
        json_data = json.loads(json_file.read())

        return json_data
