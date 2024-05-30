class Label:
    def __init__(self, text):
        self.text = text


class AndroidWelcomeLabel:

    text = "Welcome to Android app\nDeveloped by Company"  # in real life it is Appium object attribute


class iOSWelcomeLabel:

    labelApp = Label('Welcome to iOS app')
    labelCompany = Label('Developed by Company')

    @property
    def text(self):
        return f'{iOSWelcomeLabel.labelApp.text}\n{iOSWelcomeLabel.labelCompany.text}'


class StartPage:

    platform = 'Android'

    def __getattr__(self, item):
        if item == 'welcomeLabel':
            if StartPage.platform == 'Android':
                return AndroidWelcomeLabel()
            elif StartPage.platform == 'iOS':
                return iOSWelcomeLabel()


# Test script get text for welcome text
ANDROID = 'Android'
iOS = 'iOS'

StartPage.platform = ANDROID
startPage = StartPage()
print(startPage.welcomeLabel.text)
