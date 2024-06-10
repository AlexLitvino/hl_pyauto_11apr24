import json
from enum import StrEnum


class Results(StrEnum):
    PASS = 'pass'
    FAIL = 'fail'


# class SimpleTestReporter:
#
#     def save_report(self, file_path, results):
#         with open(file_path, 'w') as f:
#             json.dump(results, f)
#
#
# class TestResults:
#
#     def __init__(self):
#         self.results = {}
#         self.reporter = SimpleTestReporter()
#
#     def add_result(self, test_id, result):
#         self.results[test_id] = result
#
#     def store_report(self, file_path):
#         self.reporter.save_report(file_path, self.results)
#
#
# tr = TestResults()
# tr.add_result('id001', Results.PASS)
# tr.add_result('id002', Results.PASS)
# tr.add_result('id003', Results.FAIL)
# tr.store_report('test_results.json')

# ######################################################################################################################

from abc import ABC, abstractmethod

class AbstractReporter(ABC):

    @abstractmethod
    def save_report(self, file_path, results):
        pass

class JSONTestReporter(AbstractReporter):

    def save_report(self, file_path, results):
        with open(file_path, 'w') as f:
            json.dump(results, f)


class TextTestReporter(AbstractReporter):

    def save_report(self, file_path, results):
        with open(file_path, 'w') as f:
            for id_, result in results.items():
                f.write(f"{id_}    {result}\n")


class TestResults:

    def __init__(self, reporter):
        self.results = {}
        self.reporter = reporter

    def add_result(self, test_id, result):
        self.results[test_id] = result

    def store_report(self, file_path):
        self.reporter.save_report(file_path, self.results)


text_reporter = TextTestReporter()
tr = TestResults(text_reporter)
tr.add_result('id001', Results.PASS)
tr.add_result('id002', Results.PASS)
tr.add_result('id003', Results.FAIL)
tr.store_report('test_results.txt')