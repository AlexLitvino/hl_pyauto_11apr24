class Button:

    def __init__(self, name):
        self.name = name

    def click(self):
        print(f"Button {self.name} is clicked")

class BasePage:

    def __init__(self):
        print("Base")


class EULAPage(BasePage):

    def __init__(self):
        super().__init__()
        self.close_button = Button("Close")

    def close(self):
        self.close_button.click()


eula_page = EULAPage()
eula_page.close()


class CloseMixin:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def close(self):
        self.close_button.click()


class AboutPage(CloseMixin, BasePage):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.close_button = Button("Close")

about_page = AboutPage()
about_page.close()
