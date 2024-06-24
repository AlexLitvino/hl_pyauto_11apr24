from time import sleep

from contact import Contact
from phonebook import Phonebook

phonebook = Phonebook()
print(phonebook.get_contacts())

contact1 = Contact('John')
contact2 = Contact('Anna')

phonebook = Phonebook(path_to_db='contacts.json', auto_save_period=3)
phonebook.add_contact(contact1)
sleep(5)
phonebook.add_contact(contact2)
sleep(5)
print(phonebook.get_contacts())
phonebook.close()


