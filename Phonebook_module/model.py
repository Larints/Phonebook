import json

import text


class PhoneBook:

    def __init__(self, path: str = 'phones.json'):
        self.contact: dict = {}
        self.not_changed = {}
        self.path = path

    def get(self, index: int | None = None):
        if index:
            return self.contact.get(index)
        return self.contact

    def open_file(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                self.contact = json.load(file)
                self.not_changed = self.contact.copy()
            return True
        except:
            return False

    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.contact, file, ensure_ascii=False, indent=4)
            return True
        except:
            return False

    def search(self, word: str) -> dict[int:dict[str, str]]:
        result = {}
        for index, contact in self.contact.items():
            if word.lower() in ' '.join(contact.values()).lower():
                result[index] = contact
        return result

    def check_id(self):
        if self.contact:
            return max(list(map(int, self.contact))) + 1
        return 1

    def add_contact(self, new: dict[str, str]):
        contact = {self.check_id(): new}
        self.contact.update(contact)

    def search_id(self, word: str):  # Костыль номер два
        while True:
            id = input(text.index_change)
            if id in self.contact:
                return id
            else:
                print(text.not_id(id))
                continue

    def change_contact(self, id: str, contact: []) -> dict[int:dict[str, str]]:
        if id in self.contact:
            self.contact[id]['name'] = contact[0]
            self.contact[id]['phone'] = contact[1]
            self.contact[id]['comment'] = contact[2]
            return self.contact
        else:
            return text.not_id(id)

    def remove(self, index):
        name = self.contact.pop(str(index))
        return name.get('name')

    def check_on_exit(self):
        if self.contact == self.not_changed:
            return False
        return True
