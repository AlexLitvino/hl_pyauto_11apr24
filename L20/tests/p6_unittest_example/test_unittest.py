import os
import time
from unittest import TestCase, main
import sys
sys.path.append('../..')
sys.path.append('../phonebook')

from L20.phonebook.contact import Contact
from L20.phonebook.phonebook import Phonebook


class TestPhonebook(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("In setUpClass")
        cls.nominal_contact = Contact('John')

    def setUp(self) -> None:
        print("In setUp method")
        self.path_to_db = 'contacts.json'
        self.auto_save_period = 3
        self.phonebook = Phonebook(self.path_to_db, auto_save_period=self.auto_save_period)

    def test_adding_contact(self):
        self.phonebook.add_contact(self.nominal_contact)
        self.assertEqual(len(self.phonebook.get_contacts()), 1, 'Number of contacts not equal to 1')

    def test_saving_to_file(self):
        self.phonebook.add_contact(self.nominal_contact)
        time.sleep(self.auto_save_period + 1)
        self.assertTrue(os.path.exists(self.path_to_db), "DB wasn't created")

    def tearDown(self) -> None:
        print("In teardown method")
        self.phonebook.close()
        if os.path.exists(self.path_to_db):
            os.remove(self.path_to_db)

    @classmethod
    def tearDownClass(cls) -> None:
        print("In tear down class")


if __name__ == '__main__':
    main()
