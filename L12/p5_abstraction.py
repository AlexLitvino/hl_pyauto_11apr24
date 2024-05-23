class Button:

    def __init__(self, name):
        self.name = name

    def click(self):
        print(f"Button {self.name} is clicked")


from abc import ABC, ABCMeta, abstractmethod, abstractstaticmethod

class BasePage(ABC):
#class BasePage(metaclass=ABCMeta):

    def __init__(self):
        print("Base")

    def click_on_element(self):
        pass

    def swipe(self):
        pass

    @abstractmethod
    def get_screen_name(self):
        raise NotImplementedError

    # @staticmethod
    # @abstractmethod
    # def static(self):
    #     pass

print(BasePage.__bases__)
base_page = BasePage()
print(base_page)
base_page.get_screen_name()


class EULAPage(BasePage):

    def get_screen_name(self):
        pass

    def __init__(self):
        super().__init__()
        self.close_button = Button("Close")

    def close(self):
        self.close_button.click()

    def get_eula_text(self):
        return 'qwerertty'



class AboutPage(BasePage):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.close_button = Button("Close")

    def close(self):
        self.close_button.click()

    def get_app_version(self):
        return '1.2.0'


class ClosableIF(ABC):

    @abstractmethod
    def close(self):
        pass
