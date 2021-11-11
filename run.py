from catalog.catalog import Catalog


search_name = input('Enter Artist / Channel Name: ').title()

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
            You need to download & add Google Chrome's Webriver to the PATH variable\n
            Copy & paste the following line and then edit accordingly:
                set PATH=%PATH%;C:path-location-of-the-Webdriver
            ''')

    else:
        raise

