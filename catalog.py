import os
import time
from selenium import webdriver
import catalog.constants as const
from selenium.webdriver.common.by import By
from catalog.get_the_uploads import GetTheUploads


class Catalog(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=True):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.page_load_strategy = 'normal'
        super(Catalog, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def launch_the_tube(self, search_name):
        self.get(const.URL + f'/results?search_query={search_name}')

    def channel_manoeuvre(self, search_name):
        channels = self.find_elements(By.ID, 'channel-name')
        for channel in channels:
            if channel.text == f'{search_name}':
                channel.click()
                break
        video_tab = self.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')
        video_tab.click()

    def load_entire_page(self):
        start_size = self.execute_script("return document.documentElement.scrollHeight")

        while True:
            self.execute_script("window.scrollTo(0, " + str(start_size) + ");")
            time.sleep(2)

            scroll_size = self.execute_script("return document.documentElement.scrollHeight")

            if scroll_size == start_size:
                break

            start_size = scroll_size

    def find_the_uploads(self, search_name):
        the_find = GetTheUploads(driver=self)
        the_find.channel_data(search_name)
        the_find.item_listing()
        the_find.write_to_csv(search_name)
