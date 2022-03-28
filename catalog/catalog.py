import os
import sys
import time
from selenium import webdriver
import catalog.constants as const
from selenium.webdriver.common.by import By
from catalog.get_the_uploads import GetTheUploads
from selenium.common.exceptions import WebDriverException


def resource_path(relative_path) -> [bytes, str]:
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Catalog(webdriver.Chrome):

    def __init__(self, driver_path=resource_path(r"./SeleniumDrivers"), teardown=True):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.page_load_strategy = 'normal'
        super(Catalog, self).__init__(options=options)
        self.implicitly_wait(45)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def launch_the_tube(self, search_name: str) -> None:
        print('\n\tLaunching Google Chrome...\n')
        self.get(const.BASE_URL + f'/results?search_query={search_name}')

    def channel_manoeuvre(self, search_name: str) -> None:
        the_channel = []
        try:
            count = 0
            channels = self.find_elements(By.ID, 'channel-name')
            for channel in channels:
                if count == 8:
                    start_size = self.execute_script("return document.documentElement.scrollHeight")
                    self.execute_script("window.scrollTo(0, " + str(start_size) + ");")
                if channel.text.casefold() == f'{search_name}'.casefold():
                    channel.click()
                    print(f'We have found your channel "{channel.text}".')
                    print('\n\tSwitching to the "VIDEOS" tab. Please wait...\n')
                    the_channel.append(channel)
                    videos_screen = self.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')
                    videos_screen.click()
                    input('After your browser has switched to the "VIDEOS" screen and the video thumbnails on\nthe '
                          'first '
                          'row are showing,\nPress Enter to continue: ')
                    break
                elif channel.text.casefold() != f'{search_name}'.casefold() and channels.index(channel) == -1:
                    print(
                        f'\n\t\tSorry, we could not find any channel with the name "{search_name}".\n\t\tPlease '
                        f'check your spelling and try again.')
                    input('\nPress Enter to quit: ')
                    sys.exit()
                count += 1
        except WebDriverException as exp:
            if 'no such element' in str(exp):
                print('\nNo such channel exists. Please try a different channel name.')
                input('\nPress Enter to quit: ')
            print(str(exp))
            sys.exit()

        if len(the_channel) < 1:
            print('\nNo matching channel name found. Please try a different one.\n')
            input('Press Enter to quit: \n')
            sys.exit()

    def load_entire_page(self) -> None:
        start_size = self.execute_script("return document.documentElement.scrollHeight")

        while True:
            self.execute_script("window.scrollTo(0, " + str(start_size) + ");")
            time.sleep(5)

            scroll_size = self.execute_script("return document.documentElement.scrollHeight")

            if scroll_size == start_size:
                break

            start_size = scroll_size

    def find_the_uploads(self, search_name: str) -> None:
        the_find = GetTheUploads(driver=self)
        the_find.channel_data(search_name)
        the_find.item_listing()
        the_find.write_to_csv(search_name)
        print('\n\t-----> Channel Scraping SUCCESSFUL! Your csv file has been created! <-----')
        input('\nPress Enter to Exit: ')
