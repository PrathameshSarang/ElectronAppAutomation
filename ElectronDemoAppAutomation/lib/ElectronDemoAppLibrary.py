from selenium import webdriver


class ElectronDemoAppLibrary(object):

    def __init__(self):
        self.driver = None
        print("Electron Demo App library initialized")

    def launch_app(self, app_name):
        options = webdriver.ChromeOptions()
        options.binary_location = "E:/SoftwareInstallations/electornDemoApp/ElectronAPIDemos.exe"
        options.add_argument('localhost:9222')
        self.driver = webdriver.Chrome(chrome_options=options)
        window_title = self.driver.find_element_by_xpath('//header/h1').text
        print(window_title)


    def click_on(self, identifier_name):
        print('%s clicked' % identifier_name)
        # TODO: Selenium code to click on identifier


    def new_window_should_open_with_text(self, expected_status):
        # TODO: Add code to retrieve window contents from the new window.
        _status = 'Hello World!'  # TODO: Set this value using selenium code
        if expected_status != _status:
            raise AssertionError("Expected status to be '%s' but was '%s'." % (expected_status, _status))


    def close_the_application(self):
        self.driver.quit()
        print('Application closed')
