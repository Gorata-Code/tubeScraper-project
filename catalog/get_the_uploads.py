import csv
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class GetTheUploads:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_channel_name(self):
        channel_name = self.driver.find_element(By.CLASS_NAME, 'style-scope ytd-channel-name')
        return channel_name

    def channel_data(self, artist_name):

        video_list = self.driver.find_element(By.XPATH,
                             '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]').find_elements(
            By.TAG_NAME, 'ytd-grid-video-renderer')

        print('-----------------------------------------------------------')
        channel_name = str(self.get_channel_name().text)
        print('CHANNEL NAME: ' + channel_name)
        subscriber_count = str(self.driver.find_element(By.ID, 'subscriber-count').text).split(' ')[0]
        print('SUBSCRIBERS: ' + subscriber_count)
        video_count = str(len(video_list))
        print('This channel contains ' + video_count + ' videos!')
        print('-----------------------------------------------------------')

        with open(f'{artist_name}\'s Youtube Channel Uploads.csv', 'w', newline='', encoding='utf-8') as csv_file:

            headings = ['CHANNEL NAME', 'TOTAL VIDEOS', 'SUBSCRIBERS']

            csv_writer = csv.DictWriter(csv_file, fieldnames=headings)
            csv_writer.writeheader()

            csv_writer.writerow({'CHANNEL NAME': channel_name, 'TOTAL VIDEOS': video_count, 'SUBSCRIBERS': subscriber_count})
            csv_writer.writerow({'CHANNEL NAME': '', 'TOTAL VIDEOS': '', 'SUBSCRIBERS': ''})

    def item_listing(self):

        video_div = self.driver.find_element(By.XPATH,
                             '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]').find_elements(
            By.TAG_NAME, 'ytd-grid-video-renderer')

        for video in video_div:

            print('-----------------------------------------------------------')
            song_title = video.find_element(By.ID, 'video-title')
            video_title = str(song_title.text).split('-')[-1].strip()
            print('SONG TITLE: ' + video_title)
            artist_name = video.find_element(By.ID, 'video-title')
            artist = str(artist_name.text).split('-')[0].strip()
            print('ARTIST: ' + str(artist))
            vid_length = video.find_element(By.CLASS_NAME, 'style-scope ytd-thumbnail-overlay-time-status-renderer')
            print('LENGTH: ' + str(vid_length.text))
            upload_date = video.find_element(By.ID, 'metadata-line')
            print('UPLOADED: ' + str(upload_date.text).split('\n')[-1].strip())
            view_count = video.find_element(By.ID, 'metadata-line')
            print('VIEW COUNT: ' + str(view_count.text).split('\n')[0].strip())
            print('-----------------------------------------------------------')

    def write_to_csv(self, artist_name):

        video_container = self.driver.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]').find_elements(By.TAG_NAME, 'ytd-grid-video-renderer')

        with open(f'{artist_name}\'s Youtube Channel Uploads.csv', 'a', newline='', encoding='utf-8') as csv_file:

            column_headings = ['VIDEO TITLE', 'ARTIST', 'DURATION', 'UPLOADED', 'VIEW COUNT']

            csv_writer = csv.DictWriter(csv_file, fieldnames=column_headings, extrasaction='ignore')

            csv_writer.writeheader()
            csv_writer.writerow({'VIDEO TITLE': '', 'ARTIST': '', 'DURATION': '', 'UPLOADED': '', 'VIEW COUNT': ''})

            for video in video_container:

                video_title = video.find_element(By.ID, 'video-title')
                vid_title = str(video_title.text).split('-')[-1].strip()

                video_length = video.find_element(By.CLASS_NAME, 'style-scope ytd-thumbnail-overlay-time-status-renderer')
                vid_length = str(video_length.text)

                uploaded_date = video.find_element(By.ID, 'metadata-line')
                upload_date = str(uploaded_date.text).split('\n')[-1].strip()

                viewer_count = video.find_element(By.ID, 'metadata-line')
                view_count = str(viewer_count.text).split('\n')[0].strip()

                video_item = ({'VIDEO TITLE': vid_title, 'ARTIST': artist_name, 'DURATION': vid_length, 'UPLOADED': upload_date, 'VIEW COUNT': view_count})

                csv_writer.writerow(video_item)
