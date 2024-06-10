from collections import Counter


def count_words_and_save_to_file(sentence, file_name):
    """Calculates how many times each word appears in sentence and output to file"""
    words = [word.lower() for word in sentence.split()]
    counter = Counter(words)
    with open(file_name, 'w') as f:
        for key in counter:
            f.write(f"{key}\t{counter[key]}\n")


sentence = "Red fox jump over lazy lazy dog"
count_words_and_save_to_file(sentence, 'srp_output.txt')


def count_words(sentence):
    """Calculates how many times each word appears in sentence"""
    words = [word.lower() for word in sentence.split()]
    counter = Counter(words)
    return counter


def save_dict_to_file(dict, file_name):
    """Prints dict to file"""
    with open(file_name, 'w') as f:
        for key in dict:
            f.write(f"{key}\t{dict[key]}\n")


sentence = "Red fox jump over lazy lazy dog"
words = count_words(sentence)
save_dict_to_file(words, 'srp_output2.txt')


# ######################################################################################################################
class User:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f"{self.name} {self.birth_year}"


class HRMS:

    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def show_users(self):
        for user in self._users:
            print(user)

    def save_users_to_db(self, file_path):
        import json
        user_list = [str(user) for user in self._users]
        with open(file_path, 'w') as f:
            json.dump(user_list, f)


john = User('John', 1978)
anna = User('Anna', 2000)
hrms = HRMS()
hrms.add_user(john)
hrms.add_user(anna)
hrms.show_users()
hrms.save_users_to_db('users.json')

# ######################################################################################################################
class HRMS:

    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def get_users(self):
        return self._users


class UI:

    def __init__(self, hrms):
        self._hrms = hrms

    def show_users(self):
        for user in self._hrms.get_users():
            print(user)


class DBManager:

    def __init__(self, hrms):
        self._hrms = hrms

    def save_users_to_db(self, file_path):
        import json
        user_list = [str(user) for user in self._hrms.get_users()]
        with open(file_path, 'w') as f:
            json.dump(user_list, f)


john = User('John', 1978)
anna = User('Anna', 2000)

hrms = HRMS()
ui = UI(hrms)
db_manager = DBManager(hrms)

hrms.add_user(john)
hrms.add_user(anna)

ui.show_users()

db_manager.save_users_to_db('users.json')
