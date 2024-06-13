import json
from threading import Thread, Event
from time import sleep


class Phonebook:

    PATH_TO_DB = "phonebook.json"

    def __init__(self, auto_save_period=0):
        self._contacts = {}
        self.auto_save_period = auto_save_period
        self._run_checker = Event()
        self._run_checker.set()
        if auto_save_period:
            thread = Thread(target=self.auto_save)
            thread.start()

    @property
    def max_id(self):
        return max(self._contacts.keys()) if self._contacts else 0

    def add_contact(self, contact):
        self._contacts[self.max_id+1] = contact.serialize()

    def remove_contact(self, id_):
        self._contacts.pop(id_)

    def find_contact(self):
        raise NotImplementedError('find_contact method is not implemented yet')

    def update_contact(self, id_, new_contact):
        self._contacts[id_] = new_contact.serialize()

    def save_contacts_to_file(self, path):
        with open(path, 'w') as file:
            json.dump(self._contacts, file)

    def get_contacts(self):
        return self._contacts

    @classmethod
    def create_phone_book_from_file(cls, path):
        phonebook = Phonebook()
        with open(path, 'r') as file:
            phonebook._contacts = json.load(file)

    @classmethod
    def change_db_path(cls, db_path):
        Phonebook.PATH_TO_DB = db_path

    def auto_save(self):
        print(self._run_checker)
        while self._run_checker.is_set():
            # TODO: save only if self._contacts was changed
            self.save_contacts_to_file(Phonebook.PATH_TO_DB)
            sleep(self.auto_save_period)

    def close(self):
        self._run_checker.clear()


if __name__ == '__main__':
    from contact import Contact
    contact1 = Contact('John')
    contact2 = Contact('Anna')
    phonebook = Phonebook(auto_save_period=3)
    phonebook.add_contact(contact1)
    sleep(5)
    phonebook.add_contact(contact2)
    sleep(15)
    print(phonebook.get_contacts())
    phonebook.close()
