DECIMAL = 10

from enum import Enum, IntEnum, unique, StrEnum

#@unique
#class Status(Enum):
class Status(IntEnum):
    SUCCESS = 200
    HAPPY = 200
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_ERROR = 500

print(Status.SUCCESS)
print(type(Status.SUCCESS))
print(Status.SUCCESS.name)
print(Status.SUCCESS.value)

print(Status.SUCCESS < Status.SERVER_ERROR)

class Browers(StrEnum):
    CHROME = 'chrome'
    FIREFOX = 'firefox'

browser_type = 'chrome'
if browser_type == Browers.CHROME.value:
    print("Create driver for chrome")
