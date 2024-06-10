class ResultsNotifier:

    def __init__(self, client):
        self.slack_client = client

    def notify(self, message):
        self.slack_client.send(message)

# ######################################################################################################################

class ResultsNotifier:

    def __init__(self, client):
        self.client = client

    def notify(self, message):
        if self.client.type == 'slack':
            # other code
            self.client.send(message)
        elif self.client.type == 'msteams':
            # other code
            self.client.send(message)

# ######################################################################################################################

from abc import ABC, abstractmethod


class AbstractNotifier(ABC):

    @abstractmethod
    def __init__(self, auth_data):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class SlackNotifier(AbstractNotifier):

    def __init__(self, auth_data):
        self.client = SlackClient(auth_data)

    def notify(self, message):
        self.client.send(message)


class MSTeamsNotifier(AbstractNotifier):

    def __init__(self, auth_data):
        self.client = MSTeamsClient(auth_data)

    def notify(self, message):
        self.client.send(message)
