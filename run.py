from catalog.catalog import Catalog


def tuber_droid(search_name):
    try:

        with Catalog() as android:
            android.launch_the_tube(search_name)
            android.channel_manoeuvre(f'{search_name}')
            android.refresh()
            android.load_entire_page()
            android.find_the_uploads(search_name)

    except Exception as e:
        if 'in PATH' in str(e):
            print(''''
                You need to download & add Google Chrome's Webdriver to the PATH variable\n
                Copy & paste the following line and then edit accordingly:
                    set PATH=%PATH%;C:path-location-of-the-Webdriver
                ''')

        elif 'ERR_INTERNET_' in str(e):
            print(''''
                Please make sure you are connected to the internet and Try again.
                Cheers!
                ''')

        else:

            raise

def main():
    search_name = input('Enter Artist / Channel Name: ').title()
    tuber_droid(search_name)


if __name__ == '__main__':
    main()
