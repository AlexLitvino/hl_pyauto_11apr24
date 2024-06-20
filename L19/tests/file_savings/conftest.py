from L19.phonebook.phonebook import Phonebook


import pytest


@pytest.fixture(params=['json', 'pickle'])
def format(request):
    return request.param

@pytest.fixture()
def phonebook(tmp_path, format):
    contacts_file = tmp_path / "contacts.json"
    print(f"DB: {contacts_file}")
    phonebook = Phonebook(path_to_db=contacts_file, format=format, auto_save_period=3)
    yield phonebook
    phonebook.close()


@pytest.fixture()
def phonebook_with_autosave(request):

    def configure_phonebook(autosave):

        phonebook = Phonebook(path_to_db="contacts.json", auto_save_period=autosave)

        def closing_phonebook():
            phonebook.close()
        request.addfinalizer(closing_phonebook)

        return phonebook

    return configure_phonebook

