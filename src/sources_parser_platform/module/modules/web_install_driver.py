from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebInstallerDriver:

    def __new__(cls, dir_path: str, *args, **kwargs) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument('headless')

        chrome_prefs = {
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True,
            "download.open_pdf_in_system_reader": False,
            "profile.default_content_settings.popups": 0,
            "download.default_directory": dir_path,
        }
        options.add_experimental_option("prefs", chrome_prefs)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
