from abc import ABC, abstractmethod


class Displayable(ABC):

    @abstractmethod
    def display(self):
        raise NotImplementedError


class Button(Displayable):

    def __init__(self, name: str, callback: callable):
        self.name = name
        self.callback = callback

    def click(self):
        print(f"Button {self.name} is clicked")
        self.callback()

    def display(self):
        print(f"Button: {self.name}")


class Header(Displayable):

    def __init__(self, title):
        self.title = title

    def display(self):
        print(f"Header: {self.title}")


class Label(Displayable):

    def __init__(self, value:str):
        self._value = value

    def display(self):
        print(f"Label: {self._value}")

    def get_value(self):
        return self._value

    def update_value(self, new_value):
        self._value = new_value


class CounterScreen:

    def __init__(self):
        self._screen_elements = []
        self._header = Header('Counter')
        self._counter_label = Label('0')
        self._up_button = Button('Up', lambda: self._counter_label.update_value(int(self._counter_label.get_value())+1))
        self._down_button = Button('Down', lambda: self._counter_label.update_value(int(self._counter_label.get_value())-1))
        self._screen_elements.append(self._header)
        self._screen_elements.append(self._counter_label)
        self._screen_elements.append(self._up_button)
        self._screen_elements.append(self._down_button)

    def show(self):
        print()
        for screen_element in self._screen_elements:
            screen_element.display()
        print()

    def click_up_button(self):
        self._up_button.click()

    def click_down_button(self):
        self._down_button.click()


counter_screen = CounterScreen()
counter_screen.show()
counter_screen.click_up_button()
counter_screen.show()
counter_screen.click_up_button()
counter_screen.show()
for _ in range(3):
    counter_screen.click_down_button()
counter_screen.show()
