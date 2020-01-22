# ElectronAppAutomation

## Link of application to download
https://github.com/electron/electron-api-demos/releases

## Basic Selenium code to launch app 
```
options = webdriver.ChromeOptions()
options.binary_location = "E:/SoftwareInstallations/electornDemoApp/ElectronAPIDemos.exe"
options.add_argument('localhost:9222')
self.driver = webdriver.Chrome(chrome_options=options)
```
