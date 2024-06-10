from abc import ABC, abstractmethod


class AbstractLocalizer(ABC):

    @abstractmethod
    def localize(self, message):
        pass


class EnglishLocalizer(AbstractLocalizer):

    def localize(self, message):
        return message


class SpanishLocalizer(AbstractLocalizer):

    def __init__(self):
        self.translate_mapping = {'white': 'blanco',
                                  'red': 'rojo'}

    def localize(self, message):
        return self.translate_mapping.get(message, message)


class LocalizatorFactory:

    def __init__(self):
        self.localizator_mapping = {'en': EnglishLocalizer,
                                    'es': SpanishLocalizer}

    def get_localizator(self, locale):
        return self.localizator_mapping.get(locale, 'en')()


localizator_factory = LocalizatorFactory()
spanish = localizator_factory.get_localizator('es')
print(spanish.localize('red'))
print(spanish.localize('black'))
