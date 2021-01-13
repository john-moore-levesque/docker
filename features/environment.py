from firefox import before_all as firefoxBrowser
import geckodriver_autoinstaller


def before_all(context):
    '''
    If "chrome" is true, then a Chrome browser will be created
    If "firefox" is true, a Firefox browser will be created
    Otherwise it returns False
    '''
    geckodriver_autoinstaller.install()
    firefoxBrowser(context)
