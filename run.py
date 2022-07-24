import sys
from catalog.catalog import Catalog
from win32com.client import Dispatch
from selenium.common.exceptions import WebDriverException


def script_summary() -> None:
    print('''
               ***----------------------------------------------------------------------------------------***
         \t***------------------------ DUMELANG means GREETINGS! ~ G-CODE -----------------------***
                     \t***------------------------------------------------------------------------***\n
              
        \t"THE-TUBE-SCRAPER" Version 1.2.0\n
        
        This script will help you collect video metadata from any YouTube channel.\n
        No need for installation. Just double-click this "The Tube Scraper.exe" to run it.\n
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

        if 'executable needs to be in PATH' in str(exp):
            print('''
                       Please make sure you have not deleted or moved or renamed the "chromedriver.exe"

                       file that is next to the "The Tube Scraper.exe". The programme needs it

                       to work.

                       ''')

            input('\nPress Enter To Exit.\n')
            sys.exit(1)

        elif 'version of ChromeDriver only supports Chrome version' in str(exp):
            message: str = str(exp).split('\n')[0].split(':')[-1]
            print(f'''
                       {message}.

                        You need to download the ChromeDriver that is compatible with your version of Chrome.

                        Please refer to the information about GOOGLE CHROME & CHROME_DRIVER above. 

                        Once you are done downloading the ChromeDriver, you unzip it and then 

                        replace the current one by placing the new one in the same folder as

                        this "The Tube Scraper.exe".

                    ''')
            input('\nPress Enter To Exit.\n')
            sys.exit(1)

        elif 'INTERNET' in str(exp):

            print(''''

                            Please make sure you are connected to the internet and Try again.

                            Cheers!

                            ''')

            input('\nPress Enter To Exit.\n')
            sys.exit(1)

        elif WebDriverException:

            if 'version' in str(exp):

                print('\nPlease make sure your version of Google Chrome is at least version 103.\n'

                      'Open your Chrome browser and go to "Menu -> Help -> About Google Chrome"\n'

                      'to update your web browser.\n')

            else:
                print('\nSomething went wrong, please make sure you do not disturb the Google Chrome window\n'

                      'while it works when you try again.')

            input('\nPress Enter To Exit & try again.\n')
            sys.exit(1)

        elif 'Timed out receiving message from renderer' or 'cannot determine loading status' in str(exp):
            print('\nGoogle Chrome is taking too long to respond :( .')

        elif 'ERR_NAME_NOT_RESOLVED' or 'ERR_CONNECTION_CLOSED' or 'unexpected command response' in str(exp):
            print('\nYour internet connection may have been interrupted.')
            print('Please make sure you\'re still connected to the internet and try again.')

        else:
            print('\nSomething went wrong, please make sure you do not disturb the Google Chrome window\n'
                  'while it works when you try again.')

        input('\nPress Enter to Exit & Try Again.')
        sys.exit(1)


def detect_browser_version(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version


if __name__ == "__main__":
    script_summary()
    absolute_paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                      r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
    users_browser_version = list(filter(None, [detect_browser_version(p) for p in absolute_paths]))[0]
    print('YOUR GOOGLE CHROME VERSION: ' + users_browser_version)
    print(f'IF YOU NEED TO DOWNLOAD THE CHROME_DRIVER: https://chromedriver.chromium.org/downloads\n')


def main() -> None:
    search_name = input('\nEnter Artist / Channel Name: ').title().strip()
    if len(search_name) >= 1:
        tuber_droid(search_name)
    elif len(search_name) < 1:
        print('\nYou have to type something.')
        input('\nPress Enter to Exit: ')
        sys.exit()


if __name__ == '__main__':
    main()
