from threading import Thread, Event
from time import sleep

from reader_writer import JSONReaderWriter, PickleReaderWriter


class Phonebook:

    def __init__(self, path_to_db="", format='json', auto_save_period=0):
        self.path_to_db = path_to_db
        self._format = format
        self.auto_save_period = auto_save_period

        self._contacts = {}
        self._is_changed = False
        self._run_checker = Event()
        self._reader_writer = self._get_reader_writer()

        self._run_checker.set()
        if auto_save_period:
            thread = Thread(target=self.auto_save)
            thread.start()

    @property
    def _max_id(self):
        return max(self._contacts.keys()) if self._contacts else 0

    def _mark_data_changed(self):
        self._is_changed = True

    def _mark_data_saved(self):
        self._is_changed = False

    def add_contact(self, contact):
        self._contacts[self._max_id+1] = contact.serialize()
        self._mark_data_changed()

    def remove_contact(self, id_):
        self._contacts.pop(id_)
        self._mark_data_changed()

    def find_contact(self):
        raise NotImplementedError('find_contact method is not implemented yet')

    def update_contact(self, id_, new_contact):
        self._contacts[id_] = new_contact.serialize()
        self._mark_data_changed()

    def save_contacts_to_file(self, path):
        self._reader_writer.write(self._contacts, path)

    def get_contacts(self):
        return self._contacts

    # Might be issue because of concurent reading/writing from/to file. Need separate reading data and starting autosave thread
    @classmethod
    def create_phone_book_from_file(cls, path_to_db, format, auto_save_period):
        phonebook = Phonebook(path_to_db, format, auto_save_period)
        phonebook._contacts = phonebook._reader_writer.read(path_to_db)
        #phonebook.path_to_db = path
        return phonebook

    def auto_save(self):
        while self._run_checker.is_set():
            if self._is_changed:
                self.save_contacts_to_file(self.path_to_db)
                self._mark_data_saved()
            sleep(self.auto_save_period)

    def close(self):
        self._run_checker.clear()

    def _get_reader_writer(self):
        if self._format == 'json':
            return JSONReaderWriter()
        elif self._format == 'pickle':
            return PickleReaderWriter()
        else:
            raise ValueError(f"'{format}' format is not supported")


if __name__ == '__main__':
    from contact import Contact
    contact1 = Contact('John')
    contact2 = Contact('Anna')
    phonebook = Phonebook(path_to_db='contacts.json', auto_save_period=3)
    phonebook.add_contact(contact1)
    sleep(5)
    phonebook.add_contact(contact2)
    sleep(5)
    print(phonebook.get_contacts())
    phonebook.close()
