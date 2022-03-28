import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class GetTheUploads:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_channel_name(self) -> WebElement:
        channel_name = self.driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div['
                                                          '3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout'
                                                          '/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div['
                                                          '1]/ytd-channel-name/div/div/yt-formatted-string')
        return channel_name

    def channel_data(self, artist_name: str) -> None:

        videos_list = self.driver.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two'
                                                         '-column-browse-results-renderer/div['
                                                         '1]/ytd-section-list-renderer/div['
                                                         '2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div['
                                                         '1]').find_elements(By.TAG_NAME, 'ytd-grid-video-renderer')

        print('\n\t\t-------------------------------------------------------------------------')
        channel_name = str(self.get_channel_name().text)
        print(f'\t\t\t\t---> CHANNEL DATA FOR "{channel_name.title()}" <---')
        print('\t\t-------------------------------------------------------------------------')
        print('\t\tCHANNEL NAME: ' + channel_name)
        subscriber_count = str(self.driver.find_element(By.ID, 'subscriber-count').text).split(' ')[0]
        print('\t\tSUBSCRIBERS: ' + subscriber_count)
        video_count = str(len(videos_list))
        print('\t\tNUMBER OF VIDEOS: ' + video_count + ' Videos!')
        print('-----------------------------------------------------------')

        with open(f'{artist_name}\'s Youtube Channel Uploads.csv', 'w', newline='', encoding='utf-8') as csv_file:
            headings = ['CHANNEL NAME', 'TOTAL VIDEOS', 'SUBSCRIBERS']

            csv_writer = csv.DictWriter(csv_file, fieldnames=headings)
            csv_writer.writeheader()

            csv_writer.writerow(
                {'CHANNEL NAME': channel_name, 'TOTAL VIDEOS': video_count, 'SUBSCRIBERS': subscriber_count})
            csv_writer.writerow({'CHANNEL NAME': '', 'TOTAL VIDEOS': '', 'SUBSCRIBERS': ''})

    def item_listing(self) -> None:

        video_div = self.driver.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two'
                                                       '-column-browse-results-renderer/div['
                                                       '1]/ytd-section-list-renderer/div['
                                                       '2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div['
                                                       '1]').find_elements(By.TAG_NAME, 'ytd-grid-video-renderer')

        channel_name = str(self.get_channel_name().text)

        for video in video_div:
            print('-----------------------------------------------------------')
            video_title = video.find_element(By.ID, 'video-title').text
            print('VIDEO TITLE: ' + video_title)
            print('ARTIST / OWNER: ' + str(channel_name))
            vdo_length = video.find_element(By.ID, 'thumbnail').find_element(By.TAG_NAME, 'span')
            print('LENGTH: ' + str(vdo_length.get_attribute('innerHTML')).strip())
            upload_date = video.find_element(By.ID, 'metadata-line')
            print('UPLOADED: ' + str(upload_date.text).split('\n')[-1].strip())
            view_count = video.find_element(By.ID, 'metadata-line')
            print('VIEW COUNT: ' + str(view_count.text).split('\n')[0].strip())
            print('-----------------------------------------------------------')

    def write_to_csv(self, artist_name: str) -> None:

        video_container = self.driver.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd'
                                                             '-two-column-browse-results-renderer/div['
                                                             '1]/ytd-section-list-renderer/div['
                                                             '2]/ytd-item-section-renderer/div['
                                                             '3]/ytd-grid-renderer/div[1]').find_elements(
            By.TAG_NAME, 'ytd-grid-video-renderer')

        with open(f'{artist_name}\'s Youtube Channel Uploads.csv', 'a', newline='', encoding='utf-8') as csv_file:
            column_headings = ['VIDEO TITLE', 'ARTIST', 'DURATION', 'UPLOADED', 'VIEW COUNT']

            csv_writer = csv.DictWriter(csv_file, fieldnames=column_headings, extrasaction='ignore')

            csv_writer.writeheader()
            csv_writer.writerow({'VIDEO TITLE': '', 'ARTIST': '', 'DURATION': '', 'UPLOADED': '', 'VIEW COUNT': ''})

            for video in video_container:
                video_title = video.find_element(By.ID, 'video-title')
                vid_title = str(video_title.text).split('-')[-1].strip()

                video_length = video.find_element(By.ID, 'thumbnail').find_element(By.TAG_NAME, 'span')
                vid_length = str(video_length.get_attribute('innerHTML').strip())

                uploaded_date = video.find_element(By.ID, 'metadata-line')
                upload_date = str(uploaded_date.text).split('\n')[-1].strip()

                viewer_count = video.find_element(By.ID, 'metadata-line')
                view_count = str(viewer_count.text).split('\n')[0].strip()

                video_item = (
                    {'VIDEO TITLE': vid_title, 'ARTIST': artist_name, 'DURATION': vid_length, 'UPLOADED': upload_date,
                     'VIEW COUNT': view_count})

                csv_writer.writerow(video_item)
