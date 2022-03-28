import sys
from catalog.catalog import Catalog
from selenium.common.exceptions import WebDriverException


def script_summary() -> None:
    print('''
        \t\tDUMELANG means GREETINGS! ~ G-CODE\n
        \t"THE-TUBE-SCRAPER" Version 1.1.0\n
        This script will help you collect video metadata from any YouTube channel.\n
        No need for installation. Just double-click this "the_tube_scraper.exe" to run it.\n
        The script will collect the channel data and video details and save them in a csv\n
        file, you can then open this csv file with any spreadsheet program e.g. (Microsoft Excel)\n
        and view the information you have gathered. Please make sure you keep this window\n
        (the command prompt) open and you don't disturb the browser window that opens after.\n
        Follow the instructions and you will have the results you desire.
    ''')


def tuber_droid(search_name: str) -> None:
    try:
        with Catalog() as android:
            android.launch_the_tube(search_name)
            android.channel_manoeuvre(f'{search_name}')
            android.load_entire_page()
            android.find_the_uploads(search_name)

    except Exception as exp:

        if 'in PATH' in str(exp):

            print(''''

                            Please make sure you have not deleted or moved or renamed the "chromedriver.exe"

                            file that is next to the "the_tube_scraper.exe". The programme needs it to work.

                            If you still get this error, then you need to download the chromedriver for your 

                            version of Chrome. There are many videos on YouTube about how to get that set up.

                            Once you are done downloading it, you unzip it and then replace the current one.

                            ''')

            input('\nPress Enter To Exit.\n')

        elif 'INTERNET' in str(exp):

            print(''''

                            Please make sure you are connected to the internet and Try again.

                            Cheers!

                            ''')

            input('\nPress Enter To Exit.\n')

        elif WebDriverException:

            if 'version' in str(exp):

                print('\nPlease make sure your version of Google Chrome is at least version 97.\n'

                      'Open your Chrome browser and go to "Menu -> Help -> About Google Chrome"\n'

                      'to update your web browser.\n'

                      'If you get this error message after updating your Google Chrome, then you\n'

                      'will need to download an updated version of chromedriver.\n'

                      'Visit https://chromedriver.chromium.org/downloads and download the chromedriver\n'

                      'that matches your version of Google Chrome. Once downloaded, unzip the download\n'

                      'and copy the file named chromedriver.exe & paste it in the same place as\n'

                      'this tube_channel_downloader.exe. Then you will be good to go!')

            else:
                print('\nSomething went wrong, please make sure you do not disturb the Google Chrome window\n'

                      'while it works when you try again.')

            input('\nPress Enter To Exit & try again.\n')


def main() -> None:
    script_summary()
    search_name = input('\nEnter Artist / Channel Name: ').title().strip()
    if len(search_name) >= 1:
        tuber_droid(search_name)
    elif len(search_name) < 1:
        print('\nYou have to type something.')
        input('\nPress Enter to Exit: ')
        sys.exit()


if __name__ == '__main__':
    main()
